from aula_04.temperatura import resultado
from mapeamento_ativos import *

base_equipamentos = {}

while True:
    print('\n1. Registrar Ativo | 2. Consultar por ID | 3. Relatorio de Setores | 4 Sair')
    opcao = input('Escolha: ')

    if opcao == '1':
        serial = input('Serial do Equipamento: ')
        nome = input('Nome do Equipamento: ')
        setor = input('Setor Responsavel: ')

        dados_tecnicos = {'nome': nome, 'setor': setor, 'serial': serial}
        print(registrar_equipamento(base_equipamentos, serial, dados_tecnicos))

    elif opcao == '2':
        busca = input('Digite o Serial para busca: ').strip().upper()
        resultado = base_equipamentos.get(busca)
        if resultado:
            print(f'Localizado: {resultado['nome']} no setor {resultado["setor"]}')
        else:
            print('Equipamento nao encontrado')

    elif opcao == '3':
        print(f'Setores Atendidos: {listar_setores_unicos(base_equipamentos)}')

    elif opcao == '4':
        break

