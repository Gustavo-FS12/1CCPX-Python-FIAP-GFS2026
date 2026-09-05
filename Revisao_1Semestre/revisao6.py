lista = []

num = float(input('Digite um número inteiro maior que zero: '))
while num < 1 or num % 1 != 0:
    num = float(input('O número deve ser inteiro e maior que zero, digite novamente: '))
num_int = int(num)

for i in range (num_int):
    val = float(input('Digite um valor: '))
    lista += [val]

print(lista)

# Por sorteio

import random


