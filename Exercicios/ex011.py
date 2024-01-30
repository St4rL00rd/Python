h = float(input('Quantos metros de altura tem a parede? '))
b = float(input('Quantos metros de largura tem a parede? '))
a = b * h
#eu sei que 1L pinta 2m quadrados
l = 2
#quanto eu preciso
q = a / l
print('Para pintar {}m², você vai precisar usar {}L de tinta.'.format(a,q))