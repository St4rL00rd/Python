# comparando numeros

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

if n1 > n2:
    print('O numero {} é o maior e o numero {} é o menor.'.format(n1, n2))
elif n1 < n2:
    print('O numero {} é o maior e o numero {} é o menor.'.format(n2, n1))
else:
    print('Os dois numeros são iguais')