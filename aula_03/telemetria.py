print('--- Analista de Telemetria ---')

qtd_altitude = int(input('Quantas medidas de altitude deseja fazer? '))
pico_altitude = 0
total_alertas = 0

for qtd in range(1, qtd_altitude + 1):
    altitude = float(input(f'Qual a altura nº {qtd}: '))
    if altitude > pico_altitude:
        print('----------- Novo Pico de Altitude Máximo! -----------')
        pico_altitude = altitude

    if altitude > 100:
        print('Alerta de Risco!')
        total_alertas += 1
print('-' * 30)
print(f'Maior pico registrado {pico_altitude}')
print(f'Quantidade de alertas de risco: {total_alertas}')

