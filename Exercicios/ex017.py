import math

x = float(input('Qual é o comprimento do cateto oposto? '))
y = float(input('Qual é o comprimento do cateto adjacente? '))
print('O comprimento da hipotenusa é: {}'.format(math.hypot(x,y)))