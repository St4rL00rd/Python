import random

# Coleta os nomes
a1 = input('Digite o nome de um aluno: ')
a2 = input('Digite outro nome de um aluno: ')
a3 = input('Digite mais um nome de um aluno: ')
a4 = input('Digite um ultimo nome de um aluno: ')

# Guarda os nomes
alunos = [a1, a2, a3, a4]

# Embaralha a sequencia
random.shuffle(alunos)

# Escreve a resposta
print('A ordem de apresentação sera: ')
for aluno in alunos:
    print(aluno)