# Calculo de Faturamento
cliente = 'Tech Solutions'   # str
projeto_ativo = True         # bool
valor_hora = 150.50          # float
horas_trabalhadas = '40'     # str (simulando dado de um arquivo ou banco)

# Erro proposital: O que acontece se tentarmos multiplicar str por float?
# Precisa-se converter 'horas_trabahadas' para int ou float
total_faturamento = valor_hora * int(horas_trabalhadas)

print(f'Cliente: {cliente} | Projeto Ativo: {projeto_ativo}')
print(f'Faturamento Mensal: R$ {total_faturamento:.2f}')
