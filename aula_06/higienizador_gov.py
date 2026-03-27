def limpar_nome(nome_bruto):
    palavras = nome_bruto.split()
    return ' '.join(palavras).title()

def limpar_cpf(cpf_bruto):
    return cpf_bruto.strip().replace('.', '').replace('-', '')[:11]

def validar_salario(valor_texto):
    limpo = valor_texto.replace("R$", "").replace(".", "").replace(",", ".").strip()
    return float(limpo)

def mascarar_nome(nome_limpo):
    partes = nome_limpo.split()
    if len(partes) < 2:
        return nome_limpo
    primeiro_nome = partes[0]
    sobrenome = partes[-1]
    return f"{primeiro_nome} {sobrenome[0]}."