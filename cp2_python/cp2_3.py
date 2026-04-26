cp1 = float(input('Digite a nota do Checkpoint 1: '))
while cp1 <0 or cp1 >10:
    cp1 = float(input('A nota do Checkpoint 1 deve ser entre 0 e 10: '))

cp2 = float(input('Digite a nota do Checkpoint 2: '))
while cp2 <0 or cp2 >10:
    cp2 = float(input('A nota do Checkpoint 2 deve ser entre 0 e 10: '))

cp3 = float(input('Digite a nota do Checkpoint 3: '))
while cp3 <0 or cp3 >10:
    cp3 = float(input('A nota do Checkpoint 3 deve ser entre 0 e 10: '))

sp1 = float(input('Digite a nota da Sprint 1: '))
while sp1 <0 or sp1 >10:
    sp1 = float(input('A nota da Sprint 1 deve ser entre 0 e 10: '))

sp2 = float(input('Digite a nota da Sprint 2: '))
while sp2 <0 or sp2 >10:
    sp2 = float(input('A nota da Sprint 2 deve ser entre 0 e 10: '))

gs = float(input('Digite a nota da Global Solution: '))
while gs <0 or gs >10:
    gs = float(input('A nota da Global Solution deve ser entre 0 e 10: '))

menor = 0
if cp1 <= cp2 and cp1 <= cp3:
    menor = cp1
if cp2 <= cp1 and cp2 <= cp3:
    menor = cp2
if cp3 <= cp1 and cp3 <= cp2:
    menor = cp3

media = ((cp1 + cp2 + cp3 - menor + sp1 + sp2) / 4) * 0.4 + (gs * 0.6)
mediapeso = media * 0.4

print(f'A média do semestre sem o peso é: {media:.1f}')
print(f'A média do semestre com o peso é: {mediapeso:.1f}')