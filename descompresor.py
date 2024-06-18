import sys
import bitarray
import bitarray as bit

sys.setrecursionlimit(50000000)

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


def Conversor(arbol,arbolGrande,bits,cantidad,respuesta=""):
    if arbol==[]:
        return respuesta
    if cantidad==0:
        return respuesta
    if arbol[1]==[] and arbol[2]==[]:
        respuesta+=chr(arbol[0])
        return Conversor(arbolGrande,arbolGrande,bits,cantidad-1,respuesta)
    if bits[0]:
        return Conversor(arbol[2],arbolGrande,bits[1:],cantidad,respuesta)
    return Conversor(arbol[1],arbolGrande,bits[1:],cantidad,respuesta)

    

def ArchivoNuevo(NombreTXT,arbol,bits,cantidad):
    respuesta=""
    respuesta=Conversor(arbol,arbol,bits,cantidad)
    with open(NombreTXT,"w") as bf:
        bf.write(respuesta)
    pass
        

def main():
    if len(sys.argv)>=3:
        
        bits= bit.bitarray()
        with open(sys.argv[1], 'rb') as bf:
            bits.fromfile(bf)
        listaFrecuencias=[]
        cantidCarac=0
        with open(sys.argv[2], 'r') as nose:
            for i in nose:
                linea=tuple(i.strip().split())
                if len(linea)==1:
                    cantidCarac=int(linea[0])
                else:
                    listaFrecuencias.append((int(linea[0]),int(linea[1])))
        arbol=contruirArbol(listaFrecuencias,len(listaFrecuencias))
        ArchivoNuevo(sys.argv[3],arbol,bits,cantidCarac)  
    else :
        print("El programa no tiene los argumentos necesarios")
main()