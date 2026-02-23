# Entradas
carga_esperada = float(input('Qual a quantidade de quilos que a maquina deveria produzir? '))
carga_real = float(input('Qual a quantidade que quilos que a maqina realmente produziu? '))

# Logica do negocio
eficiencia = carga_real / carga_esperada

if eficiencia < 0.7:
    status = 'Manutencao'
elif eficiencia > 0.7 and eficiencia < 0.9:
    status = 'Desempenho Regular'
else:
    status = 'Operacao Otimizada'
Z
# Output
print(f'o Indice de eficiencia da maquina e {eficiencia:.2f}, adquirindo o Status final {status}.')