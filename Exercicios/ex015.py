km = float(input('Quantidade de Quilometros percorrido: '))
dias = int(input('Quantos dias ele esteve alugado: '))
# R$60 por dia e R$0,15 por Km
valor = (km * 0.15) + (dias * 60)
print('O valor a ser pago pelo aluguel é de: R${:.2f}'.format(valor))