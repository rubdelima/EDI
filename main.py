from escolhas import *

class Linha:
    def __init__(self,tamanho):
        self.lista = create_list(tamanho)

    def inserir(self, texto, inicio, final):
        j = 0
        for i in range(inicio, final):
            try:
                self.lista[i] = texto[j]
                j += 1
            except:
                break
    
    def inserir_pos(self, pos, item):
        self.lista[pos] = item
    
    def print(self):
        string = ''
        for i in self.lista:
            i = str(i)
            string += i
        print (string)
    
    def getLinha(self):
        return self.lista

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

def linha1(remetente, destinatario, data, hora):
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
    return linha.getLinha()

def linha2(data, hora):
    linha=Linha(120)
    linha.inserir('340',0,3)
    linha.inserir('OCORR',3,8)
    linha.inserir(data,8,12 )
    linha.inserir(hora,12,16)
    linha.inserir_pos(16,1)
    return linha.getLinha()

def linha3(cnpj, remetente):
    linha = Linha(120)
    linha.inserir('341',0,3)
    linha.inserir(cnpj,3,17)
    linha.inserir(remetente, 17,57)
    return linha.getLinha()

def linha4(cnpj, serienota, numeronota, ocorrencia, dataoco, horaoco, codigoobs, txt, dataage, horaage):
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
    return linha.getLinha()

def OCOOREN(remetente, destinatario, data, cnpj, serienota, ocorrencia, dataoco, horaoco, codigoobs, txt, dataage, horaage):
    doc = []
    doc.append(linha1(remetente, destinatario, data, hora))
    doc.append(linha2(data, hora))
    doc.append(linha3(cnpj, remetente))
    doc.append(linha4(cnpj, serienota, numeronota, ocorrencia, dataoco, horaoco, codigoobs, txt, dataage, horaage ))
    return doc

def DOCCOB():
    pass


remetente = input('Insira o remetente: ')
destinatario = input('Insira o destinatario: ')
data = input('Insira a data: ')
hora = (input('Insira hora: '))
cnpj = input('Insira o CNPJ: ')
serienota = input('Insira a série da nota fiscal:')
numeronota = input('Insira o número da nota fiscal:') 
ocorrencia = escolher()
if ocorrencia < 10:
    ocorrencia = f'0{ocorrencia}'
dataoco = input('Insira a data da ocorrência:')
horaoco = input(('Insira a hora da ocorrência:'))
codigoobs = escolher2()
codigoobs = f'0{codigoobs}'
txt = input('Insira o texto adicional:')
dataage = input('Insira a data de agendamento')
horaage = input('Insira a hora de agendamento')

doc_ocooren = OCOOREN(remetente, destinatario, data, cnpj, serienota, ocorrencia, dataoco, horaoco, codigoobs, txt, dataage,horaage)
print_doc(doc_ocooren)

doc2 = []


