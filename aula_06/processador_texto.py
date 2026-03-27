def limpar_cpf(cpf_bruto):
    # Remove pontuacoes e espacos de um cpf
    return cpf_bruto.replace('.', '').replace('-', '')

def formatar_nome_projeto(nome_bruto):
    # Remove os espacos extras e aplica title case.
    palavras = nome_bruto.split()
    return ' '.join(palavras).title()

def mascarar_cpf(cpf_limpo):
    # Retorna o CPF no formato de mascara de privacidade
    parte1 = cpf_limpo[:3]
    parte2 = cpf_limpo[-2:]
    return f'{parte1},***.***-{parte2}'

def extrair_dominio(email):
    # Extrai o dominio de um e-mail
    posicao = email.find('@') + 1
    return email[posicao:].lower().strip()
