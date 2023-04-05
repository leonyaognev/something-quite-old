from tkinter import *

root = Tk()
q = False
def event_info1(event):
    global q
    q = True
def event_info2(event):
    global q
    q = False
def test(event):
    x = event.x
    y = event.y
    if q:
        can.coords(ball, x-10, y-10, x+10, y+10)

def go():
    cor1 = can.coords(ball)
    cor2 = can.coords(tamagochy)
    vec_x = 0
    vec_y = 0
    if cor1[0] > cor2[0]:
        vec_x = 1
    elif cor1[0] < cor2[0]:
        vec_x = -1
    if cor1[1] > cor2[1]:
        vec_y = 1
    elif cor1[1] < cor2[1]:
        vec_y = -1

    if cor1[1] == cor2[1] and cor1[0] == cor2[0]:
        if cor1[0] != 5:
            can.move("group1", -1, 0)
        if cor2[1] != 5:
            can.move("group1", 0, -1)
    can.move(tamagochy, vec_x, vec_y)
    root.after(10, go)

can = Canvas(root)
can.pack()
 
ball = can.create_oval(140, 140, 160, 160, 
                     fill='green', tag="group1")
tamagochy = can.create_rectangle(5, 5, 25, 25, tag="group1")
go()
root.bind('<ButtonPress>', event_info1)
root.bind('<ButtonRelease>', event_info2)
can.bind('<Motion>', test)
root.mainloop()
