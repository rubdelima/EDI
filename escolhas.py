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

lista_ocorr2 = ['Devolução/recusa total',
                'Devolução/recusa parcial',
                '3']


def show_list(lista):
    for i in range(len(lista)):
        print(i, ' - ', lista[i])
    
def escolher():
    print('Esolha a ocorrência:')
    ent =  input('A entrega foi normal? 1/0')
    if ent == '1':
        return 1
    else:
        while True:
            show_list(lista_ocorr)
            try:
                ent = int(input('O que houve? '))
                if ent > 0 and ent < 59:
                    return ent
                print("Valor não identificado")
            except:
                print("Valor não identificado")

def escolher2():
    print('Esolha a ocorrência:')
    show_list(lista_ocorr)
    try:
        ent = int(input('O que houve? '))
        if ent > 0 and ent < 3:
            return ent+1
        print("Valor não identificado")
    except:
        print("Valor não identificado")
