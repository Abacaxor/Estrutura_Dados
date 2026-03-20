taxa_de_perda = 0.05

def calcular_estoque_reaL(quantidade):
    perda_estimada = quantidade * taxa_de_perda
    return quantidade - perda_estimada

print (f'Resultado: {calcular_estoque_reaL(750)}')