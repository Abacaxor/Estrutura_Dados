# Modulo de Decisao
temperatura = float(input("Informe a temperatura atual do sensor (ºC): "))

if temperatura > 80.0:
    status = "CRÍTICO: Desligamento Imediato!"
elif temperatura > 50.0:
    status = 'ALERTA: Resfriamento Ativado'
else:
    status = 'NORMAL: Operacao Estável'

print(f'Diagnostico: {status}')