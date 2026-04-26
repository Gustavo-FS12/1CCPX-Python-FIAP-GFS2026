code = int(input('Digite o código do estado de origem da carga (de 1 a 5): '))
while code < 1 or code > 5:
    code = int(input('O código do estado de origem da carga deve ser entre 1 e 5, digite novamente: '))

pesot = float(input('Digite o peso da carga em toneladas: '))
while pesot <= 0:
    pesot = float(input('O peso da carga deve ser  maior que 0, digite novamente: '))

codg = int(input('Digite o código da carga (de 10 a 40): '))
while codg < 10 or codg > 40:
    codg = int(input('O código da carga deve ser entre 10 e 40, digite novamente: '))

pesokg = pesot*1000

prec = 0
pimp = 0

if codg >= 10 and codg <= 20:
    prec = pesokg*100
elif codg > 20 and codg <= 30:
    prec = pesokg*250
elif codg > 30 and codg <= 40:
    prec = pesokg*340

if code == 1:
    pimp = 35
elif code == 2:
    pimp = 25
elif code == 3:
    pimp = 15
elif code == 4:
    pimp = 5
elif code == 5:
    pimp = 0

vimp = prec * (pimp/100)
prect = prec + vimp

print (f'Peso da carga do caminhão: {pesokg} kg')
print (f'Preço da carga do caminhão: R$ {prec:.2f}')
print (f'Valor do imposto: R$ {vimp:.2f}')
print (f'Valor total tranportado pelo caminhão (carga + imposto): R$ {prect:.2f}')