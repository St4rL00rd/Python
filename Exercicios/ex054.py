# verificando que é maior de idade

import datetime

maiores = []
menores = []
ano = datetime.datetime.now().year

for c in range(2):
    nome = str(input('Qual o nome da pessoa: '))
    nasc = int(input('Qual ano ele nasceu? '))
    idade = ano - nasc
    
    if idade >=18:
        maiores.append(nome)
    else:
        menores.append(nome)

print('\nPessoas maiores de idade:')
for nome in maiores:
    print(nome)

print('\nPessoas menores de idade:')
for nome in menores:
    print(nome)