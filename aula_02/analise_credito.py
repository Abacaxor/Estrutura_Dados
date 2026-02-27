# Sistema de Aprovacao de Credito
print('--- analise de Risco de Credito ---')

renda_mensal = float(input('Renda mensal: R$ '))
valor_parcela = float(input('Valor parcela: R$ '))
limite_percentual = 0.30 # 30% de renda

# Decisao Composta
if valor_parcela > (renda_mensal * limite_percentual):
    status = "CREDITO NEGADO: Parcela compromete mais de 30% da renda."
elif renda_mensal < 2000:
    status = 'CREDITO EM ANALISE: Renda abaixo do minimo para aprovacao direta'
else:
    status = 'Credito Aprovado'

print(f'Resultado da Avaliacao: {status}')