import random

size = 20
meX = random.randint(1, 10)
meY = 16
bX=[random.randint(1, 10)]
bY = 1
maze = []
for i in range(size):
    maze.append([])
    for j in range(size):
        if i == meX and j == meY:
            maze[i].append(2)
        elif i == bX[0] and j == bY:
            maze[i].append(3)
        elif j >16:
            maze[i].append(1)
        else:
            maze[i].append(0)

print(maze)