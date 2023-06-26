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

  
