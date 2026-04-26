nome = input('Digite o nome do funcionário: ')
cargo = int(input('Digite o código do cargo do funcionário (1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário): '))
while cargo < 1 or cargo > 4:
    cargo = int(input('O código do cargo do funcionário deve ser entre 1 e 4 (1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário), digite novamente:'))
salar = float(input('Digite o salário do funcionário em R$: '))
hex = float(input('Digite o total de horas extras trabalhadas: '))
falt = int(input('Digite o total de faltas no mês: '))

bonus = input('Recebeu bônus? (s ou n): ')
while bonus != 's' and bonus != 'n':
    bonus = input('Digite s ou n:')

def calcular_horas_extras(salario_base, horas):
    return salario_base * 0.015 * horas

def calcular_desconto_faltas(salario_base, faltas):
    return salario_base * 0.02 * faltas

def calcular_bonus(cargo, recebeu_bonus):
    if recebeu_bonus == 'n':
        return 0

    if cargo == 1:
        return 1000
    elif cargo == 2:
        return 500
    elif cargo == 3:
        return 300
    elif cargo == 4:
        return 100
    return 0

valhex = calcular_horas_extras(salar, hex)
descfalt = calcular_desconto_faltas(salar, falt)
valbonus = calcular_bonus(cargo, bonus)

acres = valhex + valbonus
salarfin = salar + acres - descfalt

print(f'O salário bruto é: R$ {salar:.2f}')
print(f'O total de acréscimos é de: R${acres:.2f}')
print(f'O total de descontos é de: R$ {descfalt:.2f}')
print(f'O salário final é de: R$ {salarfin:.2f}')



