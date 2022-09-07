from xml.dom import minidom
import os


def getItens(parametro):
    for x in os.listdir():
        lista = []
        if x.endswith(parametro): 
          lista.append(x)
    return lista


def getTag(string, local):
    lista = []
    with open(local, 'r', encoding='utf-8') as data:
        xml = minidom.parse(data)
        try:
            element = xml.getElementsByTagName(string)
            try:
                for i in range(100):
                    lista.append(element[i].firstChild.data)
            except:
                return lista
        except:
            return lista

def print_itens(lista):
    for i in range(len(lista)):
        print(f'{i} - {lista[i]}')


def data_hora(string):
    data , hora = string.split('T')
    data = data.split('-')
    data = ''.join(data)
    hora = hora.split(':')
    hora = ''.join(hora[0:1])
    return data, hora

def getNfe():
    pass


local_arch = "CTe26220846811890000112570010000000301684316300-procCte.xml"
local_arch2 = "CTe26220746811890000112570010000000051560636218-procCte.xml"
lista_arch = getItens('.xml')
print_itens(lista_arch)


rem = (getTag('chave', local_arch))
print_itens(rem)
print(rem)
'''
## ocoren ##
nome_remetente = (getTag('xNome', local_arch))[1] #ou sera da transportadora?
nome_destinatario = (getTag('xNome', local_arch))[3]
data_emi_doc, hora_emi_doc = data_hora((getTag('dhEmi', local_arch))[0])
cnpj_remetente = #ou sera da transportadora?
serienota = 
numeronota
ocorrencia
dataoco
horaoco
codigoobs
txt
dataage
horaage
'''

'''
DOCOB
remetente
destinatario
data
hora
cnpj
serienota
numeronota
ocorrencia
dataoco
horaoco
codigoobs
txt
dataage
horaage
'''