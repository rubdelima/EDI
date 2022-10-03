from linha import Linha
from escolhas import *
def format_2f(a):
    a = str(format(float(a), ".2f"))
    a = list(a)
    a.remove(".")
    a = ''.join(a)
    return a

class DOCOB:
    def __init__(self):
        self.doc = []

    def linha1(self, destinatario, data, hora):
        linha = Linha(170)
        linha.inserir('000', 0, 3)
        linha.inserir('CSRG TRANSPORTES LTDA', 3, 38)
        linha.inserir(destinatario, 38, 73)
        linha.inserir(data, 73, 79)
        linha.inserir(hora, 79, 83)
        linha.inserir('COB', 83, 86)
        linha.inserir(data, 86, 90)
        linha.inserir(hora, 90, 94)
        linha.inserir_pos(94, 0)
        self.doc.append(linha.getLinha())
        self.linha2(data, hora)
        

    def linha2(self, data, hora):
        linha = Linha(170)
        linha.inserir('350', 0, 3)
        linha.inserir('COBRA', 3, 8)
        linha.inserir(data, 8, 12)
        linha.inserir(hora, 12, 16)
        linha.inserir_pos(16, 1)
        self.doc.append(linha.getLinha())
        self.linha3()

    def linha3(self):
        linha = Linha(170)
        linha.inserir('351', 0, 3)
        linha.inserir('46811890000112', 3, 17)
        linha.inserir('CSRG TRANSPORTES LTDA', 17, 57)
        self.doc.append(linha.getLinha())
        self.doc.append([])

    def linha4(self, numerocobranca, dataemi, datavenci, valordoccobranca,valortotalicms):
        linha = Linha(170)
        linha.inserir('352', 0, 3)
        linha.inserir('46811890000112', 3, 13)
        linha.inserir('0', 13, 14)
        linha.inserir(numerocobranca, 17, 27)
        linha.inserir(dataemi, 27, 35)
        linha.inserir(datavenci, 35, 43)
        linha.inserir(valordoccobranca, 43, 58)
        linha.inserir('000', 58, 61)
        
        linha.inserir_fim(format_2f(valortotalicms), 61, 76)
        linha.inserir('Cora SCD - 403', 114, 149)
        linha.inserir('0001', 149, 153)
        linha.inserir("1", 153, 154)
        linha.inserir('2666201', 154, 165)
        linha.inserir('8', 164, 166)
        linha.inserir('I', 166, 167)
        self.doc[3] = linha.getLinha()
        

    def linha5(self,cte_serie, cte, valorfrete, dataemi, cnpj_rem_nf):
        linha = Linha(170)
        linha.inserir('353', 0, 3)
        linha.inserir('46811890000112', 3, 13)
        linha.inserir(cte_serie, 13,18)
        linha.inserir_fim(cte, 18, 30)
        valorfrete = format_2f(valorfrete)
        linha.inserir_fim(valorfrete, 30, 45)
        linha.inserir(dataemi, 45,53)
        linha.inserir_fim(cnpj_rem_nf, 53,67)
        #linha.inserir_fim(cnpj_dest_nf, 67, 81)
        linha.inserir('46811890000112', 81,95)
        self.doc.append(linha.getLinha())

    def linha6(self, numeronotafiscal, dataemi, pesonotaf, valormercadoria):
        linha = Linha(170)
        linha.inserir('354', 0, 3)
        linha.inserir_fim(numeronotafiscal, 6, 14)
        linha.inserir(dataemi, 14, 22)
        linha.inserir_fim(format_2f(pesonotaf), 22, 29)
        linha.inserir_fim(format_2f(valormercadoria), 29, 44)
        self.doc.append(linha.getLinha())

    def linha7(self, quant_itens, valor_total):
        linha = Linha(170)
        linha.inserir('355', 0, 3)
        linha.inserir_fim(quant_itens, 3, 7)
        linha.inserir_fim(valor_total, 7, 22)
        self.doc.append(linha.getLinha())

    def getDoc(self):
        return self.doc
