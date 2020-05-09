import random

size = 20
meX = random.randint(1, 10)
meY = 16
bX=random.randint(1, 10)
bY = 1
maze = []
for i in range(size):
    maze.append([])
    for j in range(size):
        if j >16:
            maze[i].append(1)
        else:
            maze[i].append(0)
me=[]
for i in range(size):
    me.append([])
    for j in range(size):
        if i == meX and j == meY:
            me[i].append(2)
        else:
            me[i].append(0)
box=[]
for i in range(size):
    box.append([])
    for j in range(size):
        if i == bX and j == bY:
            box[i].append(3)
        else:
            box[i].append(0)
print(maze)
print(me)
print(box)
