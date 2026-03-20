
def celcius_para_fahrenheit(celcius):
    fahrenheit = celcius * 1.8 + 32
    return fahrenheit

#uso de funcao
temp_c = float(input('Qual a temperatura em Celsius: '))
resultado = celcius_para_fahrenheit(temp_c)

print(f'A temperatura {temp_c}ºC em fahrenheit é {resultado}ºF ')
