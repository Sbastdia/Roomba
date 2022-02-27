import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from clases.dibujo import Dibujar
from clases.Pestana import Pestana
from clases.Robot import Robot
from clases.Ventana import Ventana

class Principal2():
  def __init__(self,principal):
    self.principal=principal
    self.window=Ventana("Hagamos una Roomba")
    self.window.protocol("WM_DELETE_WINDOW", self.volver)
    self.roomba=Robot("Paqui",2)
    
    self.pestadicionales = []
    self.zonas=[]
    
    self.nb = ttk.Notebook(self.window)
    self.nb.pack(fill="both", expand="yes")
    color="light steel blue"
    self.pl = Frame(self.nb, background=color)
    self.nb.add(self.pl, text="Zonas")
    
    self.lbl = Label(self.pl, text="¿Cuantas zonas tiene el lugar?", bg=color,fg="black")
    self.lbl.grid(column=6, row=0)
    
    self.spin = Spinbox(self.pl, from_=1, to=20)
    self.spin.grid(column=6, row=1)

    self.btn = Button(self.pl, text="Pulsa", command=self.creasalas)
    self.btn2 = Button(self.window, text="Calcula", command=self.calcula)
    self.btn3= Button(self.window,text="Visión gráfica", command=self.dibujar)
  
    
    self.btn.grid(column=6, row=3)
    self.window.mainloop()

  def volver(self):
    self.principal.deiconify()
    self.window.destroy()
    
  def dibujar(self):
      print(self.zonas)
      dibujo=Dibujar(self.zonas)
      dibujo.crear_ventana()
  
  
  def creasalas(self):
      numerosalas = int(self.spin.get())
      for i in range(numerosalas):
          pestaux = Pestana(self.nb)
          nombre="Sala " + str(i+1)
          self.nb.add(pestaux.pl, text=nombre)
          self.pestadicionales.append(pestaux)
      self.pl.destroy()
      self.btn2.pack()
  
  def calcula(self):
      superficie=0
      for pest in self.pestadicionales:
          ancho=int(pest.spinancho.get())/100
          largo=int(pest.spinlargo.get())/100
          self.zonas.append({"largo":largo,"ancho":ancho})
          superficie+=(ancho*largo)
      messagebox.showinfo(message="La superficie a limpiar es de: " + str(superficie) + " metros cuadrados", title="Superficie total")
      messagebox.showinfo(self.roomba.nombre+" al habla","El tiempo estimado es: "+str(self.roomba.tiempoLimpiezaEnMinutos(superficie)) + " minutos")
      messagebox.showinfo(self.roomba.nombre+" al habla", self.roomba.hablar(self.roomba.tiempoLimpiezaEnMinutos(superficie)))
      messagebox.showwarning(self.roomba.nombre+" al habla", "¡Pulsa el botón de visión gráfica!")
      self.btn2.pack_forget()
      self.btn3.pack()