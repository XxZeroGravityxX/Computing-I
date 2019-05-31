from Tkinter import *
import random
class Ganador:
    def __init__(self,x):
        self.t=x
    def ganaono(self,x):
        for col in range(7): #ganador en columnas
            for fila in range(3):
                if self.t[col][fila]==self.t[col][fila+1]==self.t[col][fila+2]==self.t[col][fila+3]==x and self.t[col][fila]!=0:
                    return True
        for fila in range(6): #ganador en filas
            for col in range(4):
                if self.t[col][fila]==self.t[col+1][fila]==self.t[col+2][fila]==self.t[col+3][fila]==x and self.t[col][fila]!=0:
                    return True
        for fila in range(3): #ganador en diagonales izq arriba-der abajo
            for col in range(4):
                if self.t[col][fila]==self.t[col+1][fila+1]==self.t[col+2][fila+2]==self.t[col+3][fila+3]==x and self.t[col][fila]!=0:
                    return True
        for fila in range(5,2,-1): #ganador en diagonales izq abaj-der arriba
            for col in range(4):
                if self.t[col][fila]==self.t[col+1][fila-1]==self.t[col+2][fila-2]==self.t[col+3][fila-3]==self.t[col+3][fila-3]==x and self.t[col][fila]!=0:
                    return True
    def nombrarganador(self,x):
        vgan=Tk()
        vgan.title("Ganador")
        lgan=Label(vgan,text=x).pack()
        vgan.mainloop()       
def pvp():
    txtj1="Turno de: "+str(j1.get())
    txtj2="Turno de: "+str(j2.get())
    jug=txtj1
    # tablero, donde 1 son las fichas del j1 y 2 las del j2
    tablero=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
    t=Ganador(tablero)
    def columna1():
        fa1=int(FILA1.cget("text"))
        if fa1==1: b1.config(state=DISABLED)
        if jugador.cget("text")==txtj1:    # método para cambiar nombre de jugador
            c.create_oval(0,d*(fa1-1),d,d*fa1,fill="red")
            tablero[0][fa1-1]=1
            if t.ganaono(1): t.nombrarganador("Gana "+str(j1.get()))
            jug=txtj2
        elif jugador.cget("text")==txtj2:
            c.create_oval(0,d*(fa1-1),d,d*fa1,fill="blue")
            tablero[0][fa1-1]=2
            if t.ganaono(2): t.nombrarganador("Gana "+str(j2.get()))
            jug=txtj1
        jugador.config(text=jug)
        FILA1.config(text=str(fa1-1))
    def columna2():
        fa2=int(FILA2.cget("text"))
        if fa2==1: b2.config(state=DISABLED)
        if jugador.cget("text")==txtj1:
            c.create_oval(d,d*(fa2-1),d*2,d*fa2,fill="red")
            tablero[1][fa2-1]=1
            if t.ganaono(1): t.nombrarganador("Gana "+str(j1.get()))
            jug=txtj2
        elif jugador.cget("text")==txtj2:
            c.create_oval(d,d*(fa2-1),d*2,d*fa2,fill="blue")
            tablero[1][fa2-1]=2
            if t.ganaono(2): t.nombrarganador("Gana "+str(j2.get()))
            jug=txtj1
        jugador.config(text=jug)
        FILA2.config(text=str(fa2-1))
    def columna3():
        fa3=int(FILA3.cget("text"))
        if fa3==1: b3.config(state=DISABLED)
        if jugador.cget("text")==txtj1:
            c.create_oval(d*2,d*(fa3-1),d*3,d*fa3,fill="red")
            tablero[2][fa3-1]=1
            if t.ganaono(1): t.nombrarganador("Gana "+str(j1.get()))
            jug=txtj2
        elif jugador.cget("text")==txtj2:
            c.create_oval(d*2,d*(fa3-1),d*3,d*fa3,fill="blue")
            tablero[2][fa3-1]=2
            if t.ganaono(2): t.nombrarganador("Gana "+str(j2.get()))
            jug=txtj1
        jugador.config(text=jug)
        FILA3.config(text=str(fa3-1))
    def columna4():
        fa4=int(FILA4.cget("text"))
        if fa4==1: b4.config(state=DISABLED)
        if jugador.cget("text")==txtj1:
            c.create_oval(d*3,d*(fa4-1),d*4,d*fa4,fill="red")
            tablero[3][fa4-1]=1
            if t.ganaono(1): t.nombrarganador("Gana "+str(j1.get()))
            jug=txtj2
        elif jugador.cget("text")==txtj2:
            c.create_oval(d*3,d*(fa4-1),d*4,d*fa4,fill="blue")
            tablero[3][fa4-1]=2
            if t.ganaono(2): t.nombrarganador("Gana "+str(j2.get()))
            jug=txtj1
        jugador.config(text=jug)
        FILA4.config(text=str(fa4-1))
    def columna5():
        fa5=int(FILA5.cget("text"))
        if fa5==1: b5.config(state=DISABLED)
        if jugador.cget("text")==txtj1:
            c.create_oval(d*4,d*(fa5-1),d*5,d*fa5,fill="red")
            tablero[4][fa5-1]=1
            if t.ganaono(1): t.nombrarganador("Gana "+str(j1.get()))
            jug=txtj2
        elif jugador.cget("text")==txtj2:
            c.create_oval(d*4,d*(fa5-1),d*5,d*fa5,fill="blue")
            tablero[4][fa5-1]=2
            if t.ganaono(2): t.nombrarganador("Gana "+str(j2.get()))
            jug=txtj1
        jugador.config(text=jug)
        FILA5.config(text=str(fa5-1))
    def columna6():
        fa6=int(FILA6.cget("text"))
        if fa6==1: b6.config(state=DISABLED)
        if jugador.cget("text")==txtj1:
            c.create_oval(d*5,d*(fa6-1),d*6,d*fa6,fill="red")
            tablero[5][fa6-1]=1
            if t.ganaono(1): t.nombrarganador("Gana "+str(j1.get()))
            jug=txtj2
        elif jugador.cget("text")==txtj2:
            c.create_oval(d*5,d*(fa6-1),d*6,d*fa6,fill="blue")
            tablero[5][fa6-1]=2
            if t.ganaono(2): t.nombrarganador("Gana "+str(j2.get()))
            jug=txtj1
        jugador.config(text=jug)
        FILA6.config(text=str(fa6-1))
    def columna7():
        fa7=int(FILA7.cget("text"))
        if fa7==1: b7.config(state=DISABLED)
        if jugador.cget("text")==txtj1:
            c.create_oval(d*6,d*(fa7-1),d*7,d*fa7,fill="red")
            tablero[6][fa7-1]=1
            if t.ganaono(1): t.nombrarganador("Gana "+str(j1.get()))
            jug=txtj2
        elif jugador.cget("text")==txtj2:
            c.create_oval(d*6,d*(fa7-1),d*7,d*fa7,fill="blue")
            tablero[6][fa7-1]=2
            if t.ganaono(2): t.nombrarganador("Gana "+str(j2.get()))
            jug=txtj1
        jugador.config(text=jug)
        FILA7.config(text=str(fa7-1))
    v = Tk()
    v.title("Conecta 4")
    jugador = Label(v, text=jug)
    FILA1=Label(v,text="6")
    FILA2=Label(v,text="6")
    FILA3=Label(v,text="6")
    FILA4=Label(v,text="6")
    FILA5=Label(v,text="6")
    FILA6=Label(v,text="6")
    FILA7=Label(v,text="6")
    jugador.pack()
    # marco 1 - botones
    f1 = Frame(v)
    f1.pack()
    b1 = Button(f1, text="C1", command=columna1, width=11)
    b2 = Button(f1, text="C2", command=columna2, width=11)
    b3 = Button(f1, text="C3", command=columna3, width=11)
    b4 = Button(f1, text="C4", command=columna4, width=11)
    b5 = Button(f1, text="C5", command=columna5, width=11)
    b6 = Button(f1, text="C6", command=columna6, width=11)
    b7 = Button(f1, text="C7", command=columna7, width=11)
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
    
def pvcpu():
    txtj1="Turno de: "+str(j1.get())
    txtc="Turno de: CPU"
    jug=txtj1
    # tablero, donde 1 son las fichas del j1 y 2 las de la CPU
    tablero=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
    t=Ganador(tablero)
    L=[1,2,3,4,5,6,7]
    def columna1():
        fa1=int(FILA1.cget("text")) #porque no sé cambiar los "x" valores de la variable (fax)
        fa2=int(FILA2.cget("text"))
        fa3=int(FILA3.cget("text"))
        fa4=int(FILA4.cget("text"))
        fa5=int(FILA5.cget("text"))
        fa6=int(FILA6.cget("text"))
        fa7=int(FILA7.cget("text"))
        if fa1==0:
            try: L.remove(1) #método para evitar que fa se vuelva negatito y ocurran errores al definir al ganador
            except ValueError: pass
        if fa2==0:
            try: L.remove(2)
            except ValueError: pass
        if fa3==0:
            try: L.remove(3)
            except ValueError: pass
        if fa4==0:
            try: L.remove(4)
            except ValueError: pass
        if fa5==0:
            try: L.remove(5)
            except ValueError: pass
        if fa6==0:
            try: L.remove(6)
            except ValueError: pass
        if fa7==0:
            try: L.remove(7)
            except ValueError: pass
        i=len(L)
        if fa1==1: b1.config(state=DISABLED)
        if jugador.cget("text")==txtj1:    # método para cambiar nombre de jugador
            c.create_oval(0,d*(fa1-1),d,d*fa1,fill="green")
            tablero[0][fa1-1]=1
            if t.ganaono(1): t.nombrarganador("Gana "+str(j1.get()))
            jug=txtc
            jugador.config(text=jug)
        FILA1.config(text=str(fa1-1))
        # jugada de la CPU
        cl=random.randint(1,i)
        colcpu=L[cl-1]
        if colcpu==1: fa=int(FILA1.cget("text"));FILA=FILA1;b=b1
        elif colcpu==2: fa=int(FILA2.cget("text"));FILA=FILA2;b=b2
        elif colcpu==3: fa=int(FILA3.cget("text"));FILA=FILA3;b=b3
        elif colcpu==4: fa=int(FILA4.cget("text"));FILA=FILA4;b=b4
        elif colcpu==5: fa=int(FILA5.cget("text"));FILA=FILA5;b=b5
        elif colcpu==6: fa=int(FILA6.cget("text"));FILA=FILA6;b=b6
        else: fa=int(FILA7.cget("text"));FILA=FILA7;b=b7
        c.create_oval(d*(colcpu-1),d*(fa-1),d*colcpu,d*fa,fill="yellow")
        tablero[colcpu-1][fa-1]=2
        if tablero[colcpu-1][0]!=0: b.config(state=DISABLED)
        if t.ganaono(2): t.nombrarganador("Gana CPU")
        jug=txtj1
        jugador.config(text=jug)
        FILA.config(text=str(fa-1))
    def columna2():
        fa1=int(FILA1.cget("text"))
        fa2=int(FILA2.cget("text"))
        fa3=int(FILA3.cget("text"))
        fa4=int(FILA4.cget("text"))
        fa5=int(FILA5.cget("text"))
        fa6=int(FILA6.cget("text"))
        fa7=int(FILA7.cget("text"))
        if fa1==0:
            try: L.remove(1)
            except ValueError: pass
        if fa2==0:
            try: L.remove(2)
            except ValueError: pass
        if fa3==0:
            try: L.remove(3)
            except ValueError: pass
        if fa4==0:
            try: L.remove(4)
            except ValueError: pass
        if fa5==0:
            try: L.remove(5)
            except ValueError: pass
        if fa6==0:
            try: L.remove(6)
            except ValueError: pass
        if fa7==0:
            try: L.remove(7)
            except ValueError: pass
        i=len(L)
        if fa2==1: b2.config(state=DISABLED)
        if jugador.cget("text")==txtj1:
            c.create_oval(d,d*(fa2-1),d*2,d*fa2,fill="green")
            tablero[1][fa2-1]=1
            if t.ganaono(1): t.nombrarganador("Gana "+str(j1.get()))
            jug=txtc
            jugador.config(text=jug)
        FILA2.config(text=str(fa2-1))
        cl=random.randint(1,i)
        colcpu=L[cl-1]
        if colcpu==1: fa=int(FILA1.cget("text"));FILA=FILA1;b=b1
        elif colcpu==2: fa=int(FILA2.cget("text"));FILA=FILA2;b=b2
        elif colcpu==3: fa=int(FILA3.cget("text"));FILA=FILA3;b=b3
        elif colcpu==4: fa=int(FILA4.cget("text"));FILA=FILA4;b=b4
        elif colcpu==5: fa=int(FILA5.cget("text"));FILA=FILA5;b=b5
        elif colcpu==6: fa=int(FILA6.cget("text"));FILA=FILA6;b=b6
        else: fa=int(FILA7.cget("text"));FILA=FILA7;b=b7
        c.create_oval(d*(colcpu-1),d*(fa-1),d*colcpu,d*fa,fill="yellow")
        tablero[colcpu-1][fa-1]=2
        if tablero[colcpu-1][0]!=0: b.config(state=DISABLED)
        if t.ganaono(2): t.nombrarganador("Gana CPU")
        jug=txtj1
        jugador.config(text=jug)
        FILA.config(text=str(fa-1))
    def columna3():
        fa1=int(FILA1.cget("text"))
        fa2=int(FILA2.cget("text"))
        fa3=int(FILA3.cget("text"))
        fa4=int(FILA4.cget("text"))
        fa5=int(FILA5.cget("text"))
        fa6=int(FILA6.cget("text"))
        fa7=int(FILA7.cget("text"))
        if fa1==0:
            try: L.remove(1)
            except ValueError: pass
        if fa2==0:
            try: L.remove(2)
            except ValueError: pass
        if fa3==0:
            try: L.remove(3)
            except ValueError: pass
        if fa4==0:
            try: L.remove(4)
            except ValueError: pass
        if fa5==0:
            try: L.remove(5)
            except ValueError: pass
        if fa6==0:
            try: L.remove(6)
            except ValueError: pass
        if fa7==0:
            try: L.remove(7)
            except ValueError: pass
        i=len(L)
        if fa3==1: b3.config(state=DISABLED)
        if jugador.cget("text")==txtj1:
            c.create_oval(d*2,d*(fa3-1),d*3,d*fa3,fill="green")
            tablero[2][fa3-1]=1
            if t.ganaono(1): t.nombrarganador("Gana "+str(j1.get()))
            jug=txtc
            jugador.config(text=jug)
        FILA3.config(text=str(fa3-1))
        cl=random.randint(1,i)
        colcpu=L[cl-1]
        if colcpu==1: fa=int(FILA1.cget("text"));FILA=FILA1;b=b1
        elif colcpu==2: fa=int(FILA2.cget("text"));FILA=FILA2;b=b2
        elif colcpu==3: fa=int(FILA3.cget("text"));FILA=FILA3;b=b3
        elif colcpu==4: fa=int(FILA4.cget("text"));FILA=FILA4;b=b4
        elif colcpu==5: fa=int(FILA5.cget("text"));FILA=FILA5;b=b5
        elif colcpu==6: fa=int(FILA6.cget("text"));FILA=FILA6;b=b6
        else: fa=int(FILA7.cget("text"));FILA=FILA7;b=b7
        c.create_oval(d*(colcpu-1),d*(fa-1),d*colcpu,d*fa,fill="yellow")
        tablero[colcpu-1][fa-1]=2
        if tablero[colcpu-1][0]!=0: b.config(state=DISABLED)
        if t.ganaono(2): t.nombrarganador("Gana CPU")
        jug=txtj1
        jugador.config(text=jug)
        FILA.config(text=str(fa-1))
    def columna4():
        fa1=int(FILA1.cget("text"))
        fa2=int(FILA2.cget("text"))
        fa3=int(FILA3.cget("text"))
        fa4=int(FILA4.cget("text"))
        fa5=int(FILA5.cget("text"))
        fa6=int(FILA6.cget("text"))
        fa7=int(FILA7.cget("text"))
        if fa1==0:
            try: L.remove(1)
            except ValueError: pass
        if fa2==0:
            try: L.remove(2)
            except ValueError: pass
        if fa3==0:
            try: L.remove(3)
            except ValueError: pass
        if fa4==0:
            try: L.remove(4)
            except ValueError: pass
        if fa5==0:
            try: L.remove(5)
            except ValueError: pass
        if fa6==0:
            try: L.remove(6)
            except ValueError: pass
        if fa7==0:
            try: L.remove(7)
            except ValueError: pass
        i=len(L)
        if fa4==1: b4.config(state=DISABLED)
        if jugador.cget("text")==txtj1:
            c.create_oval(d*3,d*(fa4-1),d*4,d*fa4,fill="green")
            tablero[3][fa4-1]=1
            if t.ganaono(1): t.nombrarganador("Gana "+str(j1.get()))
            jug=txtc
            jugador.config(text=jug)
        FILA4.config(text=str(fa4-1))
        cl=random.randint(1,i)
        colcpu=L[cl-1]
        if colcpu==1: fa=int(FILA1.cget("text"));FILA=FILA1;b=b1
        elif colcpu==2: fa=int(FILA2.cget("text"));FILA=FILA2;b=b2
        elif colcpu==3: fa=int(FILA3.cget("text"));FILA=FILA3;b=b3
        elif colcpu==4: fa=int(FILA4.cget("text"));FILA=FILA4;b=b4
        elif colcpu==5: fa=int(FILA5.cget("text"));FILA=FILA5;b=b5
        elif colcpu==6: fa=int(FILA6.cget("text"));FILA=FILA6;b=b6
        else: fa=int(FILA7.cget("text"));FILA=FILA7;b=b7
        c.create_oval(d*(colcpu-1),d*(fa-1),d*colcpu,d*fa,fill="yellow")
        tablero[colcpu-1][fa-1]=2
        if tablero[colcpu-1][0]!=0: b.config(state=DISABLED)
        if t.ganaono(2): t.nombrarganador("Gana CPU")
        jug=txtj1
        jugador.config(text=jug)
        FILA.config(text=str(fa-1))
    def columna5():
        fa1=int(FILA1.cget("text"))
        fa2=int(FILA2.cget("text"))
        fa3=int(FILA3.cget("text"))
        fa4=int(FILA4.cget("text"))
        fa5=int(FILA5.cget("text"))
        fa6=int(FILA6.cget("text"))
        fa7=int(FILA7.cget("text"))
        if fa1==0:
            try: L.remove(1)
            except ValueError: pass
        if fa2==0:
            try: L.remove(2)
            except ValueError: pass
        if fa3==0:
            try: L.remove(3)
            except ValueError: pass
        if fa4==0:
            try: L.remove(4)
            except ValueError: pass
        if fa5==0:
            try: L.remove(5)
            except ValueError: pass
        if fa6==0:
            try: L.remove(6)
            except ValueError: pass
        if fa7==0:
            try: L.remove(7)
            except ValueError: pass
        i=len(L)
        if fa5==1: b5.config(state=DISABLED)
        if jugador.cget("text")==txtj1:
            c.create_oval(d*4,d*(fa5-1),d*5,d*fa5,fill="green")
            tablero[4][fa5-1]=1
            if t.ganaono(1): t.nombrarganador("Gana "+str(j1.get()))
            jug=txtc
            jugador.config(text=jug)
        FILA5.config(text=str(fa5-1))
        cl=random.randint(1,i)
        colcpu=L[cl-1]
        if colcpu==1: fa=int(FILA1.cget("text"));FILA=FILA1;b=b1
        elif colcpu==2: fa=int(FILA2.cget("text"));FILA=FILA2;b=b2
        elif colcpu==3: fa=int(FILA3.cget("text"));FILA=FILA3;b=b3
        elif colcpu==4: fa=int(FILA4.cget("text"));FILA=FILA4;b=b4
        elif colcpu==5: fa=int(FILA5.cget("text"));FILA=FILA5;b=b5
        elif colcpu==6: fa=int(FILA6.cget("text"));FILA=FILA6;b=b6
        else: fa=int(FILA7.cget("text"));FILA=FILA7;b=b7
        c.create_oval(d*(colcpu-1),d*(fa-1),d*colcpu,d*fa,fill="yellow")
        tablero[colcpu-1][fa-1]=2
        if tablero[colcpu-1][0]!=0: b.config(state=DISABLED)
        if t.ganaono(2): t.nombrarganador("Gana CPU")
        jug=txtj1
        jugador.config(text=jug)
        FILA.config(text=str(fa-1))
    def columna6():
        fa1=int(FILA1.cget("text"))
        fa2=int(FILA2.cget("text"))
        fa3=int(FILA3.cget("text"))
        fa4=int(FILA4.cget("text"))
        fa5=int(FILA5.cget("text"))
        fa6=int(FILA6.cget("text"))
        fa7=int(FILA7.cget("text"))
        if fa1==0:
            try: L.remove(1)
            except ValueError: pass
        if fa2==0:
            try: L.remove(2)
            except ValueError: pass
        if fa3==0:
            try: L.remove(3)
            except ValueError: pass
        if fa4==0:
            try: L.remove(4)
            except ValueError: pass
        if fa5==0:
            try: L.remove(5)
            except ValueError: pass
        if fa6==0:
            try: L.remove(6)
            except ValueError: pass
        if fa7==0:
            try: L.remove(7)
            except ValueError: pass
        i=len(L)
        if fa6==1: b6.config(state=DISABLED)
        if jugador.cget("text")==txtj1:
            c.create_oval(d*5,d*(fa6-1),d*6,d*fa6,fill="green")
            tablero[5][fa6-1]=1
            if t.ganaono(1): t.nombrarganador("Gana "+str(j1.get()))
            jug=txtc
            jugador.config(text=jug)
        FILA6.config(text=str(fa6-1))
        cl=random.randint(1,i)
        colcpu=L[cl-1]
        if colcpu==1: fa=int(FILA1.cget("text"));FILA=FILA1;b=b1
        elif colcpu==2: fa=int(FILA2.cget("text"));FILA=FILA2;b=b2
        elif colcpu==3: fa=int(FILA3.cget("text"));FILA=FILA3;b=b3
        elif colcpu==4: fa=int(FILA4.cget("text"));FILA=FILA4;b=b4
        elif colcpu==5: fa=int(FILA5.cget("text"));FILA=FILA5;b=b5
        elif colcpu==6: fa=int(FILA6.cget("text"));FILA=FILA6;b=b6
        else: fa=int(FILA7.cget("text"));FILA=FILA7;b=b7
        c.create_oval(d*(colcpu-1),d*(fa-1),d*colcpu,d*fa,fill="yellow")
        tablero[colcpu-1][fa-1]=2
        if tablero[colcpu-1][0]!=0: b.config(state=DISABLED)
        if t.ganaono(2): t.nombrarganador("Gana CPU")
        jug=txtj1
        jugador.config(text=jug)
        FILA.config(text=str(fa-1))
    def columna7():
        fa1=int(FILA1.cget("text"))
        fa2=int(FILA2.cget("text"))
        fa3=int(FILA3.cget("text"))
        fa4=int(FILA4.cget("text"))
        fa5=int(FILA5.cget("text"))
        fa6=int(FILA6.cget("text"))
        fa7=int(FILA7.cget("text"))
        if fa1==0:
            try: L.remove(1)
            except ValueError: pass
        if fa2==0:
            try: L.remove(2)
            except ValueError: pass
        if fa3==0:
            try: L.remove(3)
            except ValueError: pass
        if fa4==0:
            try: L.remove(4)
            except ValueError: pass
        if fa5==0:
            try: L.remove(5)
            except ValueError: pass
        if fa6==0:
            try: L.remove(6)
            except ValueError: pass
        if fa7==0:
            try: L.remove(7)
            except ValueError: pass
        i=len(L)
        if fa7==1: b7.config(state=DISABLED)
        if jugador.cget("text")==txtj1:
            c.create_oval(d*6,d*(fa7-1),d*7,d*fa7,fill="green")
            tablero[6][fa7-1]=1
            if t.ganaono(1): t.nombrarganador("Gana "+str(j1.get()))
            jug=txtc
            jugador.config(text=jug)
        FILA7.config(text=str(fa7-1))
        cl=random.randint(1,i)
        colcpu=L[cl-1]
        if colcpu==1: fa=int(FILA1.cget("text"));FILA=FILA1;b=b1
        elif colcpu==2: fa=int(FILA2.cget("text"));FILA=FILA2;b=b2
        elif colcpu==3: fa=int(FILA3.cget("text"));FILA=FILA3;b=b3
        elif colcpu==4: fa=int(FILA4.cget("text"));FILA=FILA4;b=b4
        elif colcpu==5: fa=int(FILA5.cget("text"));FILA=FILA5;b=b5
        elif colcpu==6: fa=int(FILA6.cget("text"));FILA=FILA6;b=b6
        else: fa=int(FILA7.cget("text"));FILA=FILA7;b=b7
        c.create_oval(d*(colcpu-1),d*(fa-1),d*colcpu,d*fa,fill="yellow")
        tablero[colcpu-1][fa-1]=2
        if tablero[colcpu-1][0]!=0: b.config(state=DISABLED)
        if t.ganaono(2): t.nombrarganador("Gana CPU")
        jug=txtj1
        jugador.config(text=jug)
        FILA.config(text=str(fa-1))
    v = Tk()
    v.title("Conecta 4")
    jugador = Label(v, text=jug)
    FILA1=Label(v,text="6")
    FILA2=Label(v,text="6")
    FILA3=Label(v,text="6")
    FILA4=Label(v,text="6")
    FILA5=Label(v,text="6")
    FILA6=Label(v,text="6")
    FILA7=Label(v,text="6")
    jugador.pack()
    # marco 1 - botones
    f1 = Frame(v)
    f1.pack()
    b1 = Button(f1, text="C1", command=columna1, width=11)
    b2 = Button(f1, text="C2", command=columna2, width=11)
    b3 = Button(f1, text="C3", command=columna3, width=11)
    b4 = Button(f1, text="C4", command=columna4, width=11)
    b5 = Button(f1, text="C5", command=columna5, width=11)
    b6 = Button(f1, text="C6", command=columna6, width=11)
    b7 = Button(f1, text="C7", command=columna7, width=11)
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
def salir():
    b3=v0.destroy()
# interfaz de usuario
v0=Tk()
v0.title("Inicio")
m1=Frame(v0)
m2=Frame(v0)
m3=Frame(v0)
l1=Label(v0,text="BIENVENIDO   A   CONECTA   4")
l2=Label(v0,text="Nombres de los jugadores")
l3=Label(v0,text="Selecciona el modo de juego")
lj1=Label(m1,text="Jugador 1",width=18)
lj2=Label(m1,text="Jugador 2",width=18)
j1=Entry(m2)
j2=Entry(m2)
b1=Button(m3,text="Jugador v/s jugador",command=pvp,width=20)
b2=Button(m3,text="Jugador v/s CPU",command=pvcpu,width=20)
b3=Button(v0,text="Salir",command=salir)
l1.pack()
l2.pack()
m1.pack()
lj1.pack(side=LEFT)
lj2.pack()
m2.pack()
j1.pack(side=LEFT)
j2.pack()
l3.pack()
m3.pack()
b1.pack(side=LEFT)
b2.pack()
b3.pack()
v0.mainloop() # no se definieron más clases para crear fichas ya que requerían el mismo número de líneas o incluso más (no así el número de caractéres)
