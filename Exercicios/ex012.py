valor_original = float(input('Qual o valor do produto? '))
desconto = 0.05 #no caso são 5%
valor_desconto = valor_original * desconto
novo_valor = valor_original - valor_desconto
print('Com o nosso desconto de 5% o novo valor é de R${}'.format(novo_valor))