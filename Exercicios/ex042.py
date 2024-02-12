#Analisando triangulos v2.0

a = float(input('Digite o tamanho da primeira reta: '))
b = float(input('Digite o tamanho da segunda reta: '))
c = float(input('Digite o tamanho da terceira reta: '))
if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print ('Essas retas pode formar um triangulo Equilátero!')
    elif a != b and b != c and a != c:
        print ('Essas retas pode formar um triangulo Escaleno!')
    else:
        print ('Essas retas pode formar um triangulo Isósceles!')
else:
    print ('Essas retas não formam um triangulo!')