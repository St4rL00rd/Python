num = int(input('Digite o numero que deseja converter: '))
resp = int(input('Digite 1 para converter para binário\nDigite 2 para octal\nDigite 3 para hexadecimal\n'))
if resp == 1:
    print('O numero {} convertido para binario é: {}'.format(num, bin(num).replace('0b','')))
elif resp == 2:
    print('O numero {} convertido para octal é: {}'.format(num, oct(num).replace('0o','')))
elif resp == 3:
    print('O numero {} convertido para hexadecimal é: {}'.format(num, hex(num).replace('0x','')))