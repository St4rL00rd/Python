#Calcular idade de nadador para saber em qual categoria esta 

import datetime 

nasc = int(input('Em que ano você nasceu: '))
idade = datetime.datetime.now().year - nasc

if idade <= 9:
    print('Esse atleta deve competir na categoria MIRIN')
elif idade > 9 and idade <= 14:
    print('Esse atleta deve competir na categoria INFANTIL')
elif idade > 14 and idade <= 19:
    print('Esse atleta deve competir na categoria JUNIOR')
elif idade > 19 and idade <= 20:
    print('Esse atleta deve competir na categoria SENIOR')
else:
    print('Esse atleta deve competir na categoria MASTER')