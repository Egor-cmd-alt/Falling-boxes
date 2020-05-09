import Model

r = 30



def move(canvas, a, b):
    if canvas.coords('i')[3] < 610 and canvas.coords('i')[0] > 100 and canvas.coords('i')[2] < 700 and canvas.coords('i')[1] > 100:
        canvas.move('i', a, b)
    elif canvas.coords('i')[3] == 610:
        if b == r :
            canvas.move('i', a, 0)
        else:
            canvas.move('i', a, b)
    elif  canvas.coords('i')[0] == 100:
        if a == 5 :
            canvas.move('i', a, b)
        else:
            canvas.move('i', 0, b)
    elif canvas.coords('i')[1] == 100:
        if b == r :
            canvas.move('i', a, b)
        else:
            canvas.move('i', a, 0)
    elif canvas.coords('i')[2] == 700:
        if a == 5 :
            canvas.move('i', 0, b)
        else:
            canvas.move('i', a, b)
