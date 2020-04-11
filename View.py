import Model
import Control
import tkinter as tk

window = tk.Tk()
window.geometry("1300x700")
window.resizable(True, True)
window.title("Падающие ящики")

canvas = tk.Canvas(window, width=700, height=700)
canvas.pack()
r = 30
for i in range(Model.size):
    for j in range(Model.size):
        if Model.maze[i][j] == 1:
            color = 'brown'
        elif Model.maze[i][j] == 2:
            color = 'pink'
        elif Model.maze[i][j] == 3:
            color = 'yellow'
        else:
            color = 'blue'
        canvas.create_rectangle(r * i + 100, r * j + 100, r * i + r + 100, r * j + r + 100, fill=color)

window.bind('<Up>', lambda event: Control.move(canvas, 0, -1))
window.bind('<Down>', lambda event: Control.move(canvas, 0, 1))
window.bind('<Left>', lambda event: Control.move(canvas, -1, 0))
window.bind('<Right>', lambda event: Control.move(canvas, 1, 0))

def f():
    for i in range(Model.size):
        for j in range(Model.size):
                if Model.maze[i][j] == 3:

                    canvas.create_rectangle(r * i + 100, r * j + 100, r * i + r + 100, r * j + r + 100, fill='blue')
                    Model.maze.insert(j, 0)
                    i += 1
                    Model.maze.insert(j, 3)
                    canvas.create_rectangle(r * i + 100, r * j + 100, r * i + r + 100, r * j + r + 100, fill='yellow')
    window.after(10000, lambda: f())
f()
window.mainloop()