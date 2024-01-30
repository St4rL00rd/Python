import math

ang = int(input('Qual é o angulo: '))
rad = math.radians(ang)
print('O seno do angulo {}°, é {:.2f}, e o cosseno é {:.2f}, e a tangente é {:.2f}'.format(ang, math.sin(rad), math.cos(rad), math.tan(rad)))