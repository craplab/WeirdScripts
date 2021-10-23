import tkinter as tk
import threading
import time
import json
globalBoard = []

def main():
    global globalBoard
    root = tk.Tk()
    root.title("Conway's Game Of Life -Click to add cell, right click to remove")
    myCanvas, globalBoard = setUp(root,500,500)
    generateDefaultBoardState(myCanvas,globalBoard)
    importBoard()
    for row in globalBoard:
        for cell in row:
            if(cell["val"] == 1):
                drawSquare(cell["x"],cell["y"],myCanvas,globalBoard,True)
    root.mainloop()

def generateDefaultBoardState(canvas,board):
    x = 0
    y = 0
    for row in board:
        y=0
        for cell in row:
            drawSquare(x,y,canvas,board,False)
            y+=1
        x+=1
    
    
    #tick(board,canvas)
def drawSquare(posx,posy,canvas,board,live):
    if(live == True):
        board[posx][posy] = {"val":1,"x":posx,"y":posy}
        posx = posx*10
        posy =posy*10
        canvas.create_rectangle(0+posx,0+posy,10+posx,10+posy,fill="#000000",outline="#a8a8a8")
    else:
        board[posx][posy] = {"val":0,"x":posx,"y":posy}
        posx = posx*10
        posy =posy*10
        canvas.create_rectangle(0+posx,0+posy,10+posx,10+posy,fill="#ffffff",outline="#e6e6e6")
    return
    
    
def tick(board,canvas):
    nextBoard = [x[:] for x in board]
    for row in board:
        for cell in row:
            if(cell["val"]==1):
                n = getNumberOfNeighbors(board,cell["x"],cell["y"])
                if(n < 2):
                    drawSquare(cell["x"],cell["y"],canvas,nextBoard,False)
                elif(n > 3):
                    drawSquare(cell["x"],cell["y"],canvas,nextBoard,False)
            elif(cell["val"]==0):
                n = getNumberOfNeighbors(board,cell["x"],cell["y"])
                if(n == 3):
                    drawSquare(cell["x"],cell["y"],canvas,nextBoard,True)
    return nextBoard
                
def getNumberOfNeighbors(board,x,y):
    neighbors = 0
    try:
        y1 = y-1
        for i in range(3):
            x1 = x-1
            for z in range(3):
                if(board[x1]
                [y1]["val"] 
                == 1 and [x1,y1] != [x,y]):
                    neighbors+=1
                z+=1
                x1+=1
            i+=1
            y1+=1
    except IndexError:
        pass
    return neighbors
    
def clickEvent(event,canvas,tf):
    global globalBoard
    x = event.x//10
    y = event.y//10
    drawSquare(x,y,canvas,globalBoard,tf)
    
def setUp(root,x,y):
    myCanvas = tk.Canvas(root, bg="white", height=y, width=y)
    def lClick(event,canvas=myCanvas):
        return clickEvent(event,canvas,True)
    def rClick(event,canvas=myCanvas):
        return clickEvent(event,canvas,False)
    myCanvas.bind("<Button-1>",lClick)
    myCanvas.bind("<Button-3>",rClick)
    board = []
    for i in range(int(y//10)):
        line = []
        z=0
        for z in range(int(x//10)):
            line.append(0)
            z+=1
        board.append(line)
        i+=1
    myCanvas.pack()
    btnFrame = tk.Frame(root)
    btnFrame.pack(side="bottom")
    startBtn = tk.Button(btnFrame,text="Start",bg='#dbdbdb')
    startBtn.config(command=lambda: toggle(myCanvas,startBtn))
    editBtn = tk.Button(btnFrame,text="Clear",bg='#dbdbdb')
    editBtn.config(command=lambda: clear(myCanvas,editBtn))
    startBtn.pack(side="left")
    editBtn.pack(side="left")
    return myCanvas, board
def importBoard():
    global globalBoard
    with open('./default.json') as f:
        obj = json.load(f)["obj"]
        globalBoard = obj
thread = None
def toggle(canvas,btn):
    changeBtnColorOnPress(btn,'#02eb40',"Start","Stop")
    if(btn["bg"] == '#02eb40'):
        def subTick():
            while(btn["bg"] == '#02eb40'):
                global globalBoard
                globalBoard = tick(globalBoard,canvas)
                time.sleep(.1)
        x = threading.Thread(target=subTick)
        x.start()
        
def clear(canvas,btn):
    global globalBoard
    #changeBtnColorOnPress(btn,'#858585',"edit","stop editing")
    generateDefaultBoardState(canvas,globalBoard)
def changeBtnColorOnPress(btn,color,text1,text2,defaultColor='#dbdbdb'):
    if(btn["bg"]==color):
        btn.config(bg=defaultColor,text=text1)
    else:
        btn.config(bg=color,text=text2)

if __name__ == '__main__':
    main()
    