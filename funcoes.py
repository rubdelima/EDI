#imports globias
from xml.dom import minidom
import os
from datetime import datetime

#inport de modulos
from escolhas import *


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

def imprimir(doc, arquivo=''):
    doc[0] = [str(x) for x in doc[0]]
    nome = ''.join(doc[0][83:95])
    if arquivo != '':
        nome += arquivo[0:-4]
    nome += '.txt'
    with open(nome, "w") as saida:
        for linha in doc:
            string = ''
            for car in linha:
                car = str(car)
                string += car
            print(string, file=saida)

def getItens(parametro):
    lista = [x for x in os.listdir() if x.endswith(parametro)]
    return lista

def print_itens(lista):
    for i in range(len(lista)):
        print(f'{i} - {lista[i]}')

def add_zero(numero):
    numero = f'0{numero}'
    return numero

def randon_data(data, hora):
    #convertendo os dados
    dia = int(data[0:2])
    mes = int(data[2:4])
    ano = int(data[4:])
    minuto = int(hora[2:])
    hora = int(hora[0:2])
    #efeito cascata
    minuto += 20
    if minuto//60 >0:
        hora += 1
    minuto = minuto%60
    if minuto < 10: minuto = add_zero(minuto)
    hora += 1
    if hora//18 > 0:
        dia +=1
    hora = hora % 18
    if hora < 8:
        hora += 8
    if hora < 10: hora = add_zero(hora)
    dia += 1
    if dia//30 > 0:
        mes += 1
    if mes // 12 > 12:
        ano += 1
    dia = dia % 30
    mes = mes % 12
    if dia <10: dia = add_zero(dia)
    if mes < 10: mes = add_zero(mes)
    return '{}{}{}'.format(dia,mes,ano), '{}{}'.format(hora, minuto)
