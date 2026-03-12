print('--- Sistema de Produtividade Fabril ---')

# 1. Defina o limite do turno
horas_trabalhadas = int(input('Quantas horas durou o turno? '))

total_pecas = 0

# 2. Estrutura de repetição determinada
for hora in range(1, horas_trabalhadas + 1):
    producao = int(input(f'Quantidade de pecas produzidas na hora {hora}: '))
    total_pecas += producao

media_por_hora = total_pecas / horas_trabalhadas

print(f'\n--- Relatorio de Producao ---')
print(f'Total de pecas produzidas: {total_pecas}')
print(f'Media de pecas produzidas: {media_por_hora:.1f}pecas/hora')