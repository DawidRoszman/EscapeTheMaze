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
    def __init__(self, screen, WIDTH, HEIGHT, BASE_MAZE):
        self._screen = screen
        self._WIDTH = WIDTH
        self._HEIGHT = HEIGHT
        self._player = Player((1, 1))
        self._maze = BASE_MAZE[:]
        self._turns_left = 20
        self._turns_left_text = Text(
            f"TurnsLeft: {self._turns_left}", (WIDTH/2, 20), 64)

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
                self._turns_left -= 1
            if self._turns_left <= 0:
                return "lost"
            self._turns_left_text.change_text(f"TurnsLeft: {self._turns_left}")

            self._screen.fill(GREY)
        for i in range(7):
            for j in range(7):
                if self._maze[j][i] == 0:
                    color = WHITE
                elif self._maze[j][i] == 1:
                    color = ORANGE
                elif self._maze[j][i] == 2:
                    color = GREEN
                else:
                    color = YELLOW
                pg.draw.rect(self._screen, color, pg.Rect(((self._WIDTH/len(self._maze))*i+1,
                                                           self._HEIGHT/len(self._maze)*j+1), (self._WIDTH/len(self._maze)-2, self._HEIGHT/7-2)))
        self._turns_left_text.render_to_screen(self._screen)
