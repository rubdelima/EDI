from funcoes import *
from docob import DOCOB
def getAut(arquivo):
    lista = [[],[]]
    with open(arquivo, 'r') as a:
        i = a.read()
        i = i.splitlines()
        print('Confira os dados antes de fazer o documento: ')
        print(f'Remetente: {i[0]}, CNPJ Remetente: {i[1]}, Destinatário: {i[2]},')
        print(f'CT-e: {i[3]}, Valor do Frete: {i[4]}')
        print(f'Nota fiscal: {i[7]}, Peso: {i[6]} Valor Total: {i[8]}')
        cte = i[3]
        valor_frete = i[4]
        nota = i[7]
        peso = i[6]
        valor = i[8]
        comando = 0
        while not comando:
            comando = int(input('Deseja alterar algo? 1/0: '))
            if comando == 0:
                break
            else:
                escolha = int(input('Qual item deseja alterar?\n1. CTe\n2.Valor do Frete\n3. Nota Fiscal\n4. Peso da Nota\n5. Valor da Nota'))
                novo_valor = input('Insira o novo valor: ')
                if escolha == 1: cte = novo_valor
                elif escolha == 2:valor_frete = novo_valor
                elif escolha == 3: nota = novo_valor
                elif escolha == 4: peso = novo_valor
                elif escolha == 5: valor= novo_valor
        emissao = input('Insira a data de emissão: ')
        # cte, valor frete
        lista[0].append(cte)
        lista[0].append(valor_frete)
        # nota, emissao, peso, valor
        lista[1].append(nota)
        lista[1].append(emissao)
        lista[1].append(peso)
        lista[1].append(valor)
        
        
    return lista
doc = DOCOB()

arquivos = getItens('TXTRETURN.txt')

while True:
    escolha = input('Diga o que deseja fazer:\n1. Gerar OCOREN\n2. Inserir Novos Dados\n3. Sair\n')
    if escolha == '1':
        valorcobranca = 0
        #Dados Gerais
        data, hora = data_hora_aut()
        destinatario = input('Insira o destinatário: ')
        doc.linha1(destinatario, data, hora)
        numerocobranca = input('Insira o número da cobrança: ')
        dataemi = input('Insira a data de emissao: ')
        datavenci = input('Insira a data de vencimento: ')
        icms = input('Insira o valor do ICMS: ')
        for i in arquivos:
            i = getAut(i)
            doc.linha5(*i[0])
            doc.linha6(*i[1])
            valorcobranca += float(i[0][1])
        doc.linha4(numerocobranca, dataemi, datavenci, valorcobranca, icms)
        doc.linha7(len(arquivos), valorcobranca)
        imprimir(doc.getDoc())
        
    elif escolha == '2':
        escolha2 = input('Diga o que deseja inserir?\n 1. Manual\n2. Automatica')
        if escolha2 == '1':
            print('Indisponível')
        elif escolha2 == '2':
            numeroconhecimento  = input("") # cte emitido
            valorfrete  = input("") # valor do frete
            numeronotafiscal  = input("") # numero da nota fiscal
            dataemi  = input("") #data da emissão
            pesonotaf  = input("") #peso da nota fiscal
            valormercadoria  = input("") # valor total da mercadoria
    elif escolha == '3':
        break
    else:
        print('Comando não identificado')