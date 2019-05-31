from Tkinter import *


def columna1():
    pass


def columna2():
    pass


def columna3():
    pass


def columna4():
    pass


def columna5():
    pass


def columna6():
    pass


def columna7():
    pass


v = Tk()
v.title("Conecta 4")

jugador = Label(v, text="Turno de: Nicolas")
jugador.pack()

# marco 1 - botones
f1 = Frame(v)
f1.pack()
b1 = Button(f1, text="C1", command=columna1, width=7)
b2 = Button(f1, text="C2", command=columna2, width=7)
b3 = Button(f1, text="C3", command=columna3, width=7)
b4 = Button(f1, text="C4", command=columna4, width=7)
b5 = Button(f1, text="C5", command=columna5, width=7)
b6 = Button(f1, text="C6", command=columna6, width=7)
b7 = Button(f1, text="C7", command=columna7, width=7)
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
b4.pack(side=LEFT)
b5.pack(side=LEFT)
b6.pack(side=LEFT)
b7.pack(side=LEFT)

# dimensiones
d = 86      # lado de cuadrado
h = d*6     # alto
w = d*7     # ancho

# canvas
c = Canvas(v, height=h, width=w)
c.pack()

# dibujar lineas verticales
for fila in range(5):
    c.create_line(0, d*(fila+1), w, d*(fila+1))

# dibujar lineas horizontales
for columna in range(6):
    c.create_line(d*(columna+1), 0, d*(columna+1), h)
v.mainloop()
