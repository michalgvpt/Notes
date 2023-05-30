import tkinter as tk
import random
root = tk.Tk()
canvas = tk.Canvas(root, width=700, height=700)
canvas.pack()
boats = []
step = 0
winner = []
first = True
starter = True
counter = 0

def sail(x, y):
    plachta = random.randint(-3, 3)
    canvas.create_line(x, y, x, y-25, x+10+plachta, y-10, x, y-5)
    canvas.create_polygon(x-20, y, x+20, y, x+10, y+8, x-10, y+8)

def setup():
    for i in range(15):
        sail(20, i * 40 + 40)
        boats.append(1 + 2 * i)
    canvas.create_line(650, 0, 650, 700, fill='red')

def start(e):
    global starter
    if starter:
        mover()
        starter = False

def mover():
    global step, first, counter
    for i, j in enumerate(boats):
        line_coord = canvas.coords(j)
        move = random.randint(1, 10)
        canvas.delete(j)
        canvas.delete(j+1)
        sail(line_coord[0] + move, line_coord[1])
        if first:
            boats[i] += 31
        else:
            boats[i] += 30
        if len(canvas.find_overlapping(650, 0, 650, 700)) > 1:
            winner.append((j - 30 * counter - 1)//2 + 1)
        if len(canvas.find_overlapping(652, 0, 652, 700)):
            canvas.create_text(350, 350, text='The winner boat is: ' + str(winner[0]), font=('Helvetica', '30', 'bold'), fill='red', anchor=tk.CENTER)
            return
    first = False
    counter += 1
    canvas.after(100, mover)

setup()
canvas.bind('<Button-1>', start)
root.mainloop()