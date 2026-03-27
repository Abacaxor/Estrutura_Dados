from limpeza import *

print("=== PORTAL DE AUDITORIA DE VENDAS ===")

# 1. Coleta de dados "sujos"
cod_venda = input("Informe o código da venda (ex: VENDA-2023-LOTE05-BR): ")
valor_input = input("Informe o valor da venda (ex: R$ 1.250,00): ")
cupom_input = input("Informe o cupom de desconto: ")

# 2. Processamento via Módulo de Auditoria
try:
    valor_final = limpar_moeda(valor_input)
    lote_identificado = extrair_lote(cod_venda)

    # 3. Validação Condicional
    if validar_cupom(cupom_input):
        print("✅ Cupom válido! Aplicando 10% de desconto adicional...")
        valor_final *= 0.90
    else:
        print("⚠️ Cupom inválido ou expirado. Mantendo valor original.")

    # 4. Saída Profissional
    print("\n" + "-" * 40)
    print(formatar_relatorio_venda(lote_identificado, valor_final))
    print("-" * 40)

except Exception as e:
    print(f"❌ Erro no processamento: Verifique o formato dos dados inseridos.")