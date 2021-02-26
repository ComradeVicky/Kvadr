from tkinter import *
import math


gerb = Tk()
gerb.title("kvadrrrrr")
gerb.geometry("600x400")
gerb.resizable(False, False)
hho = StringVar()
hoh = StringVar()
ohh = StringVar()

def nova(event=None):
    if str(text["state"]) == "readonly":
        ahahha()
    else:
        getnik()

def ahahha():
    text.config(state = "normal")
    txet.config(state = "normal")
    ttex.config(state = "normal")
    hho.set("")
    hoh.set("")
    ohh.set("")
    text.focus()
    ded.config(text = "")
    exo.grid(column=2,row=7, sticky=W)
    vysl.config(text="", font=("Sans", 20))
    vysk.config(text="", font=("Sans", 20))
    ex.config(text = "x\u2081= ")



def getnik(event=None):
    try:
        a = float(hho.get())
        if a == 0:
            print("neni kvadr debile")
            return
        b = float(hoh.get())
        c = float(ohh.get())
        
    except:
        print("SRAČKO")
        sracko = Toplevel(gerb)
        sracko.title("SRAČKO")
        sracko.geometry("200x100")
        sracko.config(bg="white")
        sra = Label(sracko, text = "SRAČKO")
        sra.config(bg="white", font=("Sans", 25, "bold"))
        sra.place(x=30, y=20)
        return
    rov = str(a) + "x\u00b2" + " + " + str(b) + "x" + " + " + str(c)
    f = rov.replace("+ -", "- ")

    print(f)

    D = b * b - (4 * a * c)
    print("Diskriminant: " + str(D))
    if str(D).endswith(".0"):
        blblbl = str(D).replace(".0", "")
    ded.config(text = blblbl)

    if D < 0:
        print("Nemá řešení")
        vysl.config(text = "\u2205", font=("Sans", 25, "bold"))
        vysk.config(text = "\u2205", font=("Sans", 25, "bold"))
    if D == 0:
        x = (-b + math.sqrt(D)) / (2 * a)
        if str(x).endswith(".0"):
            x = str(x).replace(".0", "")
            print("x = " + str(x))
            vysl.config(text = str(x))
            exo.grid_forget()
            ex.config(text = "x =")
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        if str(x1).endswith(".0"):
            x1 = str(x1).replace(".0", "")
        if str(x2).endswith(".0"):
            x2= str(x2).replace(".0", "")
        print("x1 = " + str(x1))
        print("x2 = " + str(x2))
        vysl.config(text = str(x1))
        vysk.config(text = str(x2))
    text.config(state = "readonly")
    txet.config(state = "readonly")
    ttex.config(state = "readonly")

text = Entry(gerb, width = 2, textvariable = hho)
text.config(font=("Sans", 30))

txet = Entry(gerb, width = 2, textvariable = hoh)
txet.config(font=("Sans", 30))

ttex = Entry(gerb, width = 2, textvariable = ohh)
ttex.config(font=("Sans", 30))

b = Button(
    text = "tláča",
    command = getnik
)
exi = Button(
    command = ahahha,
    text = "re"
)

h = Label(text = " x\u00b2 + ")
h.config(font=("Sans", 30))

c = Label(gerb, text = " x + ")
c.config(font=("Sans", 30))

o = Label(gerb, text = " = 0")
o.config(font=("Sans", 30))

diskr = Label(gerb, text = "Diskriminant:", justify = LEFT)
diskr.config(font=("Sans", 20))

ded = Label(gerb, text = "")
ded.config(font=("Sans", 20))

ex = Label(gerb, text = "x\u2081= ")
ex.config(font=("Sans", 20))

exo = Label(gerb, text = "x\u2082= ")
exo.config(font=("Sans", 20))

vysl = Label(gerb, text = "")
vysl.config(font=("Sans", 20))

vysk = Label(gerb, text = "")
vysk.config(font=("Sans", 20))

gerb.columnconfigure(0, minsize=103)
gerb.rowconfigure(1, minsize = 80)
gerb.rowconfigure(4, minsize = 30)
gerb.rowconfigure(6, minsize = 50)
gerb.rowconfigure(7, minsize = 50)

text.focus()
gerb.bind("<Return>", nova)
vysl.grid(column=3,row=6, sticky=W, columnspan=10)
vysk.grid(column=3,row=7, sticky=W, columnspan=10)
ex.grid(column=2,row=6, sticky=W)
exo.grid(column=2,row=7, sticky=W)
exi.grid(column=4, row=4)
diskr.grid(column=2, row=5, columnspan=2)
ded.grid(column=4, row=5, columnspan=2, sticky=W)
b.grid(column=4, row=3)
text.grid(column=2, row=2)
h.grid(column=3, row=2)
txet.grid(column=4, row=2)
c.grid(column=5, row=2)
ttex.grid(column=6, row=2)
o.grid(column=7,row=2)
gerb.mainloop()