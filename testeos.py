from threading import local
from funcoes import *

def ordPaste(arquivo):
    local = os.getcwd()
    arquivos = getItens('.xml')
    for arquivo in arquivos:
        with open(arquivo, 'r') as a:
            i = a.read()
            i = i.splitlines()
            dataoco, horaoco= data_hora_xml(getTag('dhEmi', arquivo)[0])
            os.makedirs(f'{local}/{dataoco}/')
            return f'{local}/{dataoco}/'
