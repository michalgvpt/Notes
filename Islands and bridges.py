#refactoring of code is proces of modifying the code after it was written and is working
import tkinter as tk
import random as rnd
root=tk.Tk()
root.title('I and B')
p_w=50
p_h=50
c_w=rnd.randrange(4,7)
c_h=rnd.randrange(3,10)
canvas = tk.Canvas(root,width=c_w*p_w+100,height=c_h*p_w,bg='grey') #offset posunutie
canvas.pack()
water=[]
islands=[]
status=[]
field_status = True
coins = 0
text = ''
bckg=tk.PhotoImage(file='Images/ostrov3.png')
bckg2=tk.PhotoImage(file='Images/ostrov0.png')
img1=tk.PhotoImage(file='Images/ostrov1.png')
img2=tk.PhotoImage(file='Images/ostrov2.png')
img3=tk.PhotoImage(file='Images/ostrov_kruh0.png')
img4=tk.PhotoImage(file='Images/ostrov_kruh1.png')

def setup():
    global water, islands
    for y in range(c_h):
        for x in range(c_w):
            chance = rnd.random()
            if chance >= 0.2:
                water.append(canvas.create_image(p_w*x,p_h*y, image = bckg, anchor = tk.NW))
            else:
                islands.append(canvas.create_image(p_w*x,p_h*y, image = bckg2, anchor = tk.NW))
    canvas.create_image(c_w*p_w+50,0, image= img3, anchor= tk.NW, tags='iswitch')

def switch(e):
    global water, coins, text
    list1=canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if len(list1)!=0 and list1[0] in water:
        n_x=(e.x//p_w)*p_w
        n_y=(e.y//p_h)*p_h
        temp=list1[0]
        canvas.delete(temp)
        water.remove(temp)
        if field_status == True:
            canvas.create_image(n_x, n_y, image=img1, anchor=tk.NW,tag="bridge")
            coins += 10
        if field_status == False:
            canvas.create_image(n_x, n_y, image=bckg2, anchor=tk.NW)
            coins += 50
    canvas.itemconfig(text, text=str(coins))

def spinner(e):
    list1=canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if canvas.itemcget(list1[0],'image')=='pyimage3':
        canvas.itemconfig(list1[0],image=img2)
    else:
        canvas.itemconfig(list1[0],image=img1)

def spinner2(e):
    global field_status
    list1=canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if canvas.itemcget(list1[0],'image')=='pyimage6':
        canvas.itemconfig(list1[0],image=img3)
        field_status = True
    else:
        canvas.itemconfig(list1[0],image=img4)
        field_status = False

text = canvas.create_text(c_w * p_w + 25, 25, text=str(coins), font="arial100")
canvas.bind('<Button-1>', switch)
canvas.tag_bind('bridge','<Button-1>',spinner)
canvas.tag_bind('iswitch','<Button-1>',spinner2)
setup()
root.mainloop()
