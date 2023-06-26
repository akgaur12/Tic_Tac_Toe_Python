from tkinter import *
from tkinter import messagebox

click = 0
p1_wins = 0
p2_wins = 0


def result():
    global b1, b2, b3, b4, b5, b6, b7, b8, click, en1, en2, p1_wins, p2_wins, lb1, lb2
    p1 = en1.get()
    p2 = en2.get()

    if (b1['text']=='0' and b2['text']=='0' and b3['text']=='0'):
        messagebox.showinfo('Result', p1+' Won the Game')
        p1_wins += 1
        lb1.config(text=(en1.get()+" "+str(p1_wins)))
        clear()
    elif (b1['text']=='X' and b2['text']=='X' and b3['text']=='X'):
        messagebox.showinfo('Result', p2+' Won the Game')
        p2_wins += 1
        lb2.config(text=(en2.get()+" "+str(p2_wins)))
        clear()
    elif (b4['text']=='0' and b5['text']=='0' and b6['text']=='0'):
        messagebox.showinfo('Result', p1+' Won the Game')
        p1_wins += 1
        lb1.config(text=(en1.get()+" "+str(p1_wins)))
        clear()
    elif (b4['text']=='X' and b5['text']=='X' and b6['text']=='X'):
        messagebox.showinfo('Result', p2+' Won the Game')
        p2_wins += 1
        lb2.config(text=(en2.get()+" "+str(p2_wins)))
        clear()
    elif (b7['text']=='0' and b8['text']=='0' and b9['text']=='0'):
        messagebox.showinfo('Result', p1+' Won the Game')
        p1_wins += 1
        lb1.config(text=(en1.get()+" "+str(p1_wins)))
        clear()
    elif (b7['text']=='X' and b8['text']=='X' and b9['text']=='X'):
        messagebox.showinfo('Result', p2+' Won the Game')
        p2_wins += 1
        lb2.config(text=(en2.get()+" "+str(p2_wins)))
        clear()
    elif (b1['text']=='0' and b4['text']=='0' and b7['text']=='0'):
        messagebox.showinfo('Result', p1+' Won the Game')
        p1_wins += 1
        lb1.config(text=(en1.get()+" "+str(p1_wins)))
        clear()
    elif (b1['text']=='X' and b4['text']=='X' and b7['text']=='X'):
        messagebox.showinfo('Result', p2+' Won the Game')
        p2_wins += 1
        lb2.config(text=(en2.get()+" "+str(p2_wins)))
        clear()
    elif (b2['text']=='0' and b5['text']=='0' and b8['text']=='0'):
        messagebox.showinfo('Result', p1+' Won the Game')
        p1_wins += 1
        lb1.config(text=(en1.get()+" "+str(p1_wins)))
        clear()
    elif (b2['text']=='X' and b5['text']=='X' and b8['text']=='X'):
        messagebox.showinfo('Result', p2+' Won the Game')
        p2_wins += 1
        lb2.config(text=(en2.get()+" "+str(p2_wins)))
        clear()
    elif (b3['text']=='0' and b6['text']=='0' and b9['text']=='0'):
        messagebox.showinfo('Result', p1+' Won the Game')
        p1_wins += 1
        lb1.config(text=(en1.get()+" "+str(p1_wins)))
        clear()
    elif (b3['text']=='X' and b6['text']=='X' and b9['text']=='X'):
        messagebox.showinfo('Result', p2+' Won the Game')
        p2_wins += 1
        lb2.config(text=(en2.get()+" "+str(p2_wins)))
        clear()
    if (b1['text']=='0' and b5['text']=='0' and b9['text']=='0'):
        messagebox.showinfo('Result', p1+' Won the Game')
        p1_wins += 1
        lb1.config(text=(en1.get()+" "+str(p1_wins)))
        clear()
    elif (b1['text']=='X' and b5['text']=='X' and b9['text']=='X'):
        messagebox.showinfo('Result', p2+' Won the Game')
        p2_wins += 1
        lb2.config(text=(en2.get()+" "+str(p2_wins)))
        clear()
    elif (b3['text']=='0' and b5['text']=='0' and b7['text']=='0'):
        messagebox.showinfo('Result', p1+' Won the Game')
        p1_wins += 1
        lb1.config(text=(en1.get()+" "+str(p1_wins)))
        clear()
    elif (b3['text']=='X' and b5['text']=='X' and b7['text']=='X'):
        messagebox.showinfo('Result', p2+' Won the Game')
        p2_wins += 1
        lb2.config(text=(en2.get()+" "+str(p2_wins)))
        clear()
    elif click == 9:
        messagebox.showinfo('Result', 'Match Draw')
        clear()


def show(b):
    global click
    if click%2 == 0:
        if b['text'] == '':
            b.config(text='0', fg='brown')
            click += 1
    else:
        if b['text'] == '':
            b.config(text='X', fg='blue')
            click += 1
    result()


def clear():
    global b1, b2, b3, b4, b5, b6, b7, b8, click
    b1.config(text='')
    b2.config(text='')
    b3.config(text='')
    b4.config(text='')
    b5.config(text='')
    b6.config(text='')
    b7.config(text='')
    b8.config(text='')
    b9.config(text='')
    click = 0


def button(wn, x, y):
    btn = Button(
        wn, text='', 
        font=('Comic sans ms', 34,'bold'), 
        height=2, 
        width=6, 
        bg='light green',
        activebackground='light green',
        relief='sunken', 
        command=lambda:show(btn)
    )
    btn.place(x=x, y=y)
    return btn


def game():
    global wins, lb1, lb2
    f2 = Frame(root, bg='#7688ee')
    f2.place(x=0, y=0, height=564, width=516)

    img = PhotoImage(file="back.png")
    btn_back = Button(f2, image=img, command=home, bg='#7688ee', bd=0, )
    btn_back.image_names = img
    btn_back.place(x=2, y=8)

    lb1 = Label(f2, text=(en1.get()+" "+str(p1_wins)), font=('Bahnschrift', 14), bg='#7688ee', fg='white')
    lb1.place(x=110, y=5)
    lb2 = Label(f2, text=(en2.get()+" "+str(p2_wins)), font=('Bahnschrift', 14), bg='#7688ee', fg='white')
    lb2.place(x=320, y=5)

    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    b1 = button(f2,0,45)
    b2 = button(f2,172,45)
    b3 = button(f2,344,45)
    b4 = button(f2,0,218)
    b5 = button(f2,172,218)
    b6 = button(f2,344,218)
    b7 = button(f2,0,391)
    b8 = button(f2,172,391)
    b9 = button(f2,344,391)


root = Tk()
root.title('Tic-Tac-Toe')
root.geometry('516x564+500+80')
root.resizable(0,0)
icon = PhotoImage(file='img1.png')
root.iconphoto(False, icon)

p1_name = StringVar()
p2_name = StringVar()

  
