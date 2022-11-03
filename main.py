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
        self.text = text
        self.pos = pos
        self.font = pg.font.SysFont("Roboto", 24)
        self.text_to_render = self.font.render(text, True, "black")
        self.rect = self.text_to_render.get_rect()
        self.rect.center = pos
    
    def render_to_screen(self, screen):
        screen.blit(self.text_to_render, self.rect)
    
    def change_text(self, new_text):
        self.text = new_text
        self.text_to_render = self.font.render(new_text, True, "black")
        self.rect = self.text_to_render.get_rect()
        self.rect.center = self.pos


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


def main():
    player = Player((1, 1))
    lab = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 2, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 3, 1],
        [1, 1, 1, 1, 1, 1, 1],
    ]
    turns_left = 20
    turns_left_text = Text(f"TurnsLeft: {turns_left}", (WIDTH/2, 20))

    while turns_left > 0:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                raise SystemExit
            if event.type == pg.KEYDOWN:
                current_move_dir = get_input(chr(event.key))
                player_move = player.move_player(lab, current_move_dir, player.get_current_position())
                if not player_move:
                    break
                lab = player_move
                turns_left -= 1
                turns_left_text.change_text(f"TurnsLeft: {turns_left}")

        screen.fill("white")
        for i in range(7):
            for j in range(7):
                if lab[j][i] == 0:
                    color = "black"
                elif lab[j][i] == 1:
                    color = "brown"
                elif lab[j][i] == 2:
                    color = "blue"
                else:
                    color = "yellow"
                pg.draw.rect(screen, color, pygame.Rect(((WIDTH/7)*i+1, HEIGHT/7*j+1), (WIDTH/7-2, HEIGHT/7-2)))
        turns_left_text.render_to_screen(screen)
        pygame.display.flip()
        clock.tick(FPS)

        # print("Turns: ", turns_left)
        # print_array(lab)
        # current_move_dir = get_input()


    if turns_left <= 0:
        print("You failed!")


if "__main__" == __name__:
    main()
