import tkinter as tk
window=tk.Tk()
W=1000
H=750
canvas = tk.Canvas(width=W,height=H,bg="white")
canvas.pack()

file = open('Game of life/imput.txt',"r")
text = file.readline()
width, height = text.split(' ')
width = int(width)
height = int(height)
list_cell=[]
size=20

def create2Dmap(width, height):
    map = []
    temp = []
    for y in range(height):
        for x in range(width):
            temp.append(0)
        map.append(temp)
        temp = []
    return map

def processfile(map):
    x, y = 0, 0
    for row in file:
        for char in row:
            if char == '1':
                map[y][x] = 1
            x += 1
        y += 1
        x = 0

def FindNeighbours(x,y,map):
    count = 0

    if x<width-1 and map[y][x+1] == 1:
        count += 1
    if x<width-1 and y<height-1 and map[y+1][x+1] == 1:
        count += 1
    if y<height-1 and map[y+1][x] == 1:
        count += 1
    if x>0 and y<height-1 and map[y+1][x-1] == 1:
        count += 1
    if x>0 and map[y][x-1] == 1:
        count += 1
    if x>0 and y>0 and map[y-1][x-1] == 1:
        count += 1
    if y>0 and map[y-1][x] == 1:
        count += 1
    if x<width-1 and y>0 and map[y-1][x+1] == 1:
        count += 1
    return count

def rewrite(map):
    global oldmap
    x = 0
    y = 0
    newmap = create2Dmap(width, height)
    for row in map:
        for char in row:
            neighbours = FindNeighbours(x, y, oldmap)
            if map[y][x] == 1:
                if neighbours == 2 or neighbours == 3:
                    newmap[y][x] = 1
                else:
                    newmap[y][x] = 0
            elif map[y][x] == 0 and neighbours == 3:
                newmap[y][x] = 1
            else:
                newmap[y][x] = 0
            x += 1
        y += 1
        x = 0
    oldmap = newmap
    return newmap

oldmap = create2Dmap(width, height)
newmap = create2Dmap(width, height)
processfile(oldmap)

def drawGrid(ws=size):
    count=H//ws
    for i in range(count):
        canvas.create_line(0,i*ws,W,i*ws)
    count=W//ws
    for i in range(count):
        canvas.create_line(i*ws,0,i*ws,H)

def drawCells(oldmap,list_cell,ws = size):
    canvas.delete('all')
    drawGrid()
    list_cell = []
    for y in range(height):
        for x in range(width):
            if oldmap[y][x]==1:
                list_cell.append(canvas.create_oval(x*ws,y*ws,(x+1)*ws,(y+1)*ws,fill='blue'))

# def generations():
#     global oldmap
#     drawCells(oldmap,list_cell)
#     rewrite(oldmap)
#     canvas.after(100,generations)

def autoGen():
    global oldmap
    drawCells(oldmap, list_cell)
    rewrite(oldmap)
    canvas.after(100, autoGen)

def nextGen():
    global oldmap
    drawCells(oldmap, list_cell)
    rewrite(oldmap)

nextGen()
auto_button = tk.Button(window, text='Auto', command=autoGen)
auto_button.pack()
step_button = tk.Button(window, text='Next step', command=nextGen)
step_button.pack()

drawGrid()
#generations()
window.mainloop()
