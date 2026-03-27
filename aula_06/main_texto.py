from processador_texto import *

print("--- SISTEMA DE SANITIZAÇÃO DE DADOS ---")

# 1. Entrada de Dados
nome_input = input("Digite o nome completo do cliente: ")
cpf_input = input("Digite o CPF (com pontos e traços): ")
email_input = input("Digite o e-mail corporativo: ")

# 2. Processamento (Chamada das funções do Módulo A)
nome_limpo = formatar_nome_projeto(nome_input)
cpf_limpo = limpar_cpf(cpf_input)
cpf_exibicao = mascarar_cpf(cpf_limpo)
dominio = extrair_dominio(email_input)

# 3. Saída Estruturada
print("\n" + "="*30)
print(f"RELATÓRIO DE CADASTRO")
print(f"Nome Oficial: {nome_limpo}")
print(f"CPF Protegido: {cpf_exibicao}")
print(f"Provedor de E-mail: {dominio}")
print("="*30)