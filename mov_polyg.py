from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=800, height=800)
canvas.pack()
canvas.create_rectangle(1, 10, 25, 35,width=5, fill= 'green')
canvas.create_rectangle(10, 50, 50, 80, width=5, fill= 'blue')
canvas.create_rectangle(20, 100, 50, 135, width=5, fill= 'orange')

def movetriangle(event):
    if event.keysym == 'Up':
        canvas.move(1, 0, -2)
        canvas.move(2, 0, -4)
        canvas.move(3, 0, -5)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 2)
        canvas.move(2, 0, 3)
        canvas.move(3, 0, 5)
    elif event.keysym == 'Left':
        canvas.move(1, -2, 0)
        canvas.move(2, -4, 0)
        canvas.move(3, -5, 0)
    else:
        canvas.move(1, 2, 0)
        canvas.move(2, 4, 0)
        canvas.move(3, 5, 0)

canvas.bind_all('<KeyPress-Up>', movetriangle)
canvas.bind_all('<KeyPress-Down>', movetriangle)
canvas.bind_all('<KeyPress-Left>', movetriangle)
canvas.bind_all('<KeyPress-Right>', movetriangle)
tk.mainloop()