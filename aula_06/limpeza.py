def limpar_moeda(valor_sujo):
    """
    Transforma uma string monetária em um float puro.
    Ex: " R$ 1.500,50 " -> 1500.50
    """
    # Pipeline: Remove espaços, remove R$, troca ponto por nada e vírgula por ponto
    valor_limpo = valor_sujo.strip().replace("R$", "").replace(".", "").replace(",", ".")
    return float(valor_limpo)

def extrair_lote(codigo_venda):
    """
    Extrai o número do lote de um código de venda padrão.
    Padrão: "VENDA-2023-LOTE99-BR" -> "LOTE99"
    """
    partes = codigo_venda.split("-")
    # O lote é sempre a terceira parte do código
    return partes[2].upper().strip()

def validar_cupom(cupom):
    """
    Verifica se o cupom segue a regra: 10 caracteres, começa com 'DESC'
    e termina com números.
    """
    cupom = cupom.strip().upper()
    if len(cupom) == 10 and cupom.startswith("DESC") and cupom[4:].isnumeric():
        return True
    return False

def formatar_relatorio_venda(id_venda, valor):
    """
    Gera uma linha de log formatada para o sistema de auditoria.
    """
    return f"COMPROVANTE_VIRTUAL | ID: {id_venda} | VALOR_FINAL: BRL {valor:.2f}"