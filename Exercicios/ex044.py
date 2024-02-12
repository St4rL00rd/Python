# Calculo de preço com formas de pagamento

produto = str(input('Qual o produto que deseja comprar: ')).strip()
preco = float(input('Qual o preço do produto: R$'))
pagamento = int(input('Qual a forma de pagamento\n[ 1 ] para a vista em dinheiro\n[ 2 ] para a vista em cartão\n[ 3 ] para parcelar em até 2 vezes\n[ 4 ] para parcelar em 3 vezes ou mais\nEscolha uma opção:'))
if pagamento == 1:
    print('O preço do produto {} pagando à vista em dinheiro ficou R${:.2f} com o desconto de 10%'.format(produto, preco - (preco * 0.10)))
elif pagamento == 2:
    print('O preço do produto {} pagando à vista no cartão ficou R${:.2f} com o desconto de 5%'.format(produto, preco - (preco * 0.05)))
elif pagamento == 3:
    print('O preço do produto {} pagando em até 2 vezes no cartão ficara R${:.2f}'.format(produto, preco))
elif pagamento == 4:
    print('O preço do produto {} pagando em 3 vezes ou mais no cartão ficara R${:.2f} com o juros de 20%'.format(produto, preco + (preco * 0.20)))