import random

num = random.randint(0, 5)
resp = int(input('Pensei em um numero entre 0 e 5 tente adivinhar digitando qual foi o numero: '))
if resp - num == 0:
    print('Parabens você acertou!')
else:
    print('Você errou o numero que eu pensei foi {}'.format(num))