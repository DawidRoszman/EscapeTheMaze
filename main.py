import pygame as pg
import pygame.display

pg.init()

# constant values
WIDTH, HEIGHT = 640, 480
FPS = 60

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Escape The Maze")
clock = pg.time.Clock()


def print_array(array):
    for i in array:
        for j in i:
            print(j, end=" ")
        print("\n")


def get_input(input_key) -> tuple[int, int]:
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
    def __init__(self, text, pos):
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
        new_player_pos = (player_position[0] + move_dir[0], player_position[1] + move_dir[1])
        x = array[new_player_pos[0]][new_player_pos[1]]
        if x == 0:
            array[new_player_pos[0]][new_player_pos[1]] = 2
            array[player_position[0]][player_position[1]] = 0
            self.change_player_position(new_player_pos)
        if x == 3:
            self.change_player_position(new_player_pos)
            print("Congrats you won")
            return False
        if x == 1:
            return array
        return array

    def change_player_position(self, new_player_pos):
        self.player_pos = new_player_pos

    def get_current_position(self):
        return self.player_pos


class MainGame:
    def __init__(self, screen, WIDTH, HEIGHT):
        self._screen = screen
        self._WIDTH = WIDTH
        self._HEIGHT = HEIGHT
        self._player = Player((1, 1))
        self._lab = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 2, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 3, 1],
        [1, 1, 1, 1, 1, 1, 1],
    ]
        self._turns_left = 20
        self._turns_left_text = Text(f"TurnsLeft: {self._turns_left}", (WIDTH/2, 20))

    def detect_key_down(self, event):
        if event.type == pg.KEYDOWN:
            current_move_dir = get_input(chr(event.key))
            player_move = self._player.move_player(self._lab, current_move_dir, self._player.get_current_position())
            if not player_move:
                return "won"
            self._lab = player_move
            self._turns_left -= 1
            self._turns_left_text.change_text(f"TurnsLeft: {self._turns_left}")

            self._screen.fill("white")
        for i in range(7):
            for j in range(7):
                if self._lab[j][i] == 0:
                    color = "black"
                elif self._lab[j][i] == 1:
                    color = "brown"
                elif self._lab[j][i] == 2:
                    color = "blue"
                else:
                    color = "yellow"
                pg.draw.rect(self._screen, color, pygame.Rect(((self._WIDTH/len(self._lab))*i+1, self._HEIGHT/len(self._lab)*j+1), (self._WIDTH/len(self._lab)-2, self._HEIGHT/7-2)))
        self._turns_left_text.render_to_screen(self._screen)

def end_of_game():
    pass


def main():
    game_state = "main"
    running = True
    won_text = Text("You won", (WIDTH/2, HEIGHT/2))
    main_game = MainGame(screen, WIDTH, HEIGHT)
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                raise SystemExit
            if game_state == "main": 
                temp_state = main_game.detect_key_down(event)
                if temp_state == "won":
                    game_state = temp_state
        pygame.display.flip()
        if game_state == "won":
            screen.fill("white")
            won_text.render_to_screen(screen)
        clock.tick(FPS)


if "__main__" == __name__:
    main()
