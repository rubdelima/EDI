#imports globais
from xml.dom import minidom #leitura de arquivos XML
import os #operações no SO
from datetime import datetime #receber o tempo
import shutil #mover arquivos
import csv
from csv import reader, writer #ler escrever arquivos csv
#inport de modulos
from escolhas import *

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
def print_posicao(lista, item):
    for i in range(len(lista)):
        if lista[i] == item:
            print(f'Item {i+1} de {len(lista)} concluído')
def print_txtReturn(lista, item, doc):
    doc[0] = [str(x) for x in doc[0]]
    nome = ''.join(doc[0][83:95])
    item = item[0:-4] + nome + 'TXTRETURN.txt'
    with open(item, "w") as saida:
        for i in lista:
            print(i, file=saida)
def print_doc(doc):
    for item in doc:
        print_list(item)
def print_list(lista):
    string = ''
    for i in lista:
        i = str(i)
        string += i
    print(string)
def inserir(lista, texto, inicio, final):
    j = 0
    for i in range(inicio, final):
        try:
            lista[i] = texto[j]
            j += 1
        except:
            break
def imprimir(doc, arquivo=''):
    doc[0] = [str(x) for x in doc[0]]
    nome = ''.join(doc[0][83:95])
    if arquivo != '':
        nome += arquivo[0:-4]
    nome += '.txt'
    with open(nome, "w") as saida:
        for linha in doc:
            string = ''
            for car in linha:
                car = str(car)
                string += car
            print(string, file=saida)
def getItens(parametro):
    lista = [x for x in os.listdir() if x.endswith(parametro)]
    return lista
def print_itens(lista):
    for i in range(len(lista)):
        print(f'{i} - {lista[i]}')
def add_zero(numero):
    numero = f'0{numero}'
    return numero
def randon_data(data, hora):
    #convertendo os dados
    dia = int(data[0:2])
    mes = int(data[2:4])
    ano = int(data[4:])
    minuto = int(hora[2:])
    hora = int(hora[0:2])
    #efeito cascata
    minuto += 20
    if minuto//60 >0:
        hora += 1
    minuto = minuto%60
    if minuto < 10: minuto = add_zero(minuto)
    hora += 1
    if hora//18 > 0:
        dia +=1
    hora = hora % 18
    if hora < 8:
        hora += 8
    if hora < 10: hora = add_zero(hora)
    dia += 1
    if dia//30 > 0:
        mes += 1
    if mes // 12 > 12:
        ano += 1
    dia = dia % 30
    mes = mes % 12
    if dia <10: dia = add_zero(dia)
    if mes < 10: mes = add_zero(mes)
    return '{}{}{}'.format(dia,mes,ano), '{}{}'.format(hora, minuto)
def find_dest(arquivo):
    local = os.getcwd()
    list_tuplC = getNFandValueCSV()
    with open(arquivo, 'r') as a:
        i = a.read()
        i = i.splitlines()
        inCSV = compare((i[-1],i[-2]), list_tuplC)
        if 'CPX' in i[0] and inCSV:
            return f'{local}/CPX/mest/'
        elif 'ITR' in i[0] and inCSV:
            return f'{local}/ITR/mest/'
        elif 'CPX' in i[0]:
            return f'{local}/CPX/'
        elif 'ITR' in i[0]:
            return f'{local}/ITR/'
def move_emi(comando='emi', ord=True):
    if comando == 'ord': ord = False
    lista_txtret = getItens('TXTRETURN.txt')
    lista_xml = getItens('.xml')
    lista_pdf = getItens('.pdf')
    lista_ocor = getItens('procCte.txt')
    for txtret in lista_txtret:
        try:
            if comando == 'emi':
                newDest = find_dest(txtret)
            if comando == 'ord' or ord:
                for i in lista_xml:
                    if txtret[36:46] in i:
                        dest = ordPaste(i, ord)
                        break
                if ord:
                    newDest += dest
                else:
                    newDest = dest
            try:
                os.makedirs(newDest)
            except:
                pass
            for xml in lista_xml:
                if txtret[36:46] in xml:
                    shutil.move(xml, newDest)
                    break
            for pdf in lista_pdf:
                if txtret[36:46] in pdf:
                    shutil.move(pdf, newDest)
                    break
            for oco in lista_ocor:
                if txtret[36:46] in oco:
                    shutil.move(oco, newDest)
                    break
            shutil.move(txtret, newDest)
        except:
            print(f'Houve um erro ao processar o arquivo {txtret}')
def getCSVlist(item=0, all=False):
    lista_csv = getItens('.csv')
    lista = []
    for csv in lista_csv:
        with open(csv, 'r') as csv_file:
            lista_aux = []
            csv_reader = reader(csv_file)
            list_of_rows = list(csv_reader)
            for  i in list_of_rows:
                lista_aux2 = []
                try:
                    i = i.split(';')
                except:
                    pass
                for j in i:
                    if len([h for h in j if h ==';']) != len(list(j)):
                        j = j.split(';')
                        j = [h for h in j if h != '']
                        if len(j) >= 1 :
                            lista_aux2.append(j)
                if len(lista_aux2) > 0:
                    lista_aux.append(lista_aux2)
            lista.append(lista_aux)
    if all:
        return lista
    else:
        return lista[item]
def removepont(string):
    string = str(string)
    string = string.split('.')
    string = ''.join(string)
    string = string.split('"')
    string = ''.join(string)
    return string
def getNFandValueCSV():
        lista_CSV = getCSVlist()
        lista_aux = []
        for i in range(len(lista_CSV)):
            try:
                tupla = (lista_CSV[i][0][0], removepont(lista_CSV[i][0][4]))
                lista_aux.append(tupla)
            except:
                pass
        return lista_aux
def compare(i, list_tuplC):
    for j in list_tuplC:
        if   j[1] in i[0] and j[0] in i[1]:
            return True
    return False
def ordPaste(arquivo, onlydata=False):
    local = os.getcwd()
    with open(arquivo, 'r') as a:
        i = a.read()
        i = i.splitlines()
        dataoco, horaoco= data_hora_xml(getTag('dhEmi', arquivo)[0])
        if onlydata:
            return f'/{dataoco}/'
        return f'{local}/{dataoco}/'
def findArchive(arquivo, lista_xml=[], lista_pdf=[], lista_ocor=[]):
    list_ret = []
    if len(lista_xml) > 0:
        for xml in lista_xml:
            if arquivo[36:46] in xml:
                list_ret.append(xml)
                break
    if len(lista_pdf) > 0:
        for pdf in lista_pdf:
            if arquivo[36:46] in pdf:
                list_ret.append(pdf)
                break
    if len(lista_ocor) > 0:
        for oco in lista_ocor:
            if arquivo[36:46] in oco:
                list_ret.append(oco)
                break
    return list_ret
def getInTXTRet(arquivo, posicao):
    with open(arquivo, 'r') as ar:
        a = ar.read()
        a = a.splitlines()
        return a[posicao]
def scanFrete():
    lista_txtret = getItens('TXTRETURN.txt')
    lista_xml = getItens('.xml')
    lista_pdf = getItens('.pdf')
    lista_ocor = getItens('procCte.txt')
    for arquivo in lista_txtret:
        xml, pdf, ocor = (findArchive(arquivo, lista_xml, lista_pdf, lista_ocor))
        valor_frete_xml = (getTag('vRec', xml))[0]
        valor_frete_txt = getInTXTRet(arquivo, 4)
        nfe_xml = getTag('chave', xml)[0][28:34]
        nfe_txt = getInTXTRet(arquivo, -2)
        if nfe_xml == nfe_txt and valor_frete_txt != valor_frete_xml:
            print("Um frete errado for encontrado no arquivo: %s" % nfe_xml)
def getTotalval():
    lista_xml = getItens('.xml')
    total = 0
    lista_erros = []
    for item in lista_xml:
        try:
            valor_frete = float((getTag('vRec', item))[0])
            total += valor_frete
        except:
            lista_erros.append(item)
    with open('relatorio.txt', 'w') as txr:
        print(f"O total dessa pasta é de R${total}", file=txr)
        if len(lista_erros) > 0:
            print('Os arquivos que tiveram falha foram os arquivos: ')
            for i in lista_erros:
                print(i, file=txr)
        
def findItem(sep_mes=False):
    tabela = [[] for i in range(319)]
    lista_txtret = getItens('TXTRETURN.txt')
    lista_xml = getItens('.xml')
    lista_pdf = getItens('.pdf')
    lista_ocor = getItens('procCte.txt')
    lista_csv = getNFandValueCSV()
    print(f'A Quantidade de txtret é {len(lista_txtret)}')
    print(f'A Quantidade de xml é {len(lista_xml)}')
    print(f'A Quantidade de pdf é {len(lista_pdf)}')
    print(f'A Quantidade de ocor é {len(lista_ocor)}')
    for item in lista_txtret:
        julho = False
        if len(tabela[int(item[34:37])]) == 0:
            tabela[int(item[34:37])].append(f'TXT ->{item[34:37]}')
            julho = False
            nf = getInTXTRet(item, 7)
            vt = getInTXTRet(item, 8)
            tabela[int(item[34:37])].append(nf)
            tabela[int(item[34:37])].append(vt)
            for csv in lista_csv:
                if csv[0] in nf and csv[1] in vt:
                    julho = True
                    break
            tabela[int(item[34:37])].append('Julho' if julho else 'Agosto')
        else:
            for rep in lista_ocor:
                if item[55:67] == rep[:12]:
                    repeted = f"{os.getcwd()}\\itensrepitidos/"
                    try:
                        os.makedirs(repeted)
                    except:
                        pass
                    shutil.move(rep, repeted)
                    shutil.move(item, repeted)
    
    for item in lista_xml:
        tabela[int(item[34:37])].append(f'XML ->{item[34:37]}')
    for item in lista_pdf:
        tabela[int(item[34:37])].append(f'PDF ->{item[34:37]}')
    for item in lista_ocor:
        tabela[int(item[46:49])].append(f'OCO->{item[46:49]}')
    
    if sep_mes:
        julho_paste = f"{os.getcwd()}/Julho"
        try:
            os.makedirs(julho_paste)
        except:
            pass
        for i in tabela:
            try:
                if i[3] == 'Julho':
                    lista = findConj(i[0][6:9])
                    for j in lista:
                        shutil.copy(j, julho_paste)
            except:
                pass
    
    lista_faltantes = []
    
    for i in range(len(tabela)):
        if len(tabela[i]) != 7:
            tabela[i].append(False)
            lista_faltantes.append(i)
        else:
            tabela[i].append(True)
        with open('resposta.txt', 'w') as saida:
            for line in tabela:
                print(*line, file=saida)
            print(*lista_faltantes, file=saida)
        
    #iniciar = int(input('Fazer varredura? '))
    iniciar = False
    while iniciar:
        nf = input('Insira a nota fiscal: ')
        valor_total = input('Insira o valor total da nota: ')
        valor_encontrado = False
        for txtret in lista_txtret:
            if nf in getInTXTRet(txtret, 7) and valor_total in getInTXTRet(txtret, 8):
                valor_encontrado = True
                break

            
        if valor_encontrado:
            print('O valor foi encontrado')
            newDest = os.getcwd()
            newDest = f'{newDest}/itembuscado/'
            try:
                os.makedirs(newDest)
            except:
                pass
            for xml in lista_xml:
                if txtret[36:46] in xml:
                    shutil.move(xml, newDest)
                    break
            for pdf in lista_pdf:
                if txtret[36:46] in pdf:
                    shutil.move(pdf, newDest)
                    break
            for oco in lista_ocor:
                if txtret[36:46] in oco:
                    shutil.move(oco, newDest)
                    break
            shutil.move(txtret, newDest)
        else:
            print('O valor não foi encontrado!')
#findItem()
def findNome(lista, i, f, nome):
    for j in lista:
        if j[i:f] == nome:
            return j
    return False

def findConj(cte_code=''):
    if cte_code =='': cte_code = input('Insira o Código do CT-e desejado: ')
    lista = [findNome(getItens('TXTRETURN.txt'), 34, 37,cte_code), 
            findNome(getItens('.xml'), 34, 37, cte_code),
            findNome(getItens('.pdf'), 34, 37, cte_code),
            findNome(getItens('procCte.txt'), 46, 49, cte_code)]
    return lista


def moveItens(cte_code='', newPaste=''):
    if cte_code =='': cte_code = input('Insira o Código do CT-e desejado: ')
    if newPaste == '': newPaste = input('Insira o novo local: ')
    conjunto = findConj(cte_code)
    newPaste = f'{os.getcwd()}/{newPaste}'
    try:
        os.makedirs(newPaste)
    except:
        pass
    for i in conjunto:
        shutil.move(i, newPaste)

def createCSVFile(): #não concluída
    lista_itens = getItens("TXTRETURN.txt")
    with open("agosto.csv", "r") as saida:
        writer = csv.writer(saida, delimiter=';')
        writer.writerow(['Numero NF', 'Numero CT-e', 'Data Emissão', 'Remetente', 'CPF/CNPJ Destinario', 'Cidade', 'Valor NF'])
        for i in lista_itens:
            lista = [getInTXTRet(i, 5), i[27:38], '0', getInTXTRet(i, 0), getTag('string', i), getTag('string', i), getInTXTRet(i, 1)] 
            writer.writerow(lista)

def getAllItems():
    lista_txtret = getItens('TXTRETURN.txt')
    lista_xml = getItens('.xml')
    lista_pdf = getItens('.pdf')
    lista_ocor = getItens('procCte.txt')
    print(f'lista_txtret = %s' % lista_txtret)
    print(f'lista_xml = %s' % lista_xml)
    print(f'lista_pdf = %s' % lista_pdf)
    print(f'lista_ocor = %s' % lista_ocor)
    a = input('Pressione algo para sair')