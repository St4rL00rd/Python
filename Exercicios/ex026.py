frase = str(input('Digite uma frase: ')).lower().strip()
print('{} --- {} --- {}'.format(frase.count('a'), frase.find('a') + 1, frase.rfind('a') + 1))