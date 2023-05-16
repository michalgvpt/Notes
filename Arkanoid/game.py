import tkinter as tk 
import random
from PIL import ImageTk, Image
root=tk.Tk()
width=500
height=500
movement = [0,1]
ws = 10
rec_w = 25
bricks=[]
brick_w=50
brick_h=20
brick_collum=10
brick_row=5
value='none'
canvas = tk.Canvas(root,width=width,height=height,bg='white')
canvas.pack()
bi_image=tk.PhotoImage(file='Arkanoid/background.png')
canvas.create_image(0,0, image=bi_image, anchor=tk.NW)
ball = canvas.create_oval(width//2 - ws, height//2 - ws, width//2 + ws, height//2 + ws, fill = 'red')
desk = canvas.create_rectangle(width//2 - rec_w, height - 25, width//2 + rec_w, height - 20, fill= 'dark blue')

def destroy_brick():
    global movement
    coord_ball=canvas.coords(ball)
    items_list=canvas.find_overlapping(coord_ball[0],coord_ball[1],coord_ball[2],coord_ball[3])
    for i in items_list:
        if i in bricks:
            bricks.remove(i)
            canvas.delete(i)
            movement=[movement[0]* -1,movement[1]* -1]
            break

def ball_move():
    global ball, movement, desk
    canvas.move(ball, movement[0], movement[1])
    destroy_brick()
    pos = canvas.coords(ball)
    desk_pos = canvas.coords(desk)
    overlap = canvas.find_overlapping(desk_pos[0], desk_pos[1], desk_pos[2], desk_pos[3])
    if pos[2] >= width:     # prava hranica
        # movement = [-1, 1]
        movement = [movement[0] * -1, movement[1]]
    elif pos[3] >= height:  # spodna hranica
        canvas.delete('all')
        text = canvas.create_text(width//2, height//2, text='You Lost')
    elif pos[0] <= 0:       # lava hranica
        # movement = [1, -1]
        movement = [movement[0] * -1, movement[1]]
    elif pos[1] <= 0:       # vrchna hranica
        # movement = [1, 1]
        movement = [movement[0], movement[1] * -1]
    elif ball in overlap:
        # movement = [-1, -1]
        movement = bounce(pos, desk_pos)
    canvas.after(2, ball_move)

def bounce(ball_pos, rec_pos):
    ball_pos = (ball_pos[0] + ball_pos[2])//2
    rec_middle = (rec_pos[0] + rec_pos[2])//2
    ball_to_rec = ball_pos - rec_middle
    return [ball_to_rec//(rec_w//3), -1]    # rec_w//3 => vector x je 0-3

# root.wm_attributes('-transparentcolor', '#ab23ff')

def prepare_bricks():
    for y in range(brick_row):
        for x in range(brick_collum):
            bricks.append(canvas.create_rectangle(x*brick_w,y*brick_h,x*brick_w+brick_w,y*brick_h+brick_h, fill='grey', width=5, outline='black'))

def victory():
    if len(bricks)==0:
        canvas.delete('all')
        text = canvas.create_text(width//2, height//2, text='You Won')

def move_left(e):
    canvas.move(desk, -5, 0)

def move_right(e):
    canvas.move(desk, 5, 0)

def hardcore_mode():
    canvas.itemconfig(desk, fill='black')  

def easy_mode():
    canvas.itemconfig(desk, fill='yellow') 

button1=tk.Button(root, text='Hardcore Mode', command=hardcore_mode)
button1.pack()
button2=tk.Button(root, text='Easy Mode', command=easy_mode)
button2.pack()
victory()
ball_move()
prepare_bricks()
root.bind('<Left>',move_left)
root.bind('<Right>',move_right)
root.mainloop()
