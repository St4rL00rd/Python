frase = str(input('Digite uma frase: '))
fraseL = frase.lower()
print('{} --- {} --- {}'.format(fraseL.count('a'), fraseL.find('a'), fraseL.rfind('a')))