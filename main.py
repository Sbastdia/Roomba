import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import script

class Pestana():
    def __init__(self, nb):
        self.pl = Frame(nb)
        self.lblancho = Label(self.pl, text="Ancho")
        self.spinancho = Spinbox(self.pl, from_=1, to=5)
        self.lbllargo = Label(self.pl, text="Largo")
        self.spinlargo = Spinbox(self.pl, from_=1, to=5)
        self.lblancho.grid(column=0, row=0)
        self.spinancho.grid(column=1, row=0)
        self.lbllargo.grid(column=0, row=1)
        self.spinlargo.grid(column=1, row=1)

window = Tk()
window.title("Hagamos una Roomba")
window.geometry("400x255")

pestadicionales = []

nb = ttk.Notebook(window)
nb.pack(fill="both", expand="yes")
color="light steel blue"
pl = Frame(nb, background=color)
nb.add(pl, text="Zonas")


window.configure(background=color)

lbl = Label(pl, text="¿Cuantas zonas tiene el lugar?",bg=color,fg="black")
lbl.grid(column=6, row=0)

spin = Spinbox(pl, from_=1, to=20)
spin.grid(column=6, row=1)


def calcula():
    superficie=0
    for pest in pestadicionales:
        ancho=int(pest.spinancho.get())
        largo=int(pest.spinlargo.get())
        superficie+=(ancho*largo)
    messagebox.showinfo(message=str(superficie) + " metros cuadrados", title="Superficie total")

btn2 = Button(window, text="Calcula", command=calcula)

def creasalas():
    numerosalas = int(spin.get())
    for i in range(numerosalas):
        pestaux = Pestana(nb)
        nombre="Sala " + str(i+1)
        nb.add(pestaux.pl, text=nombre)
        pestadicionales.append(pestaux)
    pl.destroy()
    btn2.pack()

btn = Button(pl, text="Pulsa", command=creasalas)
btn.grid(column=6, row=3)


window.mainloop()
