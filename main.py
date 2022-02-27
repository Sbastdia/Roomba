import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from clases.dibujo import Dibujar
from clases.Pestana import Pestana
from clases.Robot import Robot
from clases.Ventana import Ventana
from clases.Forma2 import Principal
from clases.Forma1 import Principal2



if __name__=="__main__":
  
  window=Ventana("Hagamos una Roomba")
  def ejecuccion_Principal():
    window.withdraw()
    p=Principal(window)
  def ejecuccion_Principal2():
    window.withdraw()
    p=Principal2(window)
  color="light steel blue"
  lbl = Label(window, text="Elige la forma en que debe limpiar Paqui",bg=color,fg="black")
  lbl.pack()
  btn = Button(window, text="Método con obstáculo", command=ejecuccion_Principal)
  btn2 = Button(window, text="Método sin obstáculo", command=ejecuccion_Principal2)
  btn.pack()
  btn2.pack()
  window.mainloop()