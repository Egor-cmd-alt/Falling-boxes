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
            tag='ground'
        elif Model.maze[i][j] == 0:
            color = 'blue'
            tag='fon'
        elif Model.maze[i][j] == 3:
            color = 'yellow'
            tag='box'
        else:
            color = 'pink'
            tag = 'i'

        canvas.create_rectangle(r * i + 100, r * j + 100, r * i + r + 100, r * j + r + 100, fill=color, tag=tag)

def move(canvas,a,b):
    Control.move(canvas,a,b)









window.bind('<Up>', lambda event: move(canvas, 0, -r))
window.bind('<Down>', lambda event: move(canvas, 0, r))
window.bind('<Left>', lambda event: move(canvas, -r, 0))
window.bind('<Right>', lambda event: move(canvas, r, 0))


window.mainloop()
