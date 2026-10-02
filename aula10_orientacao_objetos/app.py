from aluno import Aluno
from aula09_mini_crm import model
from disciplina import Disciplina

# CRIAR /  ESTANCIAR 1 ALUNO:
aluno1 = Aluno('João', '123456', 'Ciência da Computação')
#print(aluno1.curso)

# CRIAR /  ESTANCIAR 1 ALUNO:
dsa = Disciplina('Data Strucutures', 'Álvaro')
model_lin = Disciplina('Modelagem Linear', 'Rodolpho')
# print(model_lin.professor)
# model_lin.exibir_infos()

# Matricular o aluno nas disciplinas

aluno1.matricular(dsa)
aluno1.matricular(model_lin)
#print(aluno1.disciplinas[1].professor)

# Adicioanr notas do aluno referente as disciplinas
aluno1.adicionar_nota(dsa, 10)
aluno1.adicionar_nota(dsa, 8)
aluno1.adicionar_nota(model_lin, 5)
aluno1.adicionar_nota(model_lin, 3)
#print(aluno1.notas_por_disciplina)

print(aluno1.calcular_media_d(model_lin))