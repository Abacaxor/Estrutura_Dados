def normalizar_cidade(cidade_bruta):
    """
    Remove espaços em branco e padroniza o nome da cidade.
    Ex: "  são paulo  " -> "São Paulo"
    """
    cidade_limpa = cidade_bruta.strip().title()
    return cidade_limpa

# Teste de Caixa Preta
entrada_usuario = input('Digite a cidade: ')
cidade_final = normalizar_cidade(entrada_usuario)
print(f'Cidade Registrada: "{cidade_final}"'    )