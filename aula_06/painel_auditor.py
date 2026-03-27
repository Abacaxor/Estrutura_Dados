from higienizador_gov import *

print("--- Sistema de Higienização Governamental ---")
nome_digitado = input("Digite o Nome completo: ")
cpf_digitado = input("Digite o CPF: ")
salario_digitado = input("Digite o Salário Base: ")

try:
    nome_limpo = limpar_nome(nome_digitado)
    nome_final = mascarar_nome(nome_digitado)

    cpf_final = limpar_cpf(cpf_digitado)[:11]


    salario_base = validar_salario(salario_digitado)
    salario_com_reajuste = salario_base * 1.10

    print("\n" + "="*40)
    print("      RELATÓRIO DE PROCESSAMENTO")
    print("="*40)
    print(f"Nome Mascarado: {nome_final.title()}")
    print(f"CPF Limpo:      {cpf_final}")
    print(f"Salário Atual:  R$ {salario_base:,.2f}")
    print(f"Salário + 10%:  R$ {salario_com_reajuste:,.2f}")
    print("="*40)

except ValueError:
    print("\n[ERRO] Falha ao processar o salário. Certifique-se de digitar um valor numérico válido.")
except Exception as e:
    print(f"\n[ERRO INESPERADO] {e}")