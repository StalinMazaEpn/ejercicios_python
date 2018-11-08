from tkinter import *
import time
import sys

tk = Tk()
ANCHOP = 800
ALTOP = 600
canvas = Canvas(tk,width=ANCHOP,heigh=ALTOP )
canvas.pack()
img = PhotoImage(file = "balon.gif")
img2 = PhotoImage(file = "arco.gif")
canvas.create_image(ANCHOP-32,100,anchor=NW,image=img)
canvas.create_image(0,0,anchor=NW,image = img2)

print("Coordenas Iniciales: " , 0,0)

x = 800
y = 100

def movetriangle(event):    
    global x 
    global y
    if event.keysym == 'Up':
        canvas.move(1, 0, -3)      
    elif event.keysym == 'Down':
        canvas.move(1, 0, 3)        
    elif event.keysym == 'Left':
        canvas.move(1, -3, 0)
        x = x -3
    else:
        canvas.move(1, 3, 0)
        x = x +3             
    print("Coordenadas Actuales:" , x ,y)
    if x <= 20:
        master = Tk()
        w = Message(master, text="Usted ha hecho un Gooooool")
        w.pack()
        sys.exit(0)
    
    
canvas.bind_all('<KeyPress-Up>', movetriangle)
canvas.bind_all('<KeyPress-Down>', movetriangle)
canvas.bind_all('<KeyPress-Left>', movetriangle)
canvas.bind_all('<KeyPress-Right>', movetriangle)
tk.mainloop()
