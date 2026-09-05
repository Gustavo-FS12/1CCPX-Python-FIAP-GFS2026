lista_notas = []
aluno = 1

quant = int(input("Digite a quantidade de alunos: "))
while num <= 0:
    quant = int(input("A quantidade de alunos deve ser maior que zero, digite novamente: "))

for i in range(quant):
    nota = int(input(f"Digite a nota do aluno {aluno}: "))
    while nota < 0 or nota > 10:
        nota = int(input(f"A nota deve estar entre 0 e 10, digite novamente a nota do aluno {aluno}: "))
    lista_notas += [nota]
    aluno += 1

media = sum(lista_notas) / len(lista_notas)
moda =