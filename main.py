import numpy as np

col = row = 7

player_pos = (1,1)

lab = [
    [1,1,1,1,1,1,1],
    [1,2,1,0,0,0,1],
    [1,0,1,0,1,1,1],
    [1,0,0,0,0,0,1],
    [1,0,1,1,1,0,1],
    [1,0,0,0,1,3,1],
    [1,1,1,1,1,1,1],
]

def printArray(array):
    for i in array:
        for j in i:
            print(j,end=" ")
        print("\n")

def getInput() -> int:
    x = input("Wybierz ruch: ")
    if x == "w":
        return (-1,0)
    elif x == "d":
        return (0,1)
    elif x == "s":
        return (1,0)
    elif x == "a":
        return (0,-1)
    else: return 0

def movePlayer(array, move_dir, player_pos):
    new_player_pos = (player_pos[0]+move_dir[0], player_pos[1]+move_dir[1])
    x = array[new_player_pos[0]][new_player_pos[1]]
    if x == 0:
        array[new_player_pos[0]][new_player_pos[1]] = 2
        array[player_pos[0]][player_pos[1]] = 0
    if x == 3:
        print("Congrats you won")
        return False
    if x == 1:
        return (array, player_pos)
    return (array, new_player_pos)
        
turns_left = 20
running = True
while turns_left > 0:
    print("Turns: ", turns_left)
    printArray(lab)
    curret_move_dir = getInput()
    if movePlayer(lab, curret_move_dir, player_pos) == False:
        break
    lab,player_pos = movePlayer(lab, curret_move_dir, player_pos)
    turns_left -=1
    
print("You failed")