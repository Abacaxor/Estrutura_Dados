# Programa de Reforço: Simulador de Rendimento Composto
print("--- Investimento Lab Essentials ---")

valor_inicial = float(input('Valor do investimento: R$ '))
taxa_juros = float(input('Taxa de juros anual (em %): '))
anos = int(input('Tempo de investimento (anos): '))

# Calculo de Juros Compostos
# Convertendo a taxa (ex: 10% vira 0.10)
taxa_decimal = taxa_juros / 100

# Formula: Montante = capital * (1 + taxa) ^ tempo
valor_final = valor_inicial * (1 + taxa_decimal) ** anos
rendimento_total = valor_final - valor_inicial

# Logica de Classificacao de Perfil
status_investimento = 'Baixo Retorno'
if rendimento_total > (valor_inicial * 0.5):
    status_investimento = 'Alto Retorno'

print(f'\n--- Relatorio Final ---')
print(f'Rendimento Total: R$ {rendimento_total:.2f}')
print(f'Valor Final Acumulado: R$ {valor_final:.2f}')
print(f'Classificacao: {status_investimento}')