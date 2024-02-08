n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite um ultimo numero: '))

ma = n1
me = n1

if n2 > ma:
    ma = n2
if n2 < me:
    me = n2
if n3 > ma:
    ma = n3
if n3 < me:
    me = n3
    
print('O maior numero é: {} e o menor numero é: {}'.format(ma, me))