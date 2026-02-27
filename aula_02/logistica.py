# Entrada de Dados

distancia = float(input("Distância da entrega (km): "))
peso_carga = float(input("Peso total da carga (kg): "))
cliente_fidelidade = input('Possui plano de fidelidade (sim/nao): ').strip().lower()

# Calculo Base
custo_base = (distancia * 2.5) + (peso_carga * 0.5)

# Regras de Decisao
if cliente_fidelidade == 'sim':
    custo_final = custo_base * 0.90 # 10% de desconto
    status = 'Cliente Ouro - Desconto Aplicado'
elif distancia > 500:
    custo_final = custo_base * 1.15 # 15% de taxa para longa distancia
    status = 'Taxa de Longa Distancia Aplicada'
else:
    custo_final = custo_base
    status = 'Tarifa Padrao'

print(f'\n --- Resumo do Frete ---')
print(f'Status: {status}')
print(f'Custo Total: {custo_final:.2f}')
