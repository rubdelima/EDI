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
data, hora = '020822','1220'
for i in range(10):
    data, hora = randon_data(data, hora)
    print('{} - {}'.format(data, hora))