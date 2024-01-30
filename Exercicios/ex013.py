salario_atual = float(input('Quanto você ganha hoje? '))
proc_aumento = 0.15
aumento = salario_atual * proc_aumento
novo_salario  = salario_atual + aumento
print('Aceitando o novo cargo seu salario vai passar a ser R${}'.format(novo_salario))