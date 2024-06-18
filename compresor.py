import sys
import bitarray
import bitarray as bit

#verifica si el archivo esta en la lista
def estaEnLista(lista,a):
    for i in lista:
        if a==i:
            return False
    return True
#calcula la frecuencia en que aparece un caracter
def calcularFrecuencias(archivo,numero):
    listaFrecuencias = []
    listaVistos=[]
    cantidad=0
    for i in archivo:
        if estaEnLista(listaVistos,i):
            listaVistos.append(i)
            for j in range(numero):
                if i == archivo[j]:
                    cantidad+=1
            listaFrecuencias.append((i,cantidad))
            cantidad=0
    listaFrecuencias.sort(key=lambda x: x[1], reverse=True)
    return listaFrecuencias

#es para crear un subarbol
def arbol(lista,nodo="nose"):
    if lista==[]:
        return lista
    nodosIs=[]
    if nodo =="nose":
        if len(lista)==2:
            return ["nose",[lista[0][0],[],[]],[lista[1][0],[],[]]]
        nodosIs.append(lista[0])
        nodosIs.append(lista[1])
        lista=lista[2:]
        arbolG=["nose",arbol(nodosIs),arbol(lista)]
    else:
        arbolG=["nose",[nodo],arbol(lista)]
    return arbolG

#Crea el arbol de huff
def contruirArbol(frecuencias):
    frecuencias2=frecuencias[:]
    if len(frecuencias2)%2:
        arbolg=["nose",[frecuencias2[0][0],[],[]],arbol(frecuencias2[1:])]
    else:
        arbolg=["nose",[frecuencias2[0][0],[],[]],["nose",[frecuencias2[1][0],[],[]],arbol(frecuencias2[2:])]]
    return arbolg

#retorna una lista de tuplas con todos los caminos y con sus valores(nodo,recorrico)
def CaminosArbol(arbol,recorrido="",listaRecorrido=[]):
    if arbol==[]:
        return ""
    if arbol[1]==[] and arbol[2]==[]:
        listaRecorrido.append((arbol[0],recorrido)) 
        return listaRecorrido
    CaminosArbol(arbol[1],recorrido+'0',listaRecorrido)
    CaminosArbol(arbol[2],recorrido+'1',listaRecorrido)
    return listaRecorrido

def alturaArbol(arbol):
    if arbol==[]:
        return 0
    mx=-1
    mx=max(mx,(1+max(alturaArbol(arbol[1]),alturaArbol(arbol[2]))))
    return mx

def ListaNodosNivel ( arbol , nivel , i = 0) :
    if arbol ==[]:
        return []
    if i == nivel :
        return [ arbol [0]]
    return ListaNodosNivel ( arbol [1] , nivel , i +1) + ListaNodosNivel ( arbol [2] , nivel ,i +1)

def ListaArbol (arbol):
    h=alturaArbol(arbol)
    l=[]
    for i in range(h):
        l.append((ListaNodosNivel(arbol,i),i))
    l.sort(key=lambda x: x[1])
    return l

def archivoHuff(frecuencias,texto,nombreTXT):
    arbol = contruirArbol(frecuencias)
    TodosLosCaminos=CaminosArbol(arbol)
    bits=""
    for i in texto:
        for j in TodosLosCaminos:
            if i==j[0]:
                bits+=j[1]
                continue
    secuencia=bit.bitarray(bits)
    with open(nombreTXT+'.huff', 'wb') as bf:
        secuencia.tofile(bf)
    with open(nombreTXT+'.txt','w') as bf:
        bf.write(bits)
    return arbol, TodosLosCaminos

def archivoTable(frecuencias,normbreTxt,cantidad):
    nose=str(cantidad)+"\n"
    for i in frecuencias:
        nose += str(i[0]) + " " + str(i[1])+"\n"
    with open(normbreTxt+'.table','w') as bf:
        bf.write(nose)
    pass

def archivoStats(arbol,frecuencias,nombreTXT):
    altura=alturaArbol(arbol)
    listaDeNodos=ListaArbol(arbol)
    contenido=""
    contenido+= str(altura)+"\n"
    mx=([],0)
    for i in listaDeNodos:
        if len(mx[0]) < len(i[0]):
            mx=i
    contenido+=str(len(mx[0]))+"\n"
    contenido+=str(len(listaDeNodos))+" "
    for i in listaDeNodos:
        contenido+= str(len(i[0]))+" "
    contenido+="\n"
    for i in frecuencias:
        contenido+=str(i)+" "
    with open(nombreTXT+".stats","w") as bf:
        bf.write(contenido)
    pass

def main():
    if len(sys.argv) !=0 and len(sys.argv)>1 :
        with open(sys.argv[1],mode='rb') as file:
            fileContent = file.read()
        frecuencias = calcularFrecuencias(fileContent,len(fileContent))
        arbol, caminos = archivoHuff(frecuencias,fileContent,sys.argv[1])
        archivoTable(caminos,sys.argv[1],len(fileContent))
        archivoStats(arbol,frecuencias,sys.argv[1])
    else :
        print("El programa no tiene argumentos")
main()
