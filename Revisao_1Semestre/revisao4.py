num = float(input('Digite um valor inteiro positivo: '))
while num < 1 or num % 1 != 0:
    num = float(input('O número deve ser inteiro e positivo, digite novamente: '))
num_inteiro = int(num)

for i in range (1, num_inteiro+1):
    if num_inteiro % i == 0:
        print(i)