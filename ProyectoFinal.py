import sys
sys.setrecursionlimit(500000000)
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


def contruirArbol(frecuencias):
    frecuencias.sort(key=lambda x: x[1], reverse=True)
    frecuencias2=frecuencias[:]
    if len(frecuencias2)%2:
        arbolg=["nose",[frecuencias2[0][0],[],[]],arbol(frecuencias2[1:])]
    else:
        arbolg=["nose",[frecuencias2[0][0],[],[]],["nose",[frecuencias2[1][0],[],[]],arbol(frecuencias2[2:])]]
    return arbolg

def recorrerarbol(arbol,recorrido="",listaRecorrido=[]):
    if arbol==[]:
        return ""
    if arbol[1]==[] and arbol[2]==[]:
        listaRecorrido.append((recorrido,arbol[0])) 
        return listaRecorrido
    recorrerarbol(arbol[1],recorrido+'0',listaRecorrido)
    recorrerarbol(arbol[2],recorrido+'1',listaRecorrido)
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

def busquedaNivelAncho ( arbol ):
    h=alturaArbol (arbol)
    anchoMax =0
    nivel =0
    l2=[]
    l =[]
    while h >=0:
        l= ListaNodosNivel ( arbol ,h)
        if anchoMax < len (l):
            anchoMax = len ( l)
            nivel =h
        h -=1
    return nivel

def cantidadNodosPorNivel(arbol):

    pass

arbol=contruirArbol([('A', 2), ('B', 1), ('C', 1), ('D', 1), ('E', 1), ('F', 1), ('G', 1), ('H', 1)])
arbol2=['nose', ['A', [], []], ['nose', ['B', [], []], ['nose', ['nose', ['C', [], []], ['D', [], []]], ['nose', ['nose', ['E', [], []], ['F', [], []]], ['nose', ['G', [], []], ['H', [], []]]]]]]
print(busquedaNivelAncho(arbol2))
#print(recorrerarbol(arbol))
#######################
import sys
import bitarray
import bitarray as bit

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
def contruirArbol(frecuencias,cantidad):
    frecuencias2=frecuencias[:]
    if cantidad%2:
        arbolg=["nose",[frecuencias2[0][0],[],[]],arbol(frecuencias2[1:])]
    else:
        arbolg=["nose",[frecuencias2[0][0],[],[]],["nose",[frecuencias2[1][0],[],[]],arbol(frecuencias2[2:])]]
    return arbolg

def main():
    if len(sys.argv) !=0 and len(sys.argv)>=3:
        
        bits= bit.bitarray()
        with open('nose.txt.huff', 'rb') as bf:
            bits.fromfile(bf)

        altura=int(input())
        ancho=int(input())
        Li = list(map(int, input().split()))
        cantidadNodos=int(input())
        ListaFrecuencias=[]
        for i in range(cantidadNodos):
            n,f = map(int, input().split())
            ListaFrecuencias.append((n,f))
        arbol=contruirArbol(ListaFrecuencias)

def Conversor(arbol,arbolGrande,bits,respuesta=""):
    if arbol==[]:
        return respuesta
    if bits==[]:
        return respuesta
    caracter=""
    if arbol[1]==[] and arbol[2]==[]:
        respuesta+=chr(arbol[0])
        return Conversor(arbolGrande,arbolGrande,bits[1:],respuesta)
    if bits[0]:
        return Conversor(arbol[2],arbolGrande,bits[1:],respuesta)
    return Conversor(arbol[1],arbolGrande,bits[1:],respuesta)

    

def ArchivoNuevo(NombreTXT,arbol,bits):
    respuesta=""
    respuesta=Conversor(arbol,arbol,bits)
    with open(NombreTXT,"w") as bf:
        bf.write(respuesta)
    pass

    bits= bit.bitarray()
    with open('nose.txt.huff', 'rb') as bf:
        bits.fromfile(bf)
    print(bits)