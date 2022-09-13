from funcoes import *
from ocoren import OCOREN
from escolhas import *
import time

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

arquivos = getItens('.xml')
hora_emi_doc = '0000'
for local_arch in arquivos:
    d, h = data_hora_aut()
    if h == hora_emi_doc:
        print('Espere um pouco...')
        while True:
            d, h = data_hora_aut()
            if h != hora_emi_doc:
                break
    
    #time.sleep(61)
    #local_arch = "CTe26220746811890000112570010000000051560636218-procCte.xml"
    '''
    #lista_arch = getItens('.xml')
    #print_itens(lista_arch)

    rem = (getTag('CNPJ', local_arch))
    print_itens(rem)
    print(rem)
    '''


    '''
    ## ocoren ##
    nome_remetente = getTag('xNome', local_arch)[1]
    nome_destinatario = (getTag('xNome', local_arch))[3]
    data_emi_doc, hora_emi_doc = data_hora_aut()
    cnpj_remetente = (getTag('CNPJ', local_arch))[1]
    cnpj_transp = '46811890000112'
    nome_transportadora = 'CSRG TRANSPORTES LTDA'
    serienota = (getTag('serie', local_arch))[0]
    numeronota = (getTag('cCT', local_arch))[0]
    ocorrencia = escolher(True)
    dataoco, horaoco= data_hora_xml(getTag('dhEmi', local_arch)[0])
    oco = OCOREN(nome_remetente, nome_destinatario, nome_transportadora, data_emi_doc, hora_emi_doc, cnpj_remetente, cnpj_transp, serienota,numeronota, dataoco, horaoco)
    imprimir(oco.getDoc(), local_arch)
    '''


'''
DOCOB
    remetente = (getTag('xNome', local_arch))[1] 
    destinatario = (getTag('xNome', local_arch))[3]
    data , hora = data_hora_aut()
    cnpj = (getTag('CNPJ', local_arch))[1]
    serienota = (getTag('serie', local_arch))[0]
    numeronota = (getTag('cCT', local_arch))[0]
    ocorrencia = escolher(True)
    dataoco, horaoco= data_hora_xml(getTag('dhEmi', local_arch)[0])

##### Linha 4 #####

tipodoccobranca = '0'
filialemissor
numerocobranca
dataemi  = input('Insira a data da Emissão: ')
datavenci = input('Insira a data da Vencimento: ')
alterar_valor = False
alterar = not int(input('O valor é: '))
if alterar_valor:
    valordoccobranca = float(input('Insira a valor total da cobrança: '))
else:
    valordoccobranca = valor_do_mes

tipocobranca
valortotalicms = input('Insira a valor total do ICMS: ')
juros = int(input('Vai adicionar juros? '))
if juros:
    valorjurosdiatraso =  (input('Insira a valor total dos juros: '))

indetificacaoagentecobranca
numeroagenciabancaria
digitoverificadornumdaagencia
numerocontacorrente
digitoverificadorcontacorrente
acaododocumento = 'I'


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