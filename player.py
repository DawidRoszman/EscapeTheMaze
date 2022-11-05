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
