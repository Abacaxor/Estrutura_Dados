
def validar_temperatura(valor):
    if -50 <= valor <= 150:
        return True
    else:
        return False

qtd_medicoes = int(input("Quantas medições de temperatura serão feitas? "))

soma_validas = 0
total_validas = 0
descartados = 0
for i in range(1, qtd_medicoes + 1):
    temp = float(input(f"Digite a temperatura da medição {i}: "))
    if validar_temperatura(temp):
        soma_validas += temp
        total_validas += 1
    else:
        print("Erro: Temperatura fora dos limites de segurança (-50°C a 150°C)!")
        descartados += 1

print('-' * 30)
print(f"Medições processadas com sucesso: {total_validas}")
print(f"Medições ignoradas por segurança: {descartados}")
if total_validas > 0:
    media = soma_validas / total_validas
    print(f"Média das temperaturas válidas: {media:.2f}°C")
else:
    print("Nenhuma temperatura válida foi registrada para calcular a média.")

