import random

# Coleta o nome dos alunos
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')

# Guarda os nomes
alunos = [a1, a2, a3, a4]

# Sorteia o aluno 
aluno_escolhido = random.choice(alunos)

# Mostra o resultado
print('O aluno escolhido foi o: {}'.format(aluno_escolhido))