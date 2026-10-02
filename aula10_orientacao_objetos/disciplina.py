class Disciplina:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor

    def exibir_infos(self):
        print(f'Disciplina: {self.nome} | Prof: {self.professor}')

# TEMPORÁRIO !!

# model_mat = Disciplina('Modelagem matemática', 'Igor')
# print(model_mat.professor)
# model_mat.exibir_infos()