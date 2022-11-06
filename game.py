from player import Player
from text import Text
from colors import *
import pygame as pg


def get_input(input_key):
    if input_key == "w":
        return -1, 0
    elif input_key == "d":
        return 0, 1
    elif input_key == "s":
        return 1, 0
    elif input_key == "a":
        return 0, -1
    else:
        return 0, 0


class MainGame:
    def __init__(self, screen, WIDTH, HEIGHT, BASE_MAZE, required_steps):
        self._screen = screen
        self._WIDTH = WIDTH
        self._HEIGHT = HEIGHT
        self._player = Player((1, 1))
        self._maze = BASE_MAZE[:]
        self._steps = required_steps
        self._turns_left_text = Text(
            f"Steps: {self._steps}", (WIDTH/2, 20), 32)

    def detect_key_down(self, event):
        if event.type == pg.KEYDOWN:
            if event.key not in [97, 119, 100, 115]:
                return
            current_move_dir = get_input(chr(event.key))
            temp_player_pos = self._player.get_current_position()
            player_move = self._player.move_player(
                self._maze, current_move_dir, self._player.get_current_position())
            if not player_move:
                return "won"
            self._maze = player_move
            if self._player.get_current_position() != temp_player_pos:
                self._steps -= 1
            if self._steps == 0:
                return "show_path"
            self._turns_left_text.change_text(f"Steps: {self._steps}")

            self._screen.fill(ORANGE)
        for i in range(len(self._maze)):
            for j in range(len(self._maze[i])):
                if self._maze[j][i] == 0:
                    color = WHITE
                elif self._maze[j][i] in [1, 4]:
                    color = ORANGE
                elif self._maze[j][i] == 2:
                    color = GREEN
                else:
                    color = "black"
                pg.draw.rect(self._screen, color, pg.Rect(((self._WIDTH//len(self._maze))*i,
                                                           self._HEIGHT//len(self._maze)*j), (self._WIDTH//len(self._maze)-1, self._HEIGHT//len(self._maze)-1)))
        self._turns_left_text.render_to_screen(self._screen)
