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
        linha = Linha(120)
        linha.inserir('000',0,3)
        linha.inserir(remetente,3,38 )
        linha.inserir(destinatario, 38, 73 )
        linha.inserir(data, 73, 79)
        linha.inserir(hora, 79, 83)
        linha.inserir('OCO', 83, 86)
        linha.inserir(data, 86, 90)
        linha.inserir(hora, 90, 94)
        linha.inserir_pos(94,0)
        self.doc.append(linha.getLinha())

    def linha2(self,data, hora):
        linha=Linha(120)
        linha.inserir('340',0,3)
        linha.inserir('OCORR',3,8)
        linha.inserir(data,8,12 )
        linha.inserir(hora,12,16)
        linha.inserir_pos(16,1)
        self.doc.append(linha.getLinha())

    def linha3(self,cnpj, remetente):
        linha = Linha(120)
        linha.inserir('341',0,3)
        linha.inserir(cnpj,3,17)
        linha.inserir(remetente, 17,57)
        self.doc.append(linha.getLinha())

    def linha4(self,cnpj, serienota, numeronota, ocorrencia, dataoco, horaoco, codigoobs, txt, dataage, horaage):
        linha = Linha(120)
        linha.inserir('342',0,3)
        linha.inserir(cnpj,3,17)
        linha.inserir(serienota, 17, 20)
        linha.inserir(numeronota, 20,28)
        linha.inserir(ocorrencia,28,30)
        linha.inserir(dataoco,30,38)
        linha.inserir(horaoco,38,42)
        linha.inserir(codigoobs,42,44)
        linha.inserir(txt,44,114)
        linha.inserir(dataage,114,122)
        linha.inserir(horaage,122,126)
        self.doc.append(linha.getLinha())
    
    def getDoc(self):
            return self.doc
