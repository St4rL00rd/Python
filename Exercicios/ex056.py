# media de idade e mais 

bn = []
bi = []
bs = []

for c in range(4):
    nome = str(input(f'Qual o nome da {c+1}ª pessoa: ')).strip()
    idade = int(input(f'Qual a idade da {c+1}ª pessoa: '))
    while True:
        sexo = str(input(f'Qual o sexo da {c+1}ª pessoa (Masculino/Feminino): ')).strip().capitalize()
        if sexo in ['Masculino', 'Feminino']:
            break
        else:
            print("Por favor insira 'Masculino' ou 'Feminino' como sexo.")
            
    bn.append(nome)
    bi.append(idade)
    bs.append(sexo)
    
soma_idade = 0
for idade in bi:
    soma_idade += idade
    
h_velho = None
m_20 = 0
for nome, idade, sexo in zip(bn, bi, bs):
    if sexo == 'Masculino':
        if h_velho is None or idade > h_velho[1]:
            h_velho = (nome, idade)
    elif sexo == 'Feminino' and idade < 20:
        m_20 +=1
if h_velho:
    print(f'O homem mais velho é {h_velho[0]} com {h_velho[1]} anos.')
else:
    print('Não há homens na lista.')
print(f'Total de mulheres com menos de 20 anos: {m_20}')
print(f'A media da idade é: {soma_idade / 4}')