nome = input('Digite seu nome completo: ')
nomeMA = nome.upper()
nomeMI = nome.lower()
nomeP = len(nome.split()[0])
nomeC = len(nome) - nome.count(' ')
print('{} --- {} --- {} --- {}'.format(nomeMA, nomeMI, nomeP, nomeC))