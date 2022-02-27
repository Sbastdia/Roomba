import tkinter
from tkinter import *
import turtle
class Dibujar():
    def __init__(self, zonas):
        self.zonas=zonas
        self.ventana=Tk()
        self.ventana.title("Gráfica zonas")
        self.canvas=Canvas(master=self.ventana,width=530,height=250)
        self.canvas.pack()
        self.t = turtle.RawTurtle(self.canvas)
    def dibujar_sala(self,ancho,largo,i):
        for _ in range(2):
            self.t.forward(ancho)
            self.t.left(90)

            self.t.forward(largo)
            self.t.left(90)
        if i<3:
            self.t.right(90)
        else:
            self.t.right(270)
            self.t.forward(largo)

    def dibujar_sala_impar(self,ancho,largo):
        for _ in range(2):
            self.t.forward(ancho)
            self.t.right(90)

            self.t.forward(largo)
            self.t.right(90)
        self.t.left(270)
        self.t.forward(largo)

    def dibujar_zonas(self):
        for i in range(0,len(self.zonas)):
            if i >3 and i%2==0:
                self.dibujar_sala_impar(self.zonas[i].get("ancho"), self.zonas[i].get("largo"))
            else:
                self.dibujar_sala(self.zonas[i].get("ancho"), self.zonas[i].get("largo"),i)

    def crear_ventana(self):
        self.dibujar_zonas()
        self.ventana.mainloop()
