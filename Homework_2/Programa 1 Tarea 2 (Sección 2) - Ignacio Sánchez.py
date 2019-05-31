def LineaLimpia(lin,signos):
    for s in signos:
        lin=lin.replace(s," ")
    return lin
def Palabra(lin,n):
    lin=lin.split()
    if n>len(lin):
        return ""
    else:
        return lin[n-1]
signos=[".","…","...",";",":",",",'"',"¿","?","¡","!","(",")","/","{","}","*","[","]","|"]
men=""
while True:
    cod=raw_input("Codigo?")
    cod=cod.strip()
    if cod=="0 0":
        break
    b=cod.find(" ")
    nlin=int(cod[:(b+1)])
    n=int(cod[(b+1):(len(cod))])
    a=open("Codebook.txt","r")
    c=1
    while c<=nlin:
        lin=a.readline()
        if lin=="\n": #las lineas en blanco son \n
            continue
        c+=1
    lin=LineaLimpia(lin,signos)
    p=Palabra(lin,n)
    lin=lin.split()
    if men=="":
        men=p
    else:
        men=men+" "+p
print men
a.close()
