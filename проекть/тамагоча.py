from tkinter import *
import time
from PIL import Image, ImageTk
from threading import *
from tkinter import messagebox as mb
import sqlite3

def start():
    global satiety, hp, weight, toilet, mood, old, db, sql
    db = sqlite3.connect('sqlite_python.db')
    sql = db.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS бумбельшмек(
        satiety INT,
        hp INT,
        weight INT,
        toilet INT,
        mood INT,
        old INT,
        night INT,
        peredoz INT
    )""")
    s = sql.execute("SELECT * FROM бумбельшмек").fetchall()
    print(s)

    satiety = s[0][0]
    hp = s[0][1]
    weight = s[0][2]
    toilet = s[0][3]
    mood = s[0][4]
    old = s[0][5]
    night = s[0][6]
    peredoz = s[0][7]

    print(satiety, hp, weight, toilet, mood, old, night, peredoz)
start()
def timer():
    global satiety, toilet, hp, weight
    while hp > 0:
        time.sleep(10)
        satiety -= 5
        weight -= 5
        toilet += 5
        if satiety < 20 or weight < 20:
            hp -= 20
            mb.showwarning(
            "я истащён", 
            "hp упало на 20, я щас сдохну дебил")
        elif satiety < 30 or weight < 30:
            hp -= 15
            mb.showwarning(
            "я истащён", 
            "hp упало на 15, в магилу меня свести хочешь?")
        elif satiety < 40 or weight < 40:
            hp -= 10
            mb.showwarning(
            "я истащён", 
            "hp упало на 10, это уже больно так то")
        elif satiety < 50 or weight < 50:
            hp -= 5
            mb.showwarning(
            "я истащён", 
            "hp упало на 5")
        if toilet > 100:
            hp -= 20
            mb.showwarning(
            "я утопаю в горах говна", 
            "hp упало на 20, я щас сдохну дебил")
        elif toilet > 90:
            hp -= 15
            mb.showwarning(
            "я утопаю в горах говна", 
            "hp упало на 15, в магилу меня свести хочешь?")
        elif toilet > 80:
            hp -= 10
            mb.showwarning(
            "я утопаю в горах говна", 
            "hp упало на 10, это уже больно так то")
        elif toilet > 70:
            hp -= 5
            mb.showwarning(
            "я утопаю в горах говна", 
            "hp упало на 5")
    if hp <= 0:
         s = mb.askyesno(
         title="ты сдох дебил", 
         message="возродиться?")
         if s == True:
                start()
                t = Thread(target = timer)
                t.start()
         elif s == False:
             root.destroy()

def eat():
    global bat9, bat10
    try:
        bat9.destroy()
        bat10.destroy()
    except:
        None
    bat9 = Button(text="тортик", bg = 'indigo', fg = "#ffffff",
           command = cake)
    bat10 = Button(text="супчик", bg = 'green', fg = "#ffffff",
           command = soup)
    bat9.place(anchor=NW, relx=0.3, rely=0.2,
               relwidth=0.4, relheight=0.15)
    bat10.place(anchor=NW, relx=0.3, rely=0.65,
                relwidth=0.4, relheight=0.15)
    
def soup():
    global satiety, weight, bat9, bat10, hp
    satiety += 10
    weight += 5
    bat9.destroy()
    bat10.destroy()
    if weight > 150:
        hp -= 20
        mb.showwarning(
        "пипец я жирный", 
        "hp упало на 20, я щас сдохну дебил")
    elif weight > 140:
        hp -= 15
        mb.showwarning(
        "пипец я жирный", 
        "hp упало на 15, в магилу меня свести хочешь?")
    elif weight > 130:
        hp -= 10
        mb.showwarning(
        "пипец я жирный", 
        "hp упало на 10, это уже больно так то")
    elif weight > 120:
        hp -= 5
        mb.showwarning(
        "пипец я жирный", 
        "hp упало на 5")
    if hp <= 0:
         s = mb.askyesno(
         title="ты сдох дебил", 
         message="возродиться?")
         if s == True:
                start()
                t = Thread(target = timer)
                t.start()
         elif s == False:
             root.destroy()
            
    print(satiety, weight)
def cake():
    global satiety, weight, bat9, bat10, hp
    satiety += 20
    weight += 20
    bat9.destroy()
    bat10.destroy()
    if weight > 150:
        hp -= 20
        mb.showwarning(
        "пипец я жирный", 
        "hp упало на 20, я щас сдохну дебил")
    elif weight > 140:
        hp -= 15
        mb.showwarning(
        "пипец я жирный", 
        "hp упало на 15, в магилу меня свести хочешь?")
    elif weight > 130:
        hp -= 10
        mb.showwarning(
        "пипец я жирный", 
        "hp упало на 10, это уже больно так то")
    elif weight > 120:
        hp -= 5
        mb.showwarning(
        "пипец я жирный",
        
        "hp упало на 5")
    if hp <= 0:
         s = mb.askyesno(
         title="ты сдох дебил", 
         message="возродиться?")
         if s == True:
                start()
                t = Thread(target = timer)
                t.start()
         elif s == False:
             root.destroy()

def toilet1():
    try:
        a.destroy()
    except:
        None
    def smuv():
        global toilet
        toilet = 0
        a.destroy()
    a = Toplevel()
    a.geometry('300x250')
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    w = w//4 
    h = h//4 
    w = w - 150 
    h = h - 150
    a.geometry('300x250+{}+{}'.format(w, h))
    if night % 2 == 0:
        a['bg'] = 'black'
    elif night % 2 != 0:
        a['bg'] = 'white'
    Button(a, image = png9_im, command = smuv)\
        .pack(expand=1)

def stata1():
    global arr
    try:
        arr.destroy()
    except:
        None
    def smuv():
        arr.destroy()
    arr = Toplevel()
    arr.geometry('100x150')
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    w = w - w//4 
    h = h//4 
    w = w - 200 
    h = h - 100
    arr.geometry('200x200+{}+{}'.format(w, h))
    def obnov():
        global lab1, lab2, lab3, lab4, lab5, lab6, lab7, bat12
        time.sleep(1)
        try:
            lab1.destroy()
            lab2.destroy()
            lab3.destroy()
            lab4.destroy()
            lab5.destroy()
            lab6.destroy()
            lab7.destroy()
            bat12.destroy()
        except:
            None
        lab1 = Label(arr, text = "сытость = " + str(satiety))
        lab2 = Label(arr, text = "hp = " + str(hp))
        lab3 = Label(arr, text = "вес = " + str(weight))
        lab4 = Label(arr, text = "сартир = " + str(toilet))
        lab5 = Label(arr, text = "настроение = " + str(mood))
        lab6 = Label(arr, text = "возраст = " + str(old))
        lab7 = Label(arr, text = "передоз = " + str(peredoz))
        bat12 = Button(arr, text = "закрыть", command = smuv)
        lab1.pack(expand=1)
        lab2.pack(expand=1)
        lab3.pack(expand=1)
        lab4.pack(expand=1)
        lab5.pack(expand=1)
        lab6.pack(expand=1)
        lab7.pack(expand=1)
        bat12.pack(expand=1)
        arr.after(1000, obnov)
        if night % 2 == 0:
            arr['bg'] = 'black'
            lab1['bg'] = 'black'
            lab2['bg'] = 'black'
            lab3['bg'] = 'black'
            lab4['bg'] = 'black'
            lab5['bg'] = 'black'
            lab6['bg'] = 'black'
            lab7['bg'] = 'black'
            bat12['bg'] = 'black'
            lab1['fg'] = 'white'
            lab2['fg'] = 'white'
            lab3['fg'] = 'white'
            lab4['fg'] = 'white'
            lab5['fg'] = 'white'
            lab6['fg'] = 'white'
            lab7['fg'] = 'white'
            bat12['fg'] = 'white'
        elif night % 2 != 0:
            arr['bg'] = 'white'
            lab1['bg'] = 'white'
            lab2['bg'] = 'white'
            lab3['bg'] = 'white'
            lab4['bg'] = 'white'
            lab5['bg'] = 'white'
            lab6['bg'] = 'white'
            lab7['bg'] = 'white'
            bat12['bg'] = 'white'
            lab1['fg'] = 'black'
            lab2['fg'] = 'black'
            lab3['fg'] = 'black'
            lab4['fg'] = 'black'
            lab5['fg'] = 'black'
            lab6['fg'] = 'black'
            lab7['fg'] = 'black'
            bat12['fg'] = 'black'
    obnov()
    #arr.after(10000, lambda: arr.destroy())

def svet():
    global night
    night += 1
    if night % 2 == 0:
        root['bg'] = 'black'
        bat1['bg'] = 'black'
        bat2['bg'] = 'black'
        bat3['bg'] = 'black'
        bat4['bg'] = 'black'
        bat5['bg'] = 'black'
        bat6['bg'] = 'black'
        bat7['bg'] = 'black'
        bat8['bg'] = 'black'
    elif night % 2 != 0:
        root['bg'] = 'white'
        bat1['bg'] = 'white'
        bat2['bg'] = 'white'
        bat3['bg'] = 'white'
        bat4['bg'] = 'white'
        bat5['bg'] = 'white'
        bat6['bg'] = 'white'
        bat7['bg'] = 'white'
        bat8['bg'] = 'white'
    print(night)

def durka():
    global bat13, bat14, hp, weihgt, toilet, peredoz
    def mezim():
        global weight, hp, peredoz
        if weight > 100:
            weight -= 10 
        hp += 20
        peredoz += 1 
        bat14.destroy()
        bat13.destroy()
        
    def ugol():
        global toilet, hp, peredoz
        if toilet > 20: 
            toilet -= 5
        hp += 20
        peredoz += 1 
        bat14.destroy()
        bat13.destroy()

    try:
        bat13.destroy()
        bat14.destroy()
    except:
        None
    bat13 = Button(text="уголь \n активированный", bg = 'black', fg = "white",
           command=ugol)
    bat14 = Button(text="мезим", bg = 'pink', fg = "black",
           command=mezim)
    bat13.place(anchor=NW, relx=0.3, rely=0.2,
               relwidth=0.4, relheight=0.15)
    bat14.place(anchor=NW, relx=0.3, rely=0.65,
                relwidth=0.4, relheight=0.15)

    if peredoz > 100:
        hp -= 300000000000000000000
        mb.showwarning(
        "передоз", 
        "hp упало на 20, я щас сдохну дебил")
    elif peredoz > 20:
        hp -= 15
        mb.showwarning(
        "передоз", 
        "hp упало на 15, в магилу меня свести хочешь?")
    elif peredoz > 15:
        hp -= 10
        mb.showwarning(
        "передоз", 
        "hp упало на 10, это уже больно так то")
    elif peredoz > 10:
        hp -= 5
        mb.showwarning(
        "передоз", 
        "hp упало на 5")
    if hp <= 0:
         s = mb.askyesno(
         title="ты сдох дебил", 
         message="возродиться?")
         if s == True:
                start()
                t = Thread(target = timer)
                t.start()
         elif s == False:
             root.destroy()

def stata():
    t1 = Thread(target = stata1)
    t1.start()

t = Thread(target = timer)
t.start()


root = Tk()

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w//2 
h = h//2 
w = w - 150 
h = h - 150
root.geometry('300x300+{}+{}'.format(w, h))

png1 = Image.open("1.png")
png2 = Image.open("2.png")
png3 = Image.open("3.png")
png4 = Image.open("4.png")
png5 = Image.open("5.png")
png6 = Image.open("6.png")
png7 = Image.open("7.png")
png8 = Image.open("8.png")
png9 = Image.open("toilet.png")
png1_im = ImageTk.PhotoImage(png1)
png2_im = ImageTk.PhotoImage(png2)
png3_im = ImageTk.PhotoImage(png3)
png4_im = ImageTk.PhotoImage(png4)
png5_im = ImageTk.PhotoImage(png5)
png6_im = ImageTk.PhotoImage(png6)
png7_im = ImageTk.PhotoImage(png7)
png8_im = ImageTk.PhotoImage(png8)
png9_im = ImageTk.PhotoImage(png9)
img = PhotoImage(file='test.gif')
bat1 = Button(image = png1_im, command=eat)
bat2 = Button(image = png2_im, command=svet)
bat3 = Button(image = png3_im)
bat4 = Button(image = png4_im, command=durka)
bat5 = Button(image = png5_im, command=toilet1)
bat6 = Button(image = png6_im, command=stata)
bat7 = Button(image = png7_im)
bat8 = Button(image = png8_im)
lab = Label(image = img)


bat1.place(anchor=NW, relx=0.1, rely=0,
           relwidth=0.2, relheight=0.2)
bat2.place(anchor=NW, relx=0.3, rely=0,
           relwidth=0.2, relheight=0.2)
bat3.place(anchor=NW, relx=0.5, rely=0,
           relwidth=0.2, relheight=0.2)
bat4.place(anchor=NW, relx=0.7, rely=0,
           relwidth=0.2, relheight=0.2)
lab.place(anchor=CENTER, relx=0.5, rely=0.5)
bat5.place(anchor=SW, relx=0.1, rely=1,
           relwidth=0.2, relheight=0.2)
bat6.place(anchor=SW, relx=0.3, rely=1,
           relwidth=0.2, relheight=0.2)
bat7.place(anchor=SW, relx=0.5, rely=1,
           relwidth=0.2, relheight=0.2)
bat8.place(anchor=SW, relx=0.7, rely=1,
           relwidth=0.2, relheight=0.2)
root.mainloop()
