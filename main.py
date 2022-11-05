import pygame as pg
from game import MainGame
from text import Text
from colors import *
from button import Button
pg.init()

# constant values
WIDTH, HEIGHT = 640, 480
FPS = 60

# colors


screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Escape The Maze")
clock = pg.time.Clock()


def print_array(array):
    for i in array:
        for j in i:
            print(j, end=" ")
        print("\n")


def render_end_of_game(text):
    lost_text = Text(text, (WIDTH/2, HEIGHT/2))
    screen.fill("white")
    lost_text.render_to_screen(screen)


def main():
    maze = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 2, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 3, 1],
        [1, 1, 1, 1, 1, 1, 1],
    ]
    game_state = "main"
    running = True
    screen.fill(GREY)
    main_game = MainGame(screen, WIDTH, HEIGHT, maze)
    restart_btn = Button(
        "Restart", (WIDTH/2, HEIGHT/2+50), (WIDTH/4, HEIGHT/8))
    quit_btn = Button("Quit", (WIDTH-30, 15),
                      (60, 30))
    new_game = False
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                raise SystemExit
            if event.type == pg.MOUSEBUTTONDOWN:
                if restart_btn.on_click(pg.mouse.get_pos()):
                    new_game = True
                    break
                if quit_btn.on_click(pg.mouse.get_pos()):
                    pg.quit()
                    raise SystemExit
            if game_state == "main":
                temp_state = main_game.detect_key_down(event)
                if type(temp_state) == str:
                    game_state = temp_state
            elif game_state == "won":
                render_end_of_game(
                    f"You won! Turns left: {main_game._turns_left}")
                restart_btn.render_to_screen(screen)
                quit_btn.render_to_screen(screen)
            elif game_state == "lost":
                render_end_of_game("You lost!")
                restart_btn.render_to_screen(screen)
                quit_btn.render_to_screen(screen)
        if new_game:
            break
        pg.display.flip()
        clock.tick(FPS)


if "__main__" == __name__:
    while True:
        main()
