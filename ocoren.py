from linha import Linha
from funcoes import * 

class OCOREN:
    def __init__(self,remetente, destinatario, data, hora, cnpj, serienota,numeronota, dataoco, horaoco,):
        self.doc = []
        self.linha1(remetente, destinatario, data, hora)
        self.linha2(data, hora)
        self.linha3(cnpj, remetente)
        for i in range(2):
            self.linha4(cnpj, serienota, numeronota, dataoco, horaoco, i,)
            dataoco, horaoco = randon_data(dataoco, horaoco)
            
            

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

    def linha4(self,cnpj, serienota, numeronota, dataoco, horaoco, vez):
        linha = Linha(120)
        linha.inserir('342',0,3)
        linha.inserir(cnpj,3,17)
        linha.inserir(serienota, 17, 20)
        linha.inserir(numeronota, 20,28)
        ocorrencia = escolher(True, vez)
        linha.inserir(ocorrencia,28,30)
        linha.inserir(dataoco,30,38)
        linha.inserir(horaoco,38,42)
        codigo_obs = escolher2(True, False)
        linha.inserir(codigo_obs,42,44)
        txt = escolher5(dataoco, horaoco, True, vez)
        linha.inserir(txt,44,114)
        dataoco = dataoco[0:4] + dataoco[6:]
        linha.inserir(dataoco,114,122)
        linha.inserir(horaoco,122,126)
        self.doc.append(linha.getLinha())
        if vez ==1: self.swap()
    
    def swap(self):
        self.doc[len(self.doc)-1], self.doc[len(self.doc)-2] = self.doc[len(self.doc)-2], self.doc[len(self.doc)-1]
    
    def getDoc(self):
            return self.doc
