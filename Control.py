import Model

r = 30
y = Model.meY
x = Model.meX


def move(canvas, a, b):
    global x, y
    if Model.maze[x + a][y + b] == 1 or x+a>19 or x+a<0 or y+b>19  or y+b<0:
        x += 0
        y += 0
    elif Model.maze[x + a][y + b] == 0 or Model.maze[x + a][y + b] == 2:
        canvas.create_rectangle(r * x + 100, r * y + 100, r * x + r + 100, r * y + r + 100, fill='blue')
        x += a
        y += b
        canvas.create_rectangle(r * x + 100, r * y + 100, r * x + r + 100, r * y + r + 100, fill='pink')
    elif Model.maze[x + a][y + b] == 3:
        x+=0
        y+=0

