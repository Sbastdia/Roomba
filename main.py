
import tkinter as tk
import alimpiar
import lista
import diccionarios
import script
import tupla
window1 = tk.Tk()
window1.title("Hora de hacer una Roomba")
window1.geometry("300x300")
zonas=tk.Spinbox(from=1,to=8,increment=1)
hello = tk.Label(text="¿Cuantas zonas tiene tu casa?")
hello.pack()
button = tk.Button(text="Pulsa")
button.pack()

tk.mainloop()