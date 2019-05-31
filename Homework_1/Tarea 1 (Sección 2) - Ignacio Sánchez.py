import math
def staylor(x):
    a=1
    b=3
    s=1.0/3
    n=1
    f=1
    while x>-1 and x<=1:
        y=((-x)**n)*s
        if abs(y)<0.0006:
            break
        f=f+y
        a+=3
        b+=3
        s=s*a/b 
        n+=1
    return f
while True:
    x=input("x = ")
    if x!=-1:
        rt=staylor(x)
        if x>-1:
            rm=math.pow(1+x,-1.0/3)
        if x<-1:
            rm=-math.pow(abs(1+x),-1.0/3)
        dif=rt-rm
        if x==999.9:
            break
        elif x<-1 or x>1: 
            print """    No se puede hacer c�lculo con este valor"""
        else:
            print """    Ra�z c�bica negativa de 1+x con serie de Taylor = """,rt
            print """    Ra�z c�bica negativa de 1+x usando math = """,rm
            print """    Diferencia = """,dif
    else:
        print """    No se puede hacer c�lculo con este valor""" #Seg�n la identaci�n del archivo PDF, los elementos deben imprimirse con esa identaci�n para el usuario
        
	
