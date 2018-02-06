from tkinter import *
import random

from tkinter import messagebox
root = Tk()
for row_index in range(4):
    Grid.rowconfigure(root, row_index, weight=1)
    for col_index in range(4):
        Grid.columnconfigure(root, col_index, weight=1)

    
def s1():
    if btn2['text'] == "*":
        temp=btn2['text']
        btn2['text']=btn1['text']
        btn1['text']=temp

    if btn4['text'] == "*":
        temp=btn4['text']
        btn4['text']=btn1['text']
        btn1['text']=temp

    checkwin() 
def s2():
    if btn1['text'] == "*":
        temp=btn1['text']
        btn1['text']=btn2['text']
        btn2['text']=temp
    if btn5['text'] == "*":
        temp=btn5['text']
        btn5['text']=btn2['text']
        btn2['text']=temp
    if btn3['text'] == "*":
        temp=btn3['text']
        btn3['text']=btn2['text']
        btn2['text']=temp
    checkwin()   
     
def s3():
    if btn2['text'] == "*":
        temp=btn2['text']
        btn2['text']=btn3['text']
        btn3['text']=temp
    if btn6['text'] == "*":
        temp=btn6['text']
        btn6['text']=btn3['text']
        btn3['text']=temp
    checkwin()
def s4():
    if btn1['text'] == "*":
        temp=btn1['text']
        btn1['text']=btn4['text']
        btn4['text']=temp
    if btn5['text'] == "*":
        temp=btn5['text']
        btn5['text']=btn4['text']
        btn4['text']=temp
    if btn7['text'] == "*":
        temp=btn7['text']
        btn7['text']=btn4['text']
        btn4['text']=temp
    checkwin()
def s5():
   if btn2['text'] == "*":
       temp=btn2['text']
       btn2['text']=btn5['text']
       btn5['text']=temp
   if btn4['text'] == "*":
       temp=btn4['text']
       btn4['text']=btn5['text']
       btn5['text']=temp
   if btn6['text'] == "*":
       temp=btn6['text']
       btn6['text']=btn5['text']
       btn5['text']=temp
   if btn8['text'] == "*":
       temp=btn8['text']
       btn8['text']=btn3['text']
       btn3['text']=temp
   checkwin()
def s6():
   if btn5['text'] == "*":
       temp=btn5['text']
       btn5['text']=btn6['text']
       btn6['text']=temp
   if btn3['text'] == "*":
       temp=btn3['text']
       btn3['text']=btn6['text']
       btn6['text']=temp
   if btn9['text'] == "*":
       temp=btn9['text']
       btn9['text']=btn6['text']
       btn6['text']=temp
   checkwin()  
   
def s7():
   if btn4['text'] == "*":
       temp=btn4['text']
       btn4['text']=btn7['text']
       btn7['text']=temp
        
   if btn8['text'] == "*":
       temp=btn8['text']
       btn8['text']=btn7['text']
       btn7['text']=temp
   checkwin()
  
def s8():
   if btn5['text'] == "*":
       temp=btn5['text']
       btn5['text']=btn8['text']
       btn8['text']=temp
   if btn7['text'] == "*":
       temp=btn7['text']
       btn7['text']=btn8['text']
       btn8['text']=temp
   if btn9['text'] == "*":
       temp=btn9['text']
       btn9['text']=btn8['text']
       btn8['text']=temp
   checkwin()

def s9():
   if btn8['text'] == "*":
       temp=btn8['text']
       btn8['text']=btn9['text']
       btn9['text']=temp
   if btn6['text'] == "*":
       temp=btn6['text']
       btn6['text']=btn9['text']
       btn9['text']=temp
   checkwin()

def p1():
    btn1.configure(text="1")
    btn2.configure(text="2")
    btn3.configure(text="3")
    btn4.configure(text="4")
    btn5.configure(text="*")
    btn6.configure(text="5")
    btn7.configure(text="7")
    btn8.configure(text="8")
    btn9.configure(text="6")
def p2():
    btn1.configure(text="2")
    btn2.configure(text="3")
    btn3.configure(text="1")
    btn4.configure(text="4")
    btn5.configure(text="8")
    btn6.configure(text="7")
    btn7.configure(text="6")
    btn8.configure(text="5")
    btn9.configure(text="*")

btn1 = Button(root,command=s1)
btn1.grid(column=0, row=0, sticky=N+S+E+W)
btn2 = Button(root,command=s2)
btn2.grid(column=1, row=0, sticky=N+S+E+W)
btn3 = Button(root,command=s3)
btn3.grid(column=2, row=0, sticky=N+S+E+W)
btn4 = Button(root,command=s4)
btn4.grid(column=0, row=1, sticky=N+S+E+W)
btn5 = Button(root,command=s5)
btn5.grid(column=1, row=1, sticky=N+S+E+W)
btn6 = Button(root,command=s6)
btn6.grid(column=2, row=1, sticky=N+S+E+W)
btn7 = Button(root,command=s7)
btn7.grid(column=0, row=2, sticky=N+S+E+W)
btn8 = Button(root,command=s8)
btn8.grid(column=1, row=2, sticky=N+S+E+W)
btn9 = Button(root,command=s9)
btn9.grid(column=2, row=2, sticky=N+S+E+W)
btn10 = Button(root,command=random,text="start")
btn1.configure(text=random.choice([p1,p2])())

def checkwin():
    if  btn1['text']=="1" and btn2['text']=="2" and btn3['text']=="3" and btn4['text']=="4" and btn5['text']=="5" and btn6['text']=="6" and btn7['text']=="7" and btn8['text']=="8":
        messagebox.showinfo(" you won the  game")
        btn1.configure(text=random.choice([p1,p2])())
        
