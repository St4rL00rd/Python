# Calculo de media melhorado

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m >= 7.0:
    print('Parabens você foi aprovado! Pois sua nota final foi {}'.format(m))
elif m < 5.0:
    print('Infelizmente voce foi reprovado! Pois sua nota final foi {}'.format(m))
else:
    print('Você esta de recuperação. Pois sua nota final foi {}'.format(m))