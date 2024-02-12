# Jogando Jokenpô v1.0

import random

escolha = ['PEDRA', 'PAPEL', 'TESOURA']
pc = random.choice(escolha)
resp = str(input('Escolha PEDRA, PAPEL ou TESOURA: ')).strip().upper()

if pc == resp:
    print('Empate!')
elif (resp == 'PEDRA' and pc == 'TESOURA') or (resp == 'TESOURA' and pc == 'PAPEL') or (resp == 'PAPEL' and pc == 'PEDRA'):
    print('Você ganhou!')
else:
    print('Você perdeu!')

print('Você escolheu {} e o Computador escolheu {}'.format(resp, pc))