# Somando numeros pares

soma = 0
for c in range(0,6):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        soma += num
print('A soma de todos os numeros pares que digitou é {}'.format(soma))
    