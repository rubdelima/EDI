lista_ocorr = ['Processo de Transporte já Iniciado',
                    'Entrega Realizada Normalmente',
                    'Entrega Fora da Data Programada',
                    'Recusa por Falta de Pedido de Compra',
                    'Recusa por Pedido de Compra Cancelado',
                    'Falta de Espaço Físico no Depósito do Cliente Destino',
                    'Endereço do Cliente Destino não Localizado',
                    'Devolução não Autorizada pelo Cliente',
                    'Preço Mercadoria em Desacordo com o Pedido Compra',
                    'Mercadoria em Desacordo com o Pedido Compra',
                    'Cliente Destino somente Recebe Mercadoria com Frete Pago',
                    'Recusa por Deficiência Embalagem Mercadoria',
                    'Redespacho não Indicado',
                    'Transportadora não Atende a Cidade do Cliente Destino',
                    'Mercadoria Sinistrada',
                    'Embalagem Sinistrada',
                    'Pedido de Compras em Duplicidade',
                    'Mercadoria fora da Embalagem de Atacadista',
                    'Mercadorias Trocadas',
                    'Reentrega Solicitada pelo Cliente',
                    'Entrega Prejudicada por Horário/Falta de Tempo Hábil',
                    'Estabelecimento Fechado',
                    'Reentrega sem Cobrança do Cliente',
                    'Extravio de Mercadoria em Trânsito',
                    'Mercadoria Reentregue ao Cliente Destino',
                    'Mercadoria Devolvida ao Cliente de Origem',
                    'Nota Fiscal Retida pela Fiscalização',
                    'Roubo de Carga',
                    'Mercadoria Retida até Segunda Ordem',
                    'Cliente Retira Mercadoria na Transportadora',
                    'Problema com a Documentação (Nota Fiscal e/ou CTRC)',
                    'Entrega com Indenização Efetuada',
                    'Falta com Solicitação de Reposição',
                    'Falta com Busca/Reconferência',
                    'Cliente Fechado para Balanço',
                    'Quantidade de Produto em Desacordo (Nota Fiscal e/ou Pedido)',
                    'Extravio de documentos pela cia. Aérea-Cód. Transp. Aéreo',
                    'Extravio de carga pela cia. Aérea– Cód. Transp. Aéreo',
                    'Avaria de carga pela cia. Aérea– Cód. Transp. Aéreo',
                    'Corte de carga na pista– Cód. Transp. Aéreo',
                    'Aeroporto fechado na origem - Cód. Transp. Aéreo (alterar descrição p/ RETIDA PARA PAGAMENTO DO ICMS)',
                    'Pedido de Compra Incompleto',
                    'Nota Fiscal com Produtos de Setores Diferentes',
                    'Feriado Local/Nacional',
                    'Excesso de Veículos',
                    'Cliente Destino Encerrou Atividades',
                    'Responsável de Recebimento Ausente',
                    'Cliente Destino em Greve',
                    'Aeroporto fechado no destino                           - Cód. Transp. Aéreo',
                    'Vôo cancelado                                          - Cód. Transp. Aéreo',
                    'Greve nacional (Greve Geral)',
                    'Mercadoria Vencida (Data de Validade Expirada)',
                    'Mercadoria Redespachada (Entregue para Redespacho)',
                    'Mercadoria não foi Embarcada, Permanecendo na Origem',
                    'Mercadoria Embarcada sem Conhecimento/Conhecimento não Embarcado',
                    'Endereço de Transportadora de Redespacho não Localizado/Informado',
                    'Cliente não Aceita Mercadoria com Pagamento de Reembolso',
                    'Transportadora não Atende a Cidade da Transportadora de Redespacho',
                    'Quebra do Veiculo de Entrega',
                    'Cliente sem Verba para Pagar o Frete']

lista_ocorr2 = ['00 = Entrega Normal',
                '01 = Devolução/recusa total',
                '02 = Devolução/recusa parcial',
                '03 = Aceite/entrega por acordo']

lista_cobranca = ['0 = NOTA FISCAL FATURA', '1 = ROMANEIO']

lista_acao_doc = ['I - Incluir','E - Excluir']

lista_de_txt = ['Saída para Entrega', 'Entrega Realizada', 'Entrega não Realizada']

def add_zero(numero):
    numero = f'0{numero}'
    return numero

def show_list(lista):
    for i in range(len(lista)):
        print(i, ' - ', lista[i])
    
def escolher(padrao=False, cnt=0):
    if not padrao:
        print('Esolha a ocorrência:')
        ent =  input('A entrega foi normal? 1/0 ')
        if ent == '1':
            return add_zero(1)
        else:
            while True:
                show_list(lista_ocorr)
                try:
                    ent = int(input('O que houve? '))
                    if ent > 0 and ent < 59:
                        if ent < 10:
                            return add_zero(ent)
                        return ent
                    print("Valor não identificado")
                except:
                    print("Valor não identificado")
    else:
        if cnt == 0:
            return '00'
        if cnt == 1:
            return '01'

def escolher2(padrao=False, txt=False):
    if padrao and txt:
        return 'Entrega Normal'
    if padrao:
        return '00'
    else:
        print('Esolha a ocorrência:')
        show_list(lista_ocorr2)
        while 1:
            try:
                ent = int(input('O que houve? '))
                if ent >= 0 and ent < 3:
                    return f'0{ent}'
                print("Valor não identificado")
            except:
                print("Valor não identificado")
            

def escolher3():
    while True:
        print('Esolha o tipo do documento de cobrança:')
        show_list(lista_cobranca)
        ent = input('O que houve? ')
        if ent == '1' or ent == '0':
            return ent
        print("Valor não identificado")

def escolher4():
    while True:
        print('Deseja incluir ou excluir/cancelar:')
        show_list(lista_acao_doc)
        ent = input('O que houve? ')
        if ent == 'I' or ent == 'E':
            return ent
        print("Valor não identificado")

def escolher5(data, hora, padrao=False, vez=0, lista=lista_de_txt):
    if not padrao:
        while 1:
            print('Qual ocorrência ocorreu?')
            show_list(lista)
            try:
                escolha = int(input())
                return lista[escolha]
            except:
                print('Houve algum erro, tente novamente')
    else:
        if vez == 1:
            return f'ENTREGA REALIZADA COM SUCESSO AS {hora[0:2]}:{hora[2:]} DE {data[0:2]}/{data[2:4]}/{data[6:]}'
        elif vez == 0:
            return f'ITEM SAIU PARA A ENTREGA AS {hora[0:2]}:{hora[2:]} DE {data[0:2]}/{data[2:4]}/{data[6:]}'
