from datetime import datetime

# Lista Literal de IDs Autorizados (Usamos SET para busca rápida O(1))
# Dica: O ID é a chave para o CPD
IDS_AUTORIZADOS = {"ADM01", "TEC02", "ENG03", "SUP04"}


def obter_horario_atual():
    """
    Retorna uma string com a data e hora atual formatada.
    """
    agora = datetime.now()
    # Formato: Dia/Mês/Ano Hora:Minuto:Segundo
    return agora.strftime("%d/%m/%Y %H:%M:%S")


def registrar_acesso(base_acessos, id_func):
    """
    Verifica autorização e registra no dicionário de acessos.

    Parâmetros:
        base_acessos (dict): Dicionário que armazena {ID: horário}.
        id_func (str): O ID do funcionário a ser verificado.

    Retorna:
        tuple: (bool, str) → (sucesso, mensagem)
    """
    id_func = id_func.strip().upper()

    if id_func in IDS_AUTORIZADOS:
        horario = obter_horario_atual()
        # O ID é a chave (único e imutável), o horário é o valor
        base_acessos[id_func] = horario
        return True, f"✅ Acesso Autorizado em: {horario}"
    else:
        return False, "⚠️  ACESSO NEGADO: ID não consta na lista de autorizados."
