a = float(input('Digite o tamanho da primeira reta: '))
b = float(input('Digite o tamanho da segunda reta: '))
c = float(input('Digite o tamanho da terceira reta: '))
if a + b > c and a + c > b and b + c > a:
    print ('Essas retas pode formar um triangulo!')
else:
    print ('Essas retas não formam um triangulo!')