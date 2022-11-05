import pygame as pg

pg.init()

# constant values
WIDTH, HEIGHT = 640, 480
FPS = 60

# colors
YELLOW = (233, 215, 88)
GREEN = (41, 115, 115)
ORANGE = (255, 133, 82)
WHITE = (230, 230, 230)
GREY = (128, 128, 128)

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Escape The Maze")
clock = pg.time.Clock()


def print_array(array):
    for i in array:
        for j in i:
            print(j, end=" ")
        print("\n")


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


class Text:
    def __init__(self, text, pos, size=24, font="Roboto"):
        self._text = text
        self._pos = pos
        self._font = pg.font.SysFont("Roboto", 24)
        self._text_to_render = self._font.render(text, True, "black")
        self._rect = self._text_to_render.get_rect()
        self._rect.center = self._pos

    def render_to_screen(self, screen):
        screen.blit(self._text_to_render, self._rect)

    def change_text(self, new_text):
        self._text = new_text
        self._text_to_render = self._font.render(new_text, True, "black")
        self._rect = self._text_to_render.get_rect()
        self._rect.center = self._pos


class Player:

    def __init__(self, player_pos):
        self.player_pos = player_pos

    def move_player(self, array, move_dir, player_position):
        new_player_pos = (
            player_position[0] + move_dir[0], player_position[1] + move_dir[1])
        x = array[new_player_pos[0]][new_player_pos[1]]
        if x == 0:
            array[new_player_pos[0]][new_player_pos[1]] = 2
            array[player_position[0]][player_position[1]] = 0
            self.change_player_position(new_player_pos)
        if x == 3:
            self.change_player_position(new_player_pos)
            return False
        if x == 1:
            return array
        return array

    def change_player_position(self, new_player_pos):
        self.player_pos = new_player_pos

    def get_current_position(self):
        return self.player_pos


class Button:
    def __init__(self, text, pos, size) -> None:
        self._btn_text = Text(text, pos)
        self._btn_rect = pg.Rect(
            pos[0] - size[0] // 2, pos[1] - size[1] // 2, size[0], size[1])
        self._btn_color = GREY

    def render_to_screen(self, screen):
        pg.draw.rect(screen, self._btn_color, self._btn_rect)
        self._btn_text.render_to_screen(screen)

    def change_color(self, color):
        self._btn_color = color

    def get_rect(self):
        return self._btn_rect

    def get_text(self):
        return self._btn_text._text

    def on_click(self, mouse_pos):
        if self._btn_rect.collidepoint(mouse_pos):
            self.change_color(ORANGE)
            return True
        else:
            self.change_color(GREY)
            return False


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
