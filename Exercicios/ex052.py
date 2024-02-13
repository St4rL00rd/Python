# Vendo se o numero é primo

n = int(input('Digite um numero para saber se ele é primo: '))
if n % 1 == 0 and n % n == 0:
    print('O numero {} é um numero primo!'.format(n))
else:
    print('O numero {} não é um numero primo'.format(n))