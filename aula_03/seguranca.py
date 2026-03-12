senha_correta = 'admin123'
tentativas = 0

while tentativas < 3:
    senha_digitada = input(f'Tentativa {tentativas + 1} - Digite a senha:  ')

    if senha_digitada == senha_correta:
        print('Acesso Concedido!')
        break
    else:
        print('Senha Incorreta!')
        tentativas = tentativas + 1
        if tentativas == 3:
            print('Conta bloqueada apos 3 tentativas')