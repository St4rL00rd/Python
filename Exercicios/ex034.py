salario = float(input('quanto você ganha: R$'))
if salario <=1250:
    print('Seu novo salario com o aumento de 15 sera: R${}'.format(salario + (salario * (15 / 100))))
else:
    print('Seu novo salario com o aumento de 10 sera: R${}'.format(salario + (salario * (10 / 100))))