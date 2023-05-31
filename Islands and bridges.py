#refactoring of code is proces of modifying the code after it was written and is working
import tkinter as tk
import random as rnd
root=tk.Tk()
root.title('I and B')
width=300
height=450
p_w=50
p_h=50
c_w=rnd.randrange(4,7)
c_h=rnd.randrange(3,10)
canvas = tk.Canvas(root,width=width,height=height,bg='grey')
canvas.pack()
water=[]
islands=[]
bckg=tk.PhotoImage(file='Images/ostrov3.png')
bckg2=tk.PhotoImage(file='Images/ostrov0.png')
img1=tk.PhotoImage(file='Images/ostrov1.png')
img2=tk.PhotoImage(file='Images/ostrov2.png')

def setup():
    global water, islands
    for y in range(c_h):
        for x in range(c_w):
            chance = rnd.random()
            if chance >= 0.2:
                water.append(canvas.create_image(p_w*x,p_h*y, image = bckg, anchor = tk.NW))
            else:
                islands.append(canvas.create_image(p_w*x,p_h*y, image = bckg2, anchor = tk.NW))

def switch(e):
    global water
    list1=canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if len(list1)!=0 and list1[0] in water:
        n_x=(e.x//p_w)*p_w
        n_y=(e.y//p_h)*p_h
        temp=list1[0]
        canvas.delete(temp)
        water.remove(temp)
        canvas.create_image(n_x,n_y,image = img1, anchor = tk.NW, tag='bridge')

def spinner(e):
    list1=canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    canvas.itemconfig(list1[0],image=img2)

canvas.bind('<Button-1>', switch)
canvas.tag_bind('bridge','<Button-1>',spinner)
setup()
root.mainloop()
