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
bckg=tk.PhotoImage(file='Images/ostrov3.png')
bckg2=tk.PhotoImage(file='Images/ostrov0.png')

for y in range(c_h):
    for x in range(c_w):
        chance=rnd.random()
        if chance>=0.2:
            canvas.create_image(p_w*x,p_h*y, image=bckg, anchor=tk.NW)
        else:
            canvas.create_image(p_w*x,p_h*y, image=bckg2, anchor=tk.NW)






root.mainloop()
