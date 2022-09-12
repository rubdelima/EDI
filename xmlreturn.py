from funcoes import *
from ocoren import OCOREN
from escolhas import *
import time

arquivos = getItens('.xml')
for local_arch in arquivos:
    #time.sleep(61)
    #local_arch = "CTe26220746811890000112570010000000051560636218-procCte.xml"
    '''
    #lista_arch = getItens('.xml')
    #print_itens(lista_arch)

    rem = (getTag('CNPJ', local_arch))
    print_itens(rem)
    print(rem)
    '''

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

    def data_hora_xml(string):
        data , hora = string.split('T')
        data = data.split('-')
        data = data[2] + data[1] + data[0]
        #data = ''.join(data)
        hora = hora.split(':')
        hora = ''.join(hora[0:2])
        return data, hora

    def data_hora_aut():
        a = datetime.now()
        a = str(a)
        data, hora = a.split(' ')
        data = data.split('-')
        data = f'{data[2]}{data[1]}{data[0][2:]}'
        hora = hora.split(':')
        hora = f'{hora[0]}{hora[1]}'
        return data, hora

    ## ocoren ##
    nome_remetente = getTag('xNome', local_arch)[1]
    nome_destinatario = (getTag('xNome', local_arch))[3]
    data_emi_doc, hora_emi_doc = data_hora_aut()
    cnpj_remetente = (getTag('CNPJ', local_arch))[1]
    serienota = (getTag('serie', local_arch))[0]
    numeronota = (getTag('cCT', local_arch))[0]
    ocorrencia = escolher(True)
    dataoco, horaoco= data_hora_xml(getTag('dhEmi', local_arch)[0])
    oco = OCOREN(nome_remetente, nome_destinatario, data_emi_doc, hora_emi_doc, cnpj_remetente, serienota,numeronota, dataoco, horaoco)
    imprimir(oco.getDoc(), local_arch)


# opcional codigoobs = escolher2()
#txt = escolher5()
#dataage = data_emi_doc, hora_emi_doc = data_hora_xml((getTag('dhEmi', local_arch))[0])
#horaage = data_emi_doc, hora_emi_doc = data_hora_xml((getTag('dhEmi', local_arch))[0])


'''
DOCOB
remetente = (getTag('xNome', local_arch))[1] 
destinatario = (getTag('xNome', local_arch))[3]
data = 
hora =
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