#!/usr/bin/python
import tkinter as tk
from tkinter import StringVar,ttk,Canvas
from PIL import ImageTk, Image
import random

#重新建立答案
def newGame():
    global ansList
    global strv
    global Time
    global labelText
    ansList = []
    while len(ansList) < 4:
        rr = random.randrange(0, 10)
        if (rr not in ansList):
            ansList.append(rr)

    Time=1
    #btn1.pack()
    btn1.place(x=205, y=220)
    entry1.place(x=150,y=260)
    labelText="密碼對應結果"
    strv.set(labelText)
    label2.place(x=220,y=300,anchor='n')
    StartBtn.place_forget()
    canvas.delete('label')


#遊戲結束
def gameOver():
    btn1.place_forget()
    entry1.place_forget()
    StartBtn.place(x=startBtnxy[0],y=startBtnxy[1])


#check
def check(passWord):
    passWord=str(passWord)
    A=0
    B=0
    iCount=0
    while iCount<len(ansList):
        iFind=passWord.find(str(ansList[iCount]))
        if(iFind==iCount):
            A=A+1
        elif(iFind>=0):
            B=B+1
        iCount=iCount+1

    if(A==4):
        gameOver()
        return "恭喜獲勝"

    Ans=(str(A)+"A,"+str(B)+"B")
    return Ans


def enter():
    password=entry1.get()
    #測數字
    try:
        int(password)
    except:
        return "輸入錯誤!"

    #測長度
    password=str(password)
    if(len(password)==4):
        #驗證答案
        return  check(password)
    else:
        return "輸入錯誤!"

def btnEvent():
    global Time
    global  strv
    global labelText
    if Time<=10:
        labelText=labelText+"\n第"+str(Time)+"次: "+entry1.get()+" "+str(enter())
        strv.set(labelText)
        Time=Time+1
    elif Time>10:
        labelText = labelText + "\n遊戲失敗!"
        strv.set(labelText)
        gameOver()


win=tk.Tk()


#座標
startBtnxy=[145,550]

ansList=[]
Time=1
labelText=""
strv=StringVar()

##視窗大小設定
win.minsize(width=438,height=710)
win.resizable(False,False)

#背景畫布
canvas=Canvas(win,width=440,height=710)
canvas.place(x=-2,y=0)

bgImg = ImageTk.PhotoImage(Image.open("numbg.jpg"))
canvas.create_image(220,355,image=bgImg)

titleImg=ImageTk.PhotoImage(Image.open("numTitle2.png"))
canvas.create_image(220,80,image=titleImg)

label1Img = ImageTk.PhotoImage(Image.open("numlabel1.png"))
canvas.create_image(420,350,image=label1Img,tag='label')

label2 = tk.Label(win, textvariable=strv)

#textbox
entry1=tk.Entry(win,text="90")

#確認btn
btn1=tk.Button(win,text="確認",command=btnEvent)


startImg = ImageTk.PhotoImage(Image.open("st-1.png"))
StartBtn=tk.Button(win,text="開始遊戲",image=startImg,command=newGame)
StartBtn.place(x=startBtnxy[0],y=startBtnxy[1])



"""
#需求圖片
textImg = ImageTk.PhotoImage(Image.open("TextImage.png"))
label1Img = ImageTk.PhotoImage(Image.open("label1.png"))
btnImg = ImageTk.PhotoImage(Image.open("button.png"))

#背景圖案
bgLabel=tk.Label(win,image=bgImg)
bgLabel.place(x=-5,y=-5)

#標題字
textLabel=tk.Label(win,image=textImg)
textLabel.place(x=30,y=20)

#輸入台幣
label1=tk.Label(win,image=label1Img)
label1.place(x=60,y=150)


#btn
btn1=tk.Button(win,image=btnImg,command=change)
btn1.place(x=250,y=220)

#顯示轉換後的數值label
v=StringVar()

label1=tk.Label(win,textvariable=v)
label1.place(x=400,y=230)


#下拉式選單
cbList=["abc","bbc","ccc"]
comboBox1=ttk.Combobox(win,values=cbList)
comboBox1.place(x=400,y=155)
"""

win.mainloop()