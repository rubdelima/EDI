import os
def getItens(parametro):
    for x in os.listdir():
        lista = []
        if x.endswith("parametro"): 
          lista.append(x)
    return lista

