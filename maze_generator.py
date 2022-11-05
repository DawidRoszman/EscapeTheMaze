from random import randint


def generate_maze(size):
    maze = []
    for i in range(size):
        maze.append([])
        for j in range(size):
            maze[i].append(4)
    for i in range(1, size-1):
        for j in range(1, size-1):
            maze[i][j] = 1
    # maze[1][1] = 2
    step = (1, 1)
    i = (size*size)
    while i > 0:
        maze[step[0]][step[1]] = 0
        if randint(0, 1) == 0:
            new_step = (step[0]+randint(-1, 1), step[1])
        else:
            new_step = (step[0], step[1]+randint(-1, 1))
        if maze[new_step[0]][new_step[1]] != 4:
            step = new_step
            i -= 1
    maze[1][1] = 2
    maze[step[0]][step[1]] = 3
    return maze


