print('--- Sistema de Monitoramento ---')
opcao = ''

while opcao != 'sair':
    print('\n[1] Verificar Status')
    print('[2] Reiniciar Sensores')
    print('[sair] Encerrar Programa')
    
    opcao = input('Escolha uma opcao: ').strip().lower()

    if opcao == '1':
        print('Sistemas operando normalmente.')
    elif opcao == '2':
        print('Sensores reiniciados.')
    elif opcao == 'sair':
        print('Encerrando...')
    else:
        print('Opcao Invalida!')