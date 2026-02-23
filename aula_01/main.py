# Operadores e Condicionais
print("--- Diagnóstico de Performance de Algoritimo ---")

processamentos = int(input("Quantidade de registros processados: "))
tempo_execucao = float(input("Tempo total de execuçao (segundos): "))

# Cálculo da media de tempo por registro
media_por_registro = tempo_execucao / processamentos

# Classificacao simples de eficiencia
status = "Eficiente"
if media_por_registro > 0.01:
    status = "Alerta de Latência"

print(f"Resultado: {status} ({media_por_registro:.4f} s/reg)")
