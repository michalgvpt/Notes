#Better than game of life v.0.1, easier I guess (For The Eyes)
#import tkinter as tk
#win = tk.Tk()
file = open("input.txt","r")

text = file.readline()
width, height = text.split(" ")
width = int(width)
height = int(height)


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

    if x-1>=0 and y-1>=0 and map[y-1][x-1] == 1:
        count +=1
    if y-1>=0 and map[y-1][x] == 1:
        count +=1
    if y-1>=0 and x+1<= height-1 and map[y-1][x+1] ==1:
        count +=1
    if x-1>=0 and map[y][x-1] == 1:
        count +=1
    if x+1<=width-1 and map[y][x+1] ==1:
        count +=1
    if y+1<=height-1 and x-1>=0 and map[y+1][x-1]==1:
        count+=1
    if y+1<=height-1 and map[y+1][x] ==1:
        count+=1
    if y+1<=height-1 and x+1<=width-1 and map[y+1][x+1] == 1:
        count+=1
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



#canvas = tk.Canvas(win,width*100,height*100,bg="white")
#canvas.pack()
#oldmap = rewrite(oldmap,newmap)
#def mapcreation(oldmap):
    #for y in range(0,height*100,100):
        #for x in range(0,width*100,100):
while True:
    print(oldmap)
    newmap = rewrite(oldmap,newmap)
    oldmap = newmap.copy()
    newmap = create2Dmap()
    #print stary matrix
    #vypocitas novy matrix
    #novy hodis do stareho - pomocou dvoch cyklov .copy() nie pretoze
    #novy musim vynulovat