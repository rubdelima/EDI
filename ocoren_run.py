from funcoes import *
from ocoren import OCOREN

manual = int(input('De que forma deseja realizar o procedimento?\n 0. Automatica\n 1. Manual\n'))
if manual:
    print('Ainda não foi feito')
else:
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
        
        lista_txt_return = []

        nome_remetente = getTag('xNome', local_arch)[1]

        nome_destinatario = (getTag('xNome', local_arch))[3]

        data_emi_doc, hora_emi_doc = data_hora_aut()

        cnpj_remetente = (getTag('CNPJ', local_arch))[1]

        cnpj_transp = '46811890000112'

        nome_transportadora = 'CSRG TRANSPORTES LTDA'

        serienota = (getTag('serie', local_arch))[0]
        
        numeronota = getTag('chCTe', local_arch)[0][-11:]

        ocorrencia = escolher(True)

        dataoco, horaoco= data_hora_xml(getTag('dhEmi', local_arch)[0])

        oco = OCOREN(nome_remetente, nome_destinatario, nome_transportadora, data_emi_doc, hora_emi_doc, cnpj_remetente, cnpj_transp, serienota,numeronota, dataoco, horaoco)

        imprimir(oco.getDoc(), local_arch)

        valor_frete = (getTag('vRec', local_arch))[0]
        cte = getTag('cCT', local_arch)[0]
        valor_carga = (getTag('vCarga', local_arch))[0]
        nfe = getTag('chave', local_arch)[0][28:34]
        pesonotaf = getTag('qCarga', local_arch)[0]
        lista_txt_return.append(nome_remetente)
        lista_txt_return.append(cnpj_remetente)
        lista_txt_return.append(nome_destinatario)
        lista_txt_return.append(numeronota)
        lista_txt_return.append(valor_frete)
        lista_txt_return.append(cte)
        lista_txt_return.append(pesonotaf)
        lista_txt_return.append(nfe)
        lista_txt_return.append(valor_carga)
        print_txtReturn(lista_txt_return, local_arch, oco.getDoc())
        #move_emi()
        #except:
            #print(f'Houve um erro ao tentar processar o arquivo {local_arch}')
        print_posicao(arquivos, local_arch)

print('TUDO PRONTO')