print """
                            Tareas para ejecución
                  
1: Agregar datos de tenista
2: Borrar datos de tenista
3: Lista tenistas ordenados por ranking ATP y orden alfabético
4: Salir
"""
class Nodo:
    def __init__(self,t,u,v,w,x,y,z):
        self.pl1=t
        self.pl2=u
        self.ap=v
        self.nom=w
        self.fecha=x
        self.pais=y
        self.rank=z
        self.valores=(v,w,x,y,z)
class Full(Exception):
    def __init__(self): pass
class Vacia(Exception):
    def __init__(self): pass
class Existe(Exception):
    def __init__(self): pass
class Noexiste(Exception):
    def __init__(self): pass
class Tenista:
    def __init__(self):
        self.primero=None
        self.ATP=None 
        self.alfa=None
    def agregar(self,x): #crear 1ro para lista 1 y lista 2
        if existe(x,self.primero):
            raise Existe()
        try:
            if self.primero==None:
                self.primero=Nodo(self.ATP,self.alfa,x[0],x[1],x[2],x[3],x[4])
            else:
                primero=self.primero
                if x[0]<self.primero.ap:#
                    if x[3]>self.primero.pais:
                        self.alfa=primero
                        self.primero=Nodo(self.ATP,self.alfa,x[0],x[1],x[2],x[3],x[4])
                        self.primero.pl1,primero.pl1=primero.pl1,self.primero
                    elif x[3]<self.primero.pais:#
                        self.ATP=primero
                        self.alfa=primero
                        self.primero=Nodo(self.ATP,self.alfa,x[0],x[1],x[2],x[3],x[4])   
                elif x[0]>self.primero.ap or (x[0]==self.primero.ap and x[1]>self.primero.nom):
                    if x[3]>self.primero.pais:
                        self.primero=Nodo(self.ATP,self.alfa,x[0],x[1],x[2],x[3],x[4])
                        self.primero.pl2,primero.pl2=primero.pl2,self.primero
                        self.primero.pl1,primero.pl1=primero.pl1,self.primero
                        self.primero=primero 
                    elif x[3]<self.primero.pais:
                        self.ATP=primero
                        self.primero=Nodo(self.ATP,self.alfa,x[0],x[1],x[2],x[3],x[4])
                        self.primero.pl2,primero.pl2=primero.pl2,self.primero
                        self.primero=primero        
            print "Información de jugador ingresada con éxito"
        except MemoryError:
            raise Full()         
    def borrar(self,x): #unir anterior al borrado y sgte
        if self.primero==None:
            raise Vacia()
        elif noexiste(x,self.primero):
            raise Noexiste()
        else:
            s1=self.primero
            s2=self.primero
            bckup=self.primero
            m=0
            while s1!=None:
                if s1.ap==x[0] and s1.nom==x[1]:
                    break
                s1=s1.pl1
                m+=1
            for i in range(m-1):
                self.primero=self.primero.pl1
            self.primero.pl1=s1.pl1
            self.primero=bckup
            n=0
            while s2!=None:
                if s2.ap==x[0] and s2.nom==x[1]:
                    break
                s2=s2.pl2
                n+=1
            for i in range(n-1):
                self.primero=self.primero.pl2
            self.primero.pl2=s2.pl2
            self.primero=bckup
            if n==0 or m==0: #es lo mismo
                self.primero=self.primero.pl2
            print "Información de jugador eliminada con éxito"
    def mostrarlistas(self):
        pri=self.primero
        print "Lista ordenada según ranking ATP:"
        while pri!=None:
            print pri.ap,pri.nom,pri.fecha,pri.pais,pri.rank
            pri=pri.pl1
        pri=self.primero
        print "Lista ordenada alfabéticamente:"
        while pri!=None:
            print pri.ap,pri.nom,pri.fecha,pri.pais,pri.rank
            pri=pri.pl2
    global existe
    def existe(x,y): #si existe en 1 lista existe en la otra (lo mismo en noexiste)
        r=y
        while r!=None:
            if x[0]==r.ap and x[1]==r.nom:
                return True
            r=r.pl2
        return False
    global noexiste
    def noexiste(x,y):
        r=y
        while r!=None:
            if x[0]==r.ap and x[1]==r.nom:
                return False
            r=r.pl2
        return True
ten=Tenista()
while True:
    r=input(">")
    if r==1:
        info=raw_input("Información tenista?").split()
        try:
            ten.agregar(info)
        except Full:
            print "No hay espacio suficiente en la memoria"
        except Existe:
            print "Nombre ya existe"              
    elif r==2:
        nombre=raw_input("Nombre tenista?").split()
        try:
            ten.borrar(nombre)
        except Vacia:
            print "Lista vacía"
        except Noexiste:
            print "Nombre no existe"
    elif r==3: ten.mostrarlistas()
    elif r==4: break
    else: print "Tarea a ejecutar no existe, introduzca valores válidos"
