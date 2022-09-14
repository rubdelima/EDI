from funcoes import getItens
import openpyxl as xl

#se não tiver instalado instale as extenções:
#pip3 install openpyxl

def clear_matriz(matriz):
    for i in matriz:
        for j in i:
            if j == 'None' or j == None:
                j=''
    return matriz

def print_matriz(matriz):
    matriz = clear_matriz(matriz)
    for i in matriz:
        print(i)



nome_arquivo = getItens('xlsx')[0]

arquivo = xl.load_workbook(nome_arquivo)

page = arquivo['Pagamento de Fretes']

matriz = []
for rows in page.iter_rows():
    linha = []
    for cell in rows:
        if cell.value != 'None':
            linha.append(cell.value)
    matriz.append(linha)



print_matriz(matriz)