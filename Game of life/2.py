import tkinter as tk
window=tk.Tk()
WIDTH=1000
HEIGHT=1000
canvas = tk.Canvas(width=WIDTH,height=HEIGHT,bg="white")
canvas.pack()
file = open('input.txt',"r")

text = file.readline()
width, height = text.split(" ")
width = int(width)
height = int(height)
listcell=[]

def create2Dmap() ->list:
    map = []
    temp = []
    for row in file:
        for char in row:
            if char == "1":
                temp.append(1)
            if char == "0":
                temp.append(0)
        map.append(temp)
        temp = [ ]
    file.seek(0)
    file.readline()
    return map

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

#teraz sa pozrem do mapy budem ju prechadzat pre kazde policko sa spytam kolko mas priatelov
# prechadzam cyklus v cykle vrat mi pocet priatelov pri kazdom ak si 2 ci co tak zdochnes ak nieco ine tak zijes ...?

oldmap = create2Dmap()
newmap = create2Dmap()

def rewrite(oldmap,newmap):
    for y in range(height):
        for x in range(width):
            neighbours = FindNeighbours(x,y,oldmap)
            if oldmap[y][x] == 1:
                if neighbours<2:
                    newmap[y][x] = 0
                elif neighbours ==2 or neighbours ==3:
                    newmap[y][x] = 1
                elif neighbours >2:
                    newmap[y][x] = 0
            if oldmap[y][x] == 0 and neighbours ==3:
                newmap[y][x]= 1

    return newmap

def drawGrid(ws=30):
    count=HEIGHT//ws
    for i in range(count):
        canvas.create_line(0,i*ws,WIDTH,i*ws)
    count=WIDTH//ws
    for i in range(count):
        canvas.create_line(i*ws,0,i*ws,HEIGHT)

def drawCells(oldmap,listcell,ws):
    canvas.delete('all')
    drawGrid(ws)
    for y in range(height):
        for x in range(width):
            if oldmap[y][x]==1:
                listcell.append(canvas.create_oval(x*ws,y*ws,(x+1)*ws,(y+1)*ws,fill='blue'))

def generations():
    global oldmap,newmap
    drawCells(oldmap,listcell,30)
    rewrite(oldmap,newmap)
    for y in range(height):
        for x in range(width):
            oldmap[y][x]=newmap[y][x]
    newmap=create2Dmap()
    canvas.after(100,generations)

drawGrid()
generations()
window.mainloop()
