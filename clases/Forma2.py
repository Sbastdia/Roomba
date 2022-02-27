import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import turtle
from clases.dibujobstaculo import Dibujar_obs
from clases.Sitios import *
from clases.Pestana import *
from clases.Ventana import Ventana
from clases.Robot import Robot
class Principal():
    def __init__(self,principal):
        self.principal=principal
        self.window=Ventana("Hagamos una Roomba")
        self.window.protocol("WM_DELETE_WINDOW", self.volver)
        self.pestadicionales = []
        self.posicionObs={}#x,y
        self.medidasZona={}#ancho,largo
        self.medidasObs={}#ancho, largo obstaculo
        self.roomba=Robot("Paqui",2)
        nb = ttk.Notebook(self.window)
        nb.pack(fill="both", expand="yes")
        color="light steel blue"
        self.Zonas=Pestana(nb)
        nb.add(self.Zonas.pl, text="Zonas")
        self.Obstaculo=Pestana_obs(nb)
        nb.add(self.Obstaculo.pl, text="Obstaculo")
        self.zonas=[]
        self.btn = Button(self.window, text="Cálculos", command=self.calculos)
        self.btn.pack()
        self.btn3=Button(self.window,text="Modo Dibujo Zonas", command=self.dibujo_z)
        self.btn2=Button(self.window,text="Modo Dibujo Obstáculo", command=self.dibujo_o)
        self.window.mainloop()

  
    def volver(self):
      self.principal.deiconify()
      self.window.destroy()

    
    def calculos(self):
        anchoZona = int(self.Zonas.spinancho.get())/100
        largoZona = int(self.Zonas.spinlargo.get())/100
        self.medidasZona={"ancho":anchoZona,"largo":largoZona}
        anchoObs = int(self.Obstaculo.spinancho.get())/100
        largoObs = int(self.Obstaculo.spinlargo.get())/100
        self.medidasObs={"ancho":anchoObs,"largo":largoObs}
        posxObs = int(self.Obstaculo.spinPosx.get())/100
        posyObs = int(self.Obstaculo.spinPosy.get())/100
        self.posicionObs={"posx":posxObs,"posy":posyObs}
        obstReal=Lugar(self.medidasObs,self.posicionObs)
        sala=Sala(self.medidasZona,obstReal)
        self.zonas=sala.crear_zonas()
        superficie=0
        for zona in self.zonas:
            superficie+=zona.area()
            print("Ancho: "+str(zona.dimension.get("ancho"))+" Largo: " + str(zona.dimension.get("largo"))+" Posx: " + str(zona.posicion.get("posx"))+" Posy: " + str(zona.posicion.get("posy")))
        messagebox.showinfo(message="La superficie a limpiar es de: " + str(superficie) + " metros cuadrados", title="Superficie total")
        messagebox.showinfo(self.roomba.nombre+" al habla","El tiempo estimado es: "+str(self.roomba.tiempoLimpiezaEnMinutos(superficie)) + " minutos")
        messagebox.showinfo(self.roomba.nombre+" al habla", self.roomba.hablar(self.roomba.tiempoLimpiezaEnMinutos(superficie)))
        messagebox.showwarning(self.roomba.nombre+" al habla", "¡Pulsa los botones para distintas visiones gráficas!")
        self.btn.pack_forget()
        self.btn2.pack()
        self.btn3.pack()

    def dibujo_o(self):
        Dibujar_obs().crear_ventana(self.medidasZona.get("ancho"), self.medidasZona.get("largo"), self.posicionObs,self.medidasObs.get("ancho"), self.medidasObs.get("largo"))
    def dibujo_z(self):
        Dibujar_obs().dibujar_zona_grande(self.zonas)