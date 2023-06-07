import tkinter as tk
import random as rnd
root=tk.Tk()
root.title('Snake')
width=500
height=500
canvas = tk.Canvas(root,width=width,height=height,bg='white')
canvas.pack()
start=[500//2,500//2]
v_c=[0,-1]
w_s=[start]
speed=100
end_font = ('Arial', 50, 'bold')

def setup():
    global start, v_c, speed
    canvas.create_rectangle(start[0],start[1],start[0],start[1], fill='black')
    overlap=canvas.find_overlapping(start[0],start[1],start[0],start[1])
    start[0]+=v_c[0]
    start[1]+=v_c[1]
    if len(overlap)>1:
        canvas.delete('all')
        canvas.create_text(500//2,500//2,text='You lost', font=end_font)
    else:
        canvas.after(speed, setup)

def change(e):
    global v_c, speed
    if e.char=='w':
        v_c=[0,-1]
    elif e.char=='a':
        v_c=[-1,0]
    elif e.char=='d':
        v_c=[1,0]
    elif e.char=='s':
        v_c=[0,1]
    elif e.char=='k' and speed>=1:
        speed-=10
    elif e.char=='l':
        speed+=10


setup()
root.bind('<Key>',change)
root.mainloop()
