num = float(input('Digite um número inteiro positivo: '))
while num < 1 or num % 1 != 0:
    num = float(input('O número deve ser inteiro e positivo, digite novamente: '))
num_inteiro = int(num)
soma = 0
for i in range (0, num_inteiro+1):
    soma += i
print(soma)