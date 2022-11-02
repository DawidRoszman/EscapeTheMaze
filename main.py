def print_array(array):
    for i in array:
        for j in i:
            print(j, end=" ")
        print("\n")


def move_player(array, move_dir, player_position) -> [list, tuple[int, int]]:
    new_player_pos = (player_position[0] + move_dir[0], player_position[1] + move_dir[1])
    x = array[new_player_pos[0]][new_player_pos[1]]
    if x == 0:
        array[new_player_pos[0]][new_player_pos[1]] = 2
        array[player_position[0]][player_position[1]] = 0
    if x == 3:
        print("Congrats you won")
        return False
    if x == 1:
        return array, player_position
    return array, new_player_pos


def get_input() -> tuple[int, int]:
    x = input("Choose direction(['w' - up] ['s' - down] ['d' - right] ['a' - left]):  ")
    if x == "w":
        return -1, 0
    elif x == "d":
        return 0, 1
    elif x == "s":
        return 1, 0
    elif x == "a":
        return 0, -1
    else:
        return 0, 0


class Player:

    def __init__(self, player_pos):
        self.player_pos = player_pos

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

    while turns_left > 0:
        print("Turns: ", turns_left)
        print_array(lab)
        current_move_dir = get_input()
        if not move_player(lab, current_move_dir, player.get_current_position()):
            break
        lab, new_player_position = move_player(lab, current_move_dir, player.get_current_position())
        player.change_player_position(new_player_position)
        turns_left -= 1

    if turns_left <= 0:
        print("You failed!")


if "__main__" == __name__:
    main()
