import tkinter as tk
import random as rnd
root = tk.Tk()
root.title('Plates')
width = 610
height = 100
canvas = tk.Canvas(root, width=width, height=height, bg='white')
canvas.pack()
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
chosen_plate = rnd.choice(letters)
clicked_letters = []
end_font = ('Arial', 15, 'bold')

def create_oval(canvas, x, y, letter):
    oval_width = 50
    oval_height = 50
    oval_color = 'blue'
    letter_color = 'white'
    oval_font = ('Arial', 20, 'bold')
    oval = canvas.create_oval(x, y, x + oval_width, y + oval_height, fill=oval_color)
    letter = canvas.create_text(x + oval_width / 2, y + oval_height / 2, text=letter, fill=letter_color, font=oval_font)
    canvas.itemconfig(oval, tags=(letter,))
    canvas.tag_bind(letter, '<ButtonPress-1>', click)
    return oval

def create_text():
    oval_width = 50
    spacing = 10
    x = 10
    y = 10
    for i, letter in enumerate(letters):
        create_oval(canvas, x, y, letter)
        x += oval_width + spacing
        canvas.tag_bind(i+1, '<ButtonPress-1>', click)

def click(e):
    global chosen_plate, clicked_letters
    clicked_item = canvas.find_withtag(tk.CURRENT)
    clicked_oval = clicked_item[0]
    clicked_letter = canvas.itemcget(clicked_oval, 'text')
    clicked_letters.append(clicked_letter)
    if clicked_letter == chosen_plate:
        canvas.delete(tk.ALL)
        text = canvas.create_text(width//2, height//2, text='You have clicked on the correct plate')
        label.config(text='You clicked on: {}'.format(clicked_letters))

label = tk.Label(root, text='')
label.pack()
create_text()
root.mainloop()