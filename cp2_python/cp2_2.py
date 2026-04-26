ladoa = float(input('Digite o valor do lado A do triângulo: '))
while ladoa < 1:
    ladoa = float(input('O valor deve ser maior que 0, digite novamente: '))

ladob = float(input('Digite o valor do lado B do triângulo: '))
while ladob < 1:
    ladob = float(input('O valor deve ser maior que 0, digite novamente: '))

ladoc = float(input('Digite o valor do lado C do triângulo: '))
while ladoc < 1:
    ladoc = float(input('O valor deve ser maior que 0, digite novamente: '))

if ladoa < ladob:
    ladoa, ladob = ladob, ladoa
if ladoa < ladoc:
    ladoa, ladoc = ladoc, ladoa
if ladob < ladoc:
    ladob, ladoc = ladoc, ladob

if ladoa >= ladob + ladoc:
    print('Não forma um triângulo')
else:
    if ladoa**2 == ladob**2 + ladoc**2:
        print ('Triângulo retângulo')
    elif ladoa**2 > ladob**2 + ladoc**2:
        print('Triângulo obtusângulo')
    else:
        print('Triângulo acutângulo')

    if ladoa == ladob and ladoa == ladoc:
        print('Triângulo equilátero')
    elif ladoa == ladob or ladoa == ladoc or ladob == ladoc:
        print('Triângulo isósceles')