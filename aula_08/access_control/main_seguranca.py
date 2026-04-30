from seguranca import registrar_acesso, IDS_AUTORIZADOS


def exibir_menu():
    print("\n" + "=" * 45)
    print("       SISTEMA DE CONTROLE DE ACESSO CPD")
    print("=" * 45)
    print("  [1] Registrar Acesso")
    print("  [2] Consultar Histórico de um Funcionário")
    print("  [3] Exibir Resumo do Dia")
    print("  [4] Sair")
    print("=" * 45)


def exibir_resumo(base_acessos):
    """
    Mostrar quantos funcionários acessaram o sistema
    e os respectivos horários de acesso.
    """
    print("\n" + "-" * 45)
    print("         RESUMO DE ACESSOS DO DIA")
    print("-" * 45)

    if not base_acessos:
        print("  Nenhum acesso registrado até o momento.")
    else:
        print(f"  Total de funcionários que acessaram: {len(base_acessos)}\n")
        for id_func, horario in base_acessos.items():
            print(f"   {id_func:8} → {horario}")

    print("-" * 45)


def consultar_historico(base_acessos):
    """
    Consulta o último acesso de um funcionário.
    Trata o erro (KeyError) se o ID nunca acessou o sistema.
    """
    id_busca = input("\n  Digite o ID para consulta: ").strip().upper()

    try:
        horario = base_acessos[id_busca]
        print(f"\n  ✅ Último acesso de {id_busca}: {horario}")
    except KeyError:
        # Erro tratado: ID existe na empresa mas nunca acessou o CPD
        print(f"\n  ❌ Erro: O funcionário '{id_busca}' nunca acessou o sistema.")


def main():
    # Dicionário central de acessos do dia: { ID: horário }
    base_acessos = {}

    print("\n  Sistema iniciado. IDs autorizados carregados:", len(IDS_AUTORIZADOS))

    while True:
        exibir_menu()
        opcao = input("  Escolha uma opção: ").strip()

        if opcao == "1":
            id_digitado = input("\n  Digite o ID do funcionário: ")
            autorizado, mensagem = registrar_acesso(base_acessos, id_digitado)
            print(f"\n  {mensagem}")

        elif opcao == "2":
            consultar_historico(base_acessos)

        elif opcao == "3":
            exibir_resumo(base_acessos)

        elif opcao == "4":
            print("\n  Sistema encerrado. Até logo! 👋\n")
            break

        else:
            print("\n  ⚠️  Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()