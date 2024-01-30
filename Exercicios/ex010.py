r = float(input('Quando Reais você tem na carteira: '))
d = float(4.95)
q = r // d
s = r % d
print('Com a cotação do dólar a R${}, com R${}, você consegue comprar ${}, e sobra R${:.2f} para você!'.format(d,r,q,s))