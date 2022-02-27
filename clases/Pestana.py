import tkinter
from tkinter import *

class Pestana():
    def __init__(self, nb,background="light steel blue"):
        self.pl = Frame(nb,background=background)
        self.lblancho = Label(self.pl, text="Ancho en centímetros")
        self.spinancho = Spinbox(self.pl, from_=100, to=5000,increment=100)
        self.lbllargo = Label(self.pl, text="Largo en centímetros")
        self.spinlargo = Spinbox(self.pl, from_=100, to=5000,increment=100)
        self.lblancho.grid(column=0, row=0)
        self.spinancho.grid(column=1, row=0)
        self.lbllargo.grid(column=0, row=1)
        self.spinlargo.grid(column=1, row=1)

class Pestana_obs(Pestana):
    def __init__(self, nb,background="light steel blue"):
        Pestana.__init__(self, nb, background)
        self.lblPosx = Label(self.pl, text="Coordenada 'x' esquina abajo izquierda")
        self.spinPosx = Spinbox(self.pl, from_=100, to=50000,increment=100)
        self.lblPosy = Label(self.pl, text="Coordenada 'y' esquina abajo izquierda")
        self.spinPosy = Spinbox(self.pl, from_=100, to=50000,increment=100)
        self.lblPosx.grid(column=0, row=2)
        self.spinPosx.grid(column=1, row=2)
        self.lblPosy.grid(column=0, row=3)
        self.spinPosy.grid(column=1, row=3)