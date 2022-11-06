from random import choice, randint
import numpy as np
import pygame as pg
import time


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
    i = (size*(size//2))
    counter = 2
    direction = (randint(0, 1), choice([-1, 1]))
    while i > 0:
        if counter == 0:
            direction = (randint(0, 1), choice([-1, 1]))
            counter = choice([6, 8, 10, 12])
        maze[step[0]][step[1]] = 0
        if direction[0] == 0:
            new_step = (step[0]+direction[1], step[1])
        else:
            new_step = (step[0], step[1]+direction[1])
        counter -= 1
        if maze[new_step[0]][new_step[1]] != 4:
            step = new_step
            i -= 1
    maze[1][1] = 2
    maze[step[0]][step[1]] = 3
    return maze

# find shortest path from 2 to 3 where 1 is wall and 0 is path


def find_shortest_path(maze):
    start = (1, 1)
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 3:
                end = (i, j)
            if maze[i][j] == 2:
                start = (i, j)
    queue = [start]
    path = {start: None}
    while queue:
        current = queue.pop(0)
        if current == end:
            break
        for next in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_step = (current[0]+next[0], current[1]+next[1])
            if 0 <= next_step[0] < len(maze) and 0 <= next_step[1] < len(maze) and maze[next_step[0]][next_step[1]] not in [1, 4] and next_step not in path:
                queue.append(next_step)
                path[next_step] = current
    current = end
    path_list = []
    while current != start:
        path_list.append(current)
        current = path[current]
    path_list.append(start)
    return path_list[::-1]


def draw_path(maze, path, screen, color, WIDTH, HEIGHT):
    for step in path:
        pg.draw.rect(screen, color, pg.Rect(((WIDTH//len(maze))*step[1],
                                             HEIGHT//len(maze)*step[0]), (WIDTH//len(maze)-1, HEIGHT//len(maze)-1)))
        pg.display.flip()
        time.sleep(0.05)
    time.sleep(1)
