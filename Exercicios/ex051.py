# Calculando PA 

a = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
atual = a

print('Esses são os 10 primeiros numeros da Progressão aritmética:')
for c in range(10):
    print (atual, end=" ")
    atual += r