from xml.dom import minidom
from math import *
from escolhas import *
from ocoren import OCOREN
from xmlreturn import *


def print_doc(doc):
    for item in doc:
        print_list(item)


def print_list(lista):
    string = ''
    for i in lista:
        i = str(i)
        string += i
    print(string)


def inserir(lista, texto, inicio, final):
    j = 0
    for i in range(inicio, final):
        try:
            lista[i] = texto[j]
            j += 1
        except:
            break


def imprimir(doc):
    nome = ''.join(doc[0][83:95])
    nome += '.txt'
    with open(nome, "w") as saida:
        for linha in doc:
            string = ''
            for car in linha:
                car = str(car)
                string += car
            print(string, file=saida)



'''
## Itens do OCOOREN ##
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
'''
## Itens do DOCOB ##
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



local_arch = "CTe26220846811890000112570010000000301684316300-procCte.xml"


'''


remetente = input('Insira o remetente: ')
destinatario = input('Insira o destinatario: ')
data = input('Insira a data: ')
hora = input('Insira hora: ')
cnpj = input('Insira o CNPJ: ')
serienota = input('Insira a série da nota fiscal:')
numeronota = input('Insira o número da nota fiscal:') 
ocorrencia = escolher()
if ocorrencia < 10:
    ocorrencia = f'0{ocorrencia}'
dataoco = input('Insira a data da ocorrência:')
horaoco = input(('Insira a hora da ocorrência:'))
codigoobs = escolher2()
codigoobs = f'0{codigoobs}'
txt = input('Insira o texto adicional:')
dataage = input('Insira a data de agendamento')
horaage = input('Insira a hora de agendamento')

doc_ocooren = OCOOREN(remetente, destinatario, data,hora, cnpj, serienota, ocorrencia, dataoco, horaoco, codigoobs, txt, dataage,horaage)
print_doc(doc_ocooren)

local_arch = input("Insira o local do arquivo: ")
'''


lista = getTag("xNome", local_arch)

print(lista)
