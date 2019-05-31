def LineaLimpia(lin,signos):
    for s in signos:
        lin=lin.replace(s," ")
    return lin
def npal(lin,palabra):
    n=0
    while palabra!=lin[n]:
        n+=1
    return n
signos=[".","…","...",";",":",",",'"',"¿","?","¡","!","(",")","/","{","}","*","[","]","|"]
mencod=""
while True:
    palabra=raw_input("Palabra?")
    if palabra=="Finfin":
        break
    a=open("Codebook.txt","r")
    nlin=1
    while nlin<=184:
        lin=a.readline()
        if lin=="\n":
            continue
        lin=(LineaLimpia(lin,signos)).split()
        if palabra in lin:
            break
        nlin+=1
    if palabra in lin:
        np=npal(lin,palabra)+1
        if mencod=="":
            mencod=str(nlin)+" "+str(np)
        else:
            mencod=mencod+"\n"+str(nlin)+" "+str(np)
    else:
        print "Palabra X no está en el libro"
    a.close()
print mencod

