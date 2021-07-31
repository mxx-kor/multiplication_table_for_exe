from tkinter import * 
import tkinter as tk


win = Tk()
win.title("구구단")
win.geometry("500x700")
win.option_add("*Font","고딕 10")

ent = Entry(win)    

def ent_p():
    a = int(ent.get())
    def GuGu(a):
        result = []
        i = 1
        while i < 10:
            result.append(a*i)
            i = i + 1
        return result

    def clear(Widget):
        Widget.destroy()
        btn_clear.destroy()
    
    btn_clear = Button(win)
    btn_clear.config(
        text = "clear",
        width = 10
        )
    btn_clear.config(command = lambda : clear(label1))
    label1 = tk.Label(
        win, 
        text = str(a) + " 단\n\n" 
        + str(a) + " x 1 = " + str(GuGu(a)[0]) + "\n" 
        + str(a) + " x 2 = " + str(GuGu(a)[1]) + "\n" 
        + str(a) + " x 3 = " + str(GuGu(a)[2]) + "\n" 
        + str(a) + " x 4 = " + str(GuGu(a)[3]) + "\n" 
        + str(a) + " x 5 = " + str(GuGu(a)[4]) + "\n" 
        + str(a) + " x 6 = " + str(GuGu(a)[5]) + "\n" 
        + str(a) + " x 7 = " + str(GuGu(a)[6]) + "\n" 
        + str(a) + " x 8 = " + str(GuGu(a)[7]) + "\n" 
        + str(a) + " x 9 = " + str(GuGu(a)[8]),
        font = 30)

    label1.pack()
    btn_clear.pack()


btn = Button(win)
btn.config(
    text = "구구단을 외자",
    width = 10
    )
btn.config(command = ent_p)

ent.config(width = 10)

ent.pack()
btn.pack()

win.mainloop()

