from escolhas import *

def print_doc(doc):
    for item in doc:
        print_list(item)

def create_list(tamanho):
    lista = []
    for i in range(tamanho):
        lista.append(' ')
    return lista

def print_list(lista):
    string = ''
    for i in lista:
        i = str(i)
        string += i
    print (string)

def inserir(lista, texto, inicio, final):
    j = 0
    for i in range(inicio, final):
        try:
            lista[i] = texto[j]
            j += 1
        except:
            break

def linha1(remetente, destinatario, data, hora,ocorr=0):
    linha = create_list(120)
    inserir(linha,'000',0,3)
    inserir(linha,remetente,3,38 )
    inserir(linha,destinatario, 38, 73 )
    inserir(linha,data, 73, 79)
    inserir(linha,hora, 79, 83)
    inserir(linha,'OCO', 83, 86)
    inserir(linha,data, 86, 90)
    inserir(linha,hora, 90, 94)
    linha[94]=ocorr
    return linha

def linha2(data, hora):
    linha = create_list(120)
    inserir(linha,'340',0,3)
    inserir(linha,'OCORR',3,8)
    inserir(linha,data,8,12 )
    inserir(linha,hora,12,16)
    linha[16] = 1
    return linha

doc = []
remetente = input('Insira o remetente: ')
destinatario = input('Insira o destinatario: ')
data = input('Insira a data: ')
hora = (input('Insira hora: '))
linha1(remetente, destinatario, data, hora)
doc.append(linha1(remetente, destinatario, data, hora))
doc.append(linha2(data, hora))

print_doc(doc)
