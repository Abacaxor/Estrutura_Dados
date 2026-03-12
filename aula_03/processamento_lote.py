print('--- Sistema de Processamento de Lote ---')

qtd_itens = int(input('Quantidade de itens no lote: '))
soma_pesos = 0.0

for i in range(1, qtd_itens + 1):
    peso = float(input(f'Peso do item {i} (Kg): '))
    soma_pesos += peso #acumulador

media = soma_pesos / qtd_itens
print(f'\nTotal processado: {soma_pesos:.2f} Kg')
print(f'Media de peso: {media:.2f} Kg')