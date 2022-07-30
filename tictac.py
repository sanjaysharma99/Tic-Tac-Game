from tkinter import *
from tkinter import messagebox
import time 

app=Tk()
app.title('Tic Tac By Sanjay Sharma')
app.geometry('300x350')
app.minsize(300,350)
app.maxsize(350,300)

listv=['x','o']
laststate=True
btn1v=' '
btn2v=' '
btn3v=' '
btn4v=' '
btn5v=' '
btn6v=' '
btn7v=' '
btn8v=' '
btn9v=' '




def win():
    #this section for x winner
    if btn1v==True and btn5v==True and btn9v==True:
        messagebox.showinfo('Winner','X Player is Winner')
        reset()

    if btn3v==True and btn5v==True and btn7v==True:
        messagebox.showinfo('Winner','X Player is Winner')
        reset()
        
    if btn1v==True and btn4v==True and btn7v==True:
        messagebox.showinfo('Winner','X Player is Winner')
        reset()

    if btn2v==True and btn5v==True and btn8v==True:
        messagebox.showinfo('Winner','X Player is Winner')
        reset()

    if btn3v==True and btn6v==True and btn9v==True:
        messagebox.showinfo('Winner','X Player is Winner')
        reset()

    if btn1v==True and btn2v==True and btn3v==True:
        messagebox.showinfo('Winner','X Player is Winner')
        reset()

    if btn4v==True and btn5v==True and btn6v==True:
        messagebox.showinfo('Winner','X Player is Winner')
        reset()

    if btn7v==True and btn8v==True and btn9v==True:
        messagebox.showinfo('Winner','X Player is Winner')
        reset()
    
    #this section for o winner
    if btn1v==False and btn5v==False and btn9v==False:
        messagebox.showinfo('Winner','O Player is Winner')
        reset()

    if btn3v==False and btn5v==False and btn7v==False:
        messagebox.showinfo('Winner','O Player is Winner')
        reset()
        
    if btn1v==False and btn4v==False and btn7v==False:
        messagebox.showinfo('Winner','O Player is Winner')
        reset()

    if btn2v==False and btn5v==False and btn8v==False:
        messagebox.showinfo('Winner','O Player is Winner')
        reset()

    if btn3v==False and btn6v==False and btn9v==False:
        messagebox.showinfo('Winner','O Player is Winner')
        reset()

    if btn1v==False and btn2v==False and btn3v==False:
        messagebox.showinfo('Winner','O Player is Winner')
        reset()

    if btn4v==False and btn5v==False and btn6v==False:
        messagebox.showinfo('Winner','O Player is Winner')
        reset()

    if btn7v==False and btn8v==False and btn9v==False:
        messagebox.showinfo('Winner','O Player is Winner')
        reset()
    
def fun1():
    global laststate
    global btn1v
    if laststate:
        btn1.config(text=listv[0])
        btn1v=True
        laststate=False
    else:
        btn1.config(text=listv[1])
        btn1v=False
        laststate=True
    print(type(btn1v))
    win()

def fun2():
    global laststate
    global btn2v
    if laststate:
        btn2.config(text=listv[0])
        btn2v=True
        laststate=False
    else:
        btn2.config(text=listv[1])
        btn2v=False
        laststate=True
    win()
    
def fun3():
    global laststate
    global btn3v
    if laststate:
        btn3.config(text=listv[0])
        btn3v=True
        laststate=False
    else:
        btn3.config(text=listv[1])
        btn3v=False
        laststate=True
    win()

def fun4():
    global laststate
    global btn4v
    if laststate:
        btn4.config(text=listv[0])
        btn4v=True
        laststate=False
    else:
        btn4.config(text=listv[1])
        btn4v=False
        laststate=True
    win()

def fun5():
    global laststate
    global btn5v
    if laststate:
        btn5.config(text=listv[0])
        btn5v=True
        laststate=False
    else:
        btn5.config(text=listv[1])
        btn5v=False
        laststate=True
    win()

def fun6():
    global laststate
    global btn6v
    if laststate:
        btn6.config(text=listv[0])
        btn6v=True
        laststate=False
    else:
        btn6.config(text=listv[1])
        btn6v=False
        laststate=True
    win()

def fun7():
    global laststate
    global btn7v
    if laststate:
        btn7.config(text=listv[0])
        btn7v=True
        laststate=False
    else:
        btn7.config(text=listv[1])
        btn7v=False
        laststate=True
    win()

def fun8():
    global laststate
    global btn8v
    if laststate:
        btn8.config(text=listv[0])
        btn8v=True
        laststate=False
    else:
        btn8.config(text=listv[1])
        btn8v=False
        laststate=True
    win()

def fun9():
    global laststate
    global btn9v
    if laststate:
        btn9.config(text=listv[0])
        btn9v=True
        laststate=False
    else:
        btn9.config(text=listv[1])
        btn9v=False
        laststate=True
    win()

def reset():
    global btn1v
    global btn2v
    global btn3v
    global btn4v
    global btn5v
    global btn6v
    global btn7v
    global btn8v
    global btn9v

    btn1.config(text=' ')
    btn2.config(text=' ')
    btn3.config(text=' ')
    btn4.config(text=' ')
    btn5.config(text=' ')
    btn6.config(text=' ')
    btn7.config(text=' ')
    btn8.config(text=' ')
    btn9.config(text=' ')
    
    btn1v=' '
    btn2v=' '
    btn3v=' '
    btn4v=' '
    btn5v=' '
    btn6v=' '
    btn7v=' '
    btn8v=' '
    btn9v=' '

btn1=Button(app,text=' ',command=fun1,height=1,width=3,font='italic 36 bold',fg='blue',activeforeground='blue')
btn2=Button(app,text=' ',command=fun2,height=1,width=3,font='italic 36 bold',fg='blue',activeforeground='blue')
btn3=Button(app,text=' ',command=fun3,height=1,width=3,font='italic 36 bold',fg='blue',activeforeground='blue')
btn4=Button(app,text=' ',command=fun4,height=1,width=3,font='italic 36 bold',fg='blue',activeforeground='blue')
btn5=Button(app,text=' ',command=fun5,height=1,width=3,font='italic 36 bold',fg='blue',activeforeground='blue')
btn6=Button(app,text=' ',command=fun6,height=1,width=3,font='italic 36 bold',fg='blue',activeforeground='blue')
btn7=Button(app,text=' ',command=fun7,height=1,width=3,font='italic 36 bold',fg='blue',activeforeground='blue')
btn8=Button(app,text=' ',command=fun8,height=1,width=3,font='italic 36 bold',fg='blue',activeforeground='blue')
btn9=Button(app,text=' ',command=fun9,height=1,width=3,font='italic 36 bold',fg='blue',activeforeground='blue')
btn=Button(app,text='Reset',command=reset,font='italic 16 bold',bg='lightgreen',activebackground='lightgreen',fg='blue',activeforeground='blue')

btn1.grid(row=1,column=1)
btn2.grid(row=1,column=2)
btn3.grid(row=1,column=3)
btn4.grid(row=2,column=1)
btn5.grid(row=2,column=2)
btn6.grid(row=2,column=3)
btn7.grid(row=3,column=1)
btn8.grid(row=3,column=2)
btn9.grid(row=3,column=3)
btn.grid(row=4,column=2,pady=10)

app.mainloop()