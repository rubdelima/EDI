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

lista_de_txt = ['Saída para Entrega', 'Entrega Realizada', 'Entrega não Realizada']

local_arch = "CTe26220746811890000112570010000000051560636218-procCte.xml"
#lista_arch = getItens('.xml')
#print_itens(lista_arch)


rem = (getTag('CNPJ', local_arch))
print_itens(rem)
print(rem)
'''
## ocoren ##
nome_remetente = (getTag('xNome', local_arch))[1]
nome_destinatario = (getTag('xNome', local_arch))[3]
data_emi_doc, hora_emi_doc = data_hora((getTag('dhEmi', local_arch))[0])
cnpj_remetente = (getTag('CNPJ', local_arch))[1]
serienota = (getTag('serie', local_arch))[0]
numeronota = (getTag('cCT', local_arch))[0]
ocorrencia = escolher1
dataoco = (getTag('dhEmi', local_arch))
horaoco = (getTag('dhEmi', local_arch))
codigoobs = escolher2
txt = lista_de_txt
dataage = 
horaage
'''

'''
DOCOB
remetente = (getTag('xNome', local_arch))[1] #ou sera da transportadora?
destinatario = (getTag('xNome', local_arch))[3]
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
filialemissor
tipodoccobranca
seriecobranca
numerocobranca
dataemi
datavenci
valordoccobranca
tipocobranca
valortotalicms
valorjurosdiatraso
datalimitepagamentodesconto
valordesconto
indetificacaoagentecobranca
numeroagenciabancaria
digitoverificadornumdaagencia
numerocontacorrente
digitoverificadorcontacorrente
acaododocumento
serieconhecimento
numeroconhecimento
valorfrete
dataemissaoconhecimento
cnpjremetente
cnpjdestinatario
cnpjemissorconhecimento
serie
numeronotafiscal
dataemi
pesonotaf
valormercadoria
cnpjemissor
quantidadetotaldoccobranca
valortotaldoccobranca
''' 