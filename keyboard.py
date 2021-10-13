import tkinter
import sys
import time
import random

indata = 0000
randomdata = "0000"
txtdata = "hoge"


mainfrm = tkinter.Tk()
mainfrm.geometry("980x700")             
mainfrm.title("タイピング練習")
txtbox = tkinter.Entry(width=70)
txtbox.place(x=200,y=400) 
indata = txtbox.get
#def atosyori():

def kotae():
    print(randomdata)
    if  randomdata.strip() == indata :
        lbl3 = tkinter.Label(text="正解")
        lbl3.place(x=490,y=300)

    else:
        lbl4 = tkinter.Label(text="不正解")
        lbl4.place(x=490,y=300)
def monndai():
    global randomdata
    with open("kotae.txt") as f:
        indata = f.readlines()
    x = random.choice(indata)
    lbl = tkinter.Label(text=x)
    lbl.place(x=490,y=200)
    randomdata = x

def awase():
    kotae()


#btnclick1はウィンドウを消すボタンです
btnclick1 = tkinter.Button(mainfrm, text="終わり",bg="#d2b48c",command=mainfrm.destroy)
btnclick1.place(x=900,y=660)
btnclick2 = tkinter.Button(mainfrm,text="問題",command=monndai)
btnclick2.place(x=740,y=660)
btnclick3 = tkinter.Button(mainfrm,text="答え合わせ",command=awase)
btnclick3.place(x=800,y=660)
mainfrm.mainloop()

print("the end")