def registrar_equipamento(estoque, id_serial, informacoes):
    # Padronizacao da chave
    id_limpo = id_serial.strip().upper()
    estoque[id_limpo] = informacoes

def listar_setores_unicos(estoque):
    setores = set()
    for info in estoque.values():
        setores.add(info['setor'].upper())
    return sorted(list(setores))
