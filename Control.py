import Model

r = 30
y = Model.meY
x = Model.meX


def move(canvas, a, b):
    global x, y
    if Model.maze[x][y] == 1 or x>19 or x<0 or y>19 or y<0:
        x += 0
        y += 0
    elif Model.maze[x][y] == 0 or Model.maze[x][y] == 2:
        canvas.move('i',a,b)
    elif Model.maze[x + a][y + b] == 3:
        x+=0
        y+=0
