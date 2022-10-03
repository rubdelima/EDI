from tkinter import E
from docob import DOCOB
from ocoren import OCOREN
from funcoes import *

if __name__ == '__main__':
    arquivos = getItens('.xml')
    # Globais
    
    nomeRemetenteDOC = 'CSRG TRANSPORTES LTDA'
    
    cnpjTransport = '46811890000112'
    
    nomeDestinatarioDOC = input('Insira o nome do Destinatário do Documento: ')
    
    CNPJDestinatarioDOC = input('Insira o CNPJ do Destinatario: ')
    
    data, hora = data_hora_aut()
    
    numeroCobranca = input('Insira o número da cobrança: ')
    
    numeroCobranca = (10-len(list(numeroCobranca)))*'0' + numeroCobranca
    
    dataVencimento = input('Insira a data de vencimento: ')
    
    
    oco = OCOREN(nomeRemetenteDOC, nomeDestinatarioDOC, nomeRemetenteDOC, data, hora, cnpjTransport)
    
    cob = DOCOB()
    
    cob.linha1(nomeDestinatarioDOC, data, hora)
    
    cob.linha4(numeroCobranca, data, dataVencimento, '%%%%%%%%%%%%%%%' , '00000000000')
    
    valor_total = 0
    total_arquivos = 0
    EDIRETURN = []
    
    for local_arch in arquivos:
        try:
            #Dados Individuais
            serienota = (getTag('serie', local_arch))[0]
            numeronota = getTag('chCTe', local_arch)[0][-11:]
            dataoco, horaoco= data_hora_xml(getTag('dhEmi', local_arch)[0])
            pesonotaf = getTag('qCarga', local_arch)[0]
            valor_frete = (getTag('vRec', local_arch))[0]
            valor_carga = (getTag('vCarga', local_arch))[0]
            cte_serie = local_arch[25:28]
            cte = local_arch[33:37]
            nfe = getTag('chave', local_arch)[0][28:34]
            nome_destinatario = (getTag('xNome', local_arch))[3]
            print(f'Verifique os dados: Numero da Nota Fiscal {nfe} Valor do Frete: {valor_frete}')
            print(f'Valor Total da NF: {valor_carga}, Destinatário: {nome_destinatario}')
            dataEmissaoNF = input("Insira a data de emissão da NF: ")
            
            EDIRETURN.append((serienota, nfe, dataoco, horaoco, pesonotaf, valor_frete, valor_carga, cte, nfe, nome_destinatario, dataEmissaoNF))
            
            vez = 1
            for i in range(2):
                oco.linha4(CNPJDestinatarioDOC,serienota, nfe, dataoco, horaoco, vez)
                vez -= 1
            oco.linha5()
            cob.linha5(cte_serie, cte, valor_frete, dataoco, CNPJDestinatarioDOC)
            cob.linha6(nfe, dataEmissaoNF, pesonotaf, valor_carga)
            valor_total += float(valor_frete)
            total_arquivos += 1
            
        except:
            print(f'Houve um erro ao processar o arquivo: {local_arch}')
    
    cob.linha7(total_arquivos, valor_total)
    imprimir(oco.getDoc())
    imprimir(cob.getDoc())
    with open('EDIRETURN.txt', 'w') as saida:
        j = 0
        for i in EDIRETURN:
            print(f'ITEM {j}', file= saida)
            print(f'serienota {i[0]}\nnumeronota {i[1]}\ndataoco {i[2]}\nhoraoco {i[3]}\npesonotaf {i[4]}\nvalor_frete {i[5]}\nvalor_carga {i[6]}\ncte {i[7]}\nnfe {i[8]}\nnome_destinatario {i[9]}\ndataEmissaoNF {i[10]}', file =saida)
            print('__END__', file = saida)
            j += 1
