# Vendo quem é mais pesado

pesos = []

for c in range(5):
    peso = float(input(f'Qual o peso da {c+1}ª pessoa em kg: '))
    pesos.append(peso)
    
maior = max(pesos)
menor = min(pesos)

print(f'Maior peso: {maior} Kg')
print(f'Menor peso: {menor} Kg')