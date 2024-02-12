#Calculando o indice de massa corporal

n = str(input('Qual o nome da pessoa: '))
p = float(input('Qual o peso da pessoal em kg: '))
a = float(input('Qual é a altura da pessoa em m: '))
imc = p / (a * a)
if imc < 18.5:
    print('O IMC é {:.1f}, {} esta abaixo do peso ideal!'.format(imc, n))
elif imc >= 18.5 and imc <= 24.9:
    print('O IMC é {:.1f}, {} esta no seu peso ideal!'.format(imc, n))
elif imc >= 25.0 and imc <= 29.9:
    print('O IMC é {:.1f}, {} esta com sobrepeso!'.format(imc, n))
elif imc >= 30.0 and imc <= 34.9:
    print('O IMC é {:.1f}, {} esta com OBESIDADE GRAU I!'.format(imc, n))
elif imc >= 35.0 and imc <= 39.9:
    print('O IMC é {:.1f}, {} esta com OBESIDADE GRAU II (SEVERA)!'.format(imc, n))
else:
    print('O IMC é {:.1f}, {} esta com OBESIDADE GRAU III (MORBIDA)!'.format(imc, n))