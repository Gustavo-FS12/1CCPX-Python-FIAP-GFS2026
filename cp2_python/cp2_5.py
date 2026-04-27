nome = input("Digite o nome do cliente: ")
idade = int(input("Digite a idade do cliente: "))
rendamen = float(input("Digite a renda mensal do cliente: "))
while rendamen <=0:
    rendamen = float(input("A renda mensal do cliente deve ser maior que 0, digite novamente: "))
valemp = float(input("Digite o valor desejado do empreśtimo: "))
while valemp <=0:
    valemp = float(input('O valor desejado do empréstimo deve ser maior que 0, digite novamente: '))
parcela = int(input("Digite a quantidade de parcelas do empréstimo (de 3 a 24): "))
while parcela <3 or parcela >24:
    parcela = int(input('A quantidade de parcelas deve estar entre 3 e 24, digite novamente: '))

def pode_aprovar(idade, renda, valor):
    if idade >=18 and renda*20 >= valor:
        return 1
    else:
        return 0

def definir_taxa(parcelas):
    if parcelas <= 6:
        return 0.05
    elif parcelas <= 12:
        return 0.08
    else:
        return 0.10

def calcular_parcela(valor, taxa, parcelas):
    return valor * ((taxa * (1 + taxa)**parcelas) / ((1 + taxa)**parcelas -1))

def calcular_total(parcela, parcelas):
    return parcela*parcelas

def calcular_juros(total, valor):
    return total-valor

juros = definir_taxa(parcela)
valparcela = calcular_parcela(valemp, juros, parcela)
totalpago = calcular_total(valparcela, parcela)
jurospagos = calcular_juros(totalpago, valemp)
aprovado = pode_aprovar(idade, rendamen, valemp)

if aprovado == 1:
    print(f'Nome do cliente: {nome}')
    print(f'Valor financiado: R${valemp:.2f}')
    print(f'Taxa de juros aplicada: {juros*100}%')
    print(f'Valor da parcela: R${valparcela:.2f}')
    print(f'Valor total pago: R${totalpago:.2f}')
    print(f'Valor total dos juros: R${jurospagos:.2f}')

else:
    if idade <18 and rendamen*20 < valemp:
        print('Crédito não aprovado, cliente menor de 18 anos e o valor do empréstimo é maior do que 20 vezes a renda mensal')
    elif idade <18:
        print('Crédito não aprovado, cliente menor de 18 anos')
    else:
        print('Crédito não aprovado, valor do empréstimo é maior do que 20 vezes o salário do cliente')





