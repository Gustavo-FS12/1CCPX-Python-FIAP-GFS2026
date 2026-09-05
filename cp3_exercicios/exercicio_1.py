lista = []

for i in range (5):
    num = int(input("Digite um número maior que zero: "))
    while num <= 0:
        num = int(input("O número digitado é menor ou igual a zero, digite novamente: "))
    lista += [num]
    i += 1

print(lista)