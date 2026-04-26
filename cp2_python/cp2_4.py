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

valhex = salar*0.015*hex
descfalt = salar*0.02*falt

valbonus = 0
if bonus == 'n':
    valbonus = 0
elif cargo == 1:
    valbonus = 1000
elif cargo == 2:
    valbonus = 500
elif cargo == 3:
    valbonus = 300
elif cargo == 4:
    valbonus = 100

acres = valhex + valbonus
salarfin = salar+acres-descfalt

print(f'O salário bruto é: R$ {salar:.2f}')
print(f'O total de acréscimos é de: R${acres:.2f}')
print(f'O total de descontos é de: R$ {descfalt:.2f}')
print(f'O salário final é de: R$ {salarfin:.2f}')