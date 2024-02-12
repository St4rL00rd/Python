# Aprovando emprestimos

valor = float(input('Qual é o valor da casa desejada ? R$'))
salario = float(input('Qual é o salario do comprador ? R$'))
anos = int(input('Em quantos anos o comprador deseja parcelar ? '))
prest = valor / (anos * 12)
por = salario * 0.30

if por > prest:
    print('Financiamento APROVADO, serão parcelas no valor de R${:.2f} por {} meses.'.format(prest, anos*12))
elif por == prest:
    print('Financiamento APROVADO, serão parcelas no valor de R${:.2f} por {} meses.\nATENÇÃO VALOR DA PARCELA É O EQUIVALENTE A 30% DO SALARIO!'.format(prest, anos*12))
else:
    print('FINANCIAMENTO REPROVADO!')