from linha import Linha
from escolhas import *

class DOCOB:
    def __init__(self,remetente, destinatario, data, hora, cnpj, serienota,numeronota, ocorrencia, dataoco, horaoco, codigoobs, txt, dataage, horaage):
        self.doc = []
        self.linha1(remetente, destinatario, data, hora)
        self.linha2(data, hora)
        self.linha3(cnpj, remetente)
        continuar = True
        while continuar: 
            self.linha4(cnpj, serienota, numeronota, ocorrencia, dataoco, horaoco, codigoobs, txt, dataage, horaage)
            continuar = int(input('Deseja adicionar mais uma linha? 0/1'))

    def linha1(self,remetente, destinatario, data, hora):
        linha = Linha(170)
        linha.inserir('000',0,3)
        linha.inserir(remetente,3,38 )
        linha.inserir(destinatario, 38, 73 )
        linha.inserir(data, 73, 79)
        linha.inserir(hora, 79, 83)
        linha.inserir('COB', 83, 86)
        linha.inserir(data, 86, 90)
        linha.inserir(hora, 90, 94)
        linha.inserir_pos(94,0)
        self.doc.append(linha.getLinha())

    def linha2(self,data, hora):
        linha=Linha(170)
        linha.inserir('350',0,3)
        linha.inserir('OCORR',3,8)
        linha.inserir(data,8,12 )
        linha.inserir(hora,12,16)
        linha.inserir_pos(16,1)
        self.doc.append(linha.getLinha())

    def linha3(self,cnpj, remetente):
        linha = Linha(170)
        linha.inserir('351',0,3)
        linha.inserir(cnpj,3,17)
        linha.inserir(remetente, 17,57)
        self.doc.append(linha.getLinha())

    def linha4(self,tipodoccobranca,acaododocumento,filialemissor,seriecobranca,dataemi,datavenci,numerocobranca,
    valordoccobranca,tipocobranca,valortotalicms, valorjurosdiatraso,datalimitepagamentodesconto,valordesconto
    ,indetificacaoagentecobranca,numeroagenciabancaria,digitoverificadornumdaagencia,numerocontacorrente,digitoverificadorcontacorrente   ):
        linha = Linha(170)
        linha.inserir('352',0,3)
        linha.inserir(filialemissor,3,13)
        linha.inserir(tipodoccobranca, 13, 14)
        linha.inserir(seriecobranca, 14,17)
        linha.inserir(numerocobranca,17,27)
        linha.inserir(dataemi,27,35)
        linha.inserir(datavenci,35,43)
        linha.inserir(valordoccobranca,43,58)
        linha.inserir(tipocobranca,58,61)
        linha.inserir(valortotalicms,61,76)
        linha.inserir(valorjurosdiatraso,76,91)
        linha.inserir(datalimitepagamentodesconto, 91, 99)
        linha.inserir(valordesconto,99,114)
        linha.inserir(indetificacaoagentecobranca,114,149)
        linha.inserir(numeroagenciabancaria,149,153)
        linha.inserir(digitoverificadornumdaagencia,153,154)
        linha.inserir(numerocontacorrente,154,165)
        linha.inserir(digitoverificadorcontacorrente,164,166)
        linha.inserir(acaododocumento)
        self.doc.append(linha.getLinha())
    def linha5(self,filialemissor,serieconhecimento,numeroconhecimento,valorfrete,dataemissaoconhecimento
    ,cnpjremetente, cnpjdestinatario,cnpjemissorconhecimento ):
        linha = Linha(170)
        linha.inserir('353',0,3)
        linha.inserir(filialemissor,3,13)
        linha.inserir(serieconhecimento,13,18)
        linha.inserir(numeroconhecimento,18,30)
        linha.inserir(valorfrete,30,45)
        linha.inserir(dataemissaoconhecimento,45,53)
        linha.inserir(cnpjremetente,53,67)
        linha.inserir(cnpjdestinatario,67,81)
        linha.inserir(cnpjemissorconhecimento,81,95)
        self.doc.append(linha.getLinha())
    def linha6(serie,numeronotafiscal,dataemi,pesonotaf,valormercadoria,cnpjemissor,self):
        linha = Linha(170)
        linha.inserir('354',0,3)
        linha.inserir(serie,3,6)
        linha.inserir(numeronotafiscal,6,15)
        linha.inserir(dataemi,15,22)
        linha.inserir(pesonotaf,22,29)
        linha.inserir(valormercadoria,29,44)
        linha.inserir(cnpjemissor,44,58)
        self.doc.append(linha.getLinha())
     def linha7(quantidadetotaldoccobranca,self,valortotaldoccobranca):
        linha = Linha(170)
        linha.inserir('355',0,3)
        linha.inserir(quantidadetotaldoccobranca,3,7)
        linha.inserir(valortotaldoccobranca,7,22)
        self.doc.append(linha.getLinha())
     def getDoc(self):
            return self.doc
'''Eu não sei o que é filial emissora do documento vulgo filialemissor'''