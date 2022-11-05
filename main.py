import pygame as pg
from game import MainGame
from text import Text
from colors import *
from button import Button
from maze_generator import generate_maze, find_shortest_path
pg.init()

# constant values
try:
    res = input("Enter the resolution (example 640 mean 640x640): ")
    WIDTH, HEIGHT = int(res), int(res)
except:
    WIDTH, HEIGHT = 640, 640
FPS = 60

# colors


screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Escape The Maze")
clock = pg.time.Clock()


def render_end_of_game(text):
    lost_text = Text(text, (WIDTH/2, HEIGHT/2))
    screen.fill("white")
    lost_text.render_to_screen(screen)


def main(maze_size):
    steps = 0
    while steps < maze_size*1.5:
        maze = generate_maze(maze_size)
        steps = find_shortest_path(maze)
    game_state = "main"
    running = True
    screen.fill(ORANGE)
    level_text = Text(f"Level: {maze_size//15}", (50, 20), 64)
    main_game = MainGame(screen, WIDTH, HEIGHT, maze, steps)
    restart_btn = Button(
        "Restart", (WIDTH/2, HEIGHT*2//3), (WIDTH/4, HEIGHT/8))
    quit_btn = Button("Quit", (WIDTH-30, 15),
                      (60, 30))
    next_btn = Button("Next", (WIDTH/2, HEIGHT*2/3), (WIDTH/4, HEIGHT/8))
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                raise SystemExit
            if event.type == pg.MOUSEBUTTONDOWN:
                if restart_btn.on_click(pg.mouse.get_pos()) and game_state == "lost":
                    return 0
                if next_btn.on_click(pg.mouse.get_pos()) and game_state == "won":
                    return 15
                if quit_btn.on_click(pg.mouse.get_pos()):
                    pg.quit()
                    raise SystemExit
            if game_state == "main":
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:
                        return 0
                temp_state = main_game.detect_key_down(event)
                if type(temp_state) == str:
                    game_state = temp_state
            elif game_state == "won":
                render_end_of_game(
                    f"You won!")
                next_btn.render_to_screen(screen)
                quit_btn.render_to_screen(screen)
            elif game_state == "lost":
                render_end_of_game(
                    f"You lost!")
                restart_btn.render_to_screen(screen)
                quit_btn.render_to_screen(screen)
            level_text.render_to_screen(screen)
        pg.display.flip()
        clock.tick(FPS)


if "__main__" == __name__:
    maze_size = 10
    while True:
        count = main(maze_size)
        maze_size += count if maze_size + count < 200 else 0
