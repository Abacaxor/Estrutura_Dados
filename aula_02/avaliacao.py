# Entradas
nome_servidor = str(input("Qual o nome do servidor? "))
uso_cpu = float(input("Qual o uso de um CPU(%)? "))
uso_memoria = int(input("Qual o uso de um memoria(%)? "))

# Logica de Classificacao
if uso_cpu > 90 or uso_memoria > 32:
    status = 'Prioridade Critica'
elif 70 <= uso_cpu <= 90:
    status = 'Alta Carga'
else:
    status = 'Carga Normal'

# Output
print(f''' --- Prioridade do servidor: {nome_servidor} ---
Uso do CPU: {uso_cpu:.2f}%
Uso da memoria: {uso_memoria:.2f}%
Status final: {status}
''')
