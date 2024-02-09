import datetime as da

nasc = int(input('Em que ano você nasceu: '))
idade = da.datetime.now().year - nasc

if idade < 18:
    print('Você ainda não precisa se alistar. Faltam {} anos para isso.'.format(18 - idade))
elif idade == 18:
    print('Esta na hora de se alistar não se esqueça!')
else:
    print('Ja passou da hora de se alistar, espero que tenha realizado seu alistamento ha {} anos atras.'.format(idade - 18))