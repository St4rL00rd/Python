vel = int(input('Qual é a velocidade que o carro esta em Km/h: '))
if vel <=80:
    print('Tudo certo pode seguir!')
else:
    print('Você foi multada por estar acima da velocidade permitida, sua multa é de R${}'.format((vel-80)*7))