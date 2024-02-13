# Verificando se a palavra é palindromo

frase = str(input('Digite uma palavra: '))
se = frase.lower().replace(" ", "")
invertida = ''
for letra in se:
    invertida = letra + invertida

if se == invertida:
    print('A frase é um palindromo.\n{}'.format(invertida))
else:
    print(' A frase "{}" não é um palindromo.'.format(frase))