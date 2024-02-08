num = float(input('Qual é a distancia da sua viajem em Km: '))
if num <=200:
    print('Sua passagem vai custar R${:.2f}'.format(num * 0.50))
else:
    print('Sua passagem vai custar R${:.2f}'.format(num * 0.45))