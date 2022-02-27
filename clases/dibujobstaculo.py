import tkinter
from tkinter import *
import turtle

class Dibujar_obs():
    def __init__(self):
        self.ventana=Tk()
        self.ventana.title("Gráfica zonas")
        self.canvas=Canvas(master=self.ventana,width=530,height=250)
        self.canvas.pack()
        self.t = turtle.RawTurtle(self.canvas)

    def dibujar_sala(self,ancho,largo):
        for _ in range(2):
            self.t.forward(ancho)
            self.t.left(90)

            self.t.forward(largo)
            self.t.left(90)
    def dibujar_zona(self,zona,color):
        self.t.penup()
        self.t.goto(zona.posicion.get("posx"),zona.posicion.get("posy"))
        self.t.pendown()
        self.t.fillcolor(color)
        self.t.begin_fill()
        self.dibujar_sala(zona.dimension.get("ancho"),zona.dimension.get("largo"))
        self.t.end_fill()

    def dibujar_zona_grande(self,zonas):
        colores=["red","green","blue","purple"]
        i=0
        for zona in zonas:
            self.dibujar_zona(zona,colores[i%4])
            i+=1
    def dibujar_zonas(self):
        for i in range(0,len(self.zonas)):
            self.dibujar_sala(self.zonas[i].get("ancho"), self.zonas[i].get("largo"),i)

    def crear_ventana(self,ancho1,largo1,posicion,ancho2,largo2):
        self.dibujar_sala(ancho1,largo1)
        self.t.penup()
        self.t.goto(posicion.get("posx"),posicion.get("posy"))
        self.t.pendown()
        self.t.fillcolor("black")
        self.t.begin_fill()
        self.dibujar_sala(ancho2,largo2)
        self.t.end_fill()
        self.ventana.mainloop()