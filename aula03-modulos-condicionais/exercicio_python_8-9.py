num = 0

while num <= 0:
    num = int(input("Digite um número inteiro: "))
    while num <=0:
        num = int(input("Número digitado não é inteiro, digite novamente: "))

print(f"Os divisores de {num} são: ")

for i in range(1, num + 1):
    if num % i == 0:
        print(i)