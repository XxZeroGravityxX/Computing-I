from Tkinter import *
class Conjunto:
    def __init__(self,s):
        self.s=str(s)
    def vacio(self):
        return self.s=="" 
    def union(self,x):
        uni=(self.s).strip()
        for c in str(x):
            if (self.s).find(c)==-1:
                uni+=c
        if uni=="" and self.s=="":
            return "Vacío"
        return uni     
    def interseccion(self,x):
        inter=""
        for c in str(x):
            if (self.s).find(c)!=-1:
                inter=inter+c
        if inter=="":
            return "Vacío"
        else:
            return inter
    def __str__(self):
        b=""
        for m in self.s:
            if b=="":
                b=m
            else:
                b=b+" "+m
        return b
def unir():
    x=con1.get()
    y=con2.get()
    rc1=Conjunto(x)
    rc2=Conjunto(y)
    ru=rc1.union(rc2)
    txt.config(text=ru)
def intersectar():
    x=con1.get()
    y=con2.get()
    rc1=Conjunto(x)
    rc2=Conjunto(y)
    if rc1.vacio() or rc2.vacio():
        txt.config(text="Vacío")
    else:
        ri=rc1.interseccion(rc2)
        txt.config(text=ri)
def salir():
    salir=v.destroy()
v=Tk()
v.title("Conjuntos")
marco0=Frame(v)
marco1=Frame(v)
marco2=Frame(v)
marco0.pack()
marco1.pack()
marco2.pack()
con1=Entry(marco1)
con2=Entry(marco1)
con1.pack(side=LEFT)
con2.pack()
u=Button(marco2,text="Unión",command=unir)
i=Button(marco2,text="Intersección",command=intersectar)
u.pack(side=LEFT)
i.pack()
txt=Label(v,text="")
txt.pack()
t1=Label(marco0,text="Conjunto 1")
t2=Label(marco0,text="Conjunto 2")
t1.pack(side=LEFT)
t2.pack()
salir=Button(v,text="Salir",command=salir)
salir.pack()
v.mainloop()
