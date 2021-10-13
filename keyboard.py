import tkinter
import sys
import time
import random

#ver 0.1

indata = 0000
randata = "0000"
txtdata = "hoge"


mainfrm = tkinter.Tk()
mainfrm.geometry("980x700")             
mainfrm.title("タイピング練習")
txtbox = tkinter.Entry(width=70)
txtbox.place(x=200,y=400) 
indata = txtbox.get()
txtbox1 = tkinter.Entry(width=40)
txtbox1.place(x=270,y=300)

def kotae():
    indata = txtbox1.get()
    if  randata.strip() == indata :
        lbl3 = tkinter.Label(text=" 正解 ")
        lbl3.place(x=490,y=300)
        txtbox1.delete(0, tkinter.END)
        txtbox.delete(0, tkinter.END)


    else:
        lbl4 = tkinter.Label(text="不正解")
        lbl4.place(x=490,y=300)
        txtbox1.delete(0, tkinter.END)
        txtbox.delete(0, tkinter.END)
def monndai():
    global randata
    with open("kotae.txt") as f:
        indata = f.readlines()
    randata = random.choice(indata)
    txtbox1.insert(tkinter.END,randata)

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