while True:
    num = input('Digite um número de 4 dígitos: ')
    
    if num.isdigit() and len(num) == 4:
        break
    else:
        print('Número inválido. Por favor, digite exatamente 4 dígitos.')

print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(num[0], num[1], num[2], num[3]))