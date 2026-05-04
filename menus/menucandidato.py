candidatos = []  


def cadastrar_candidato():
    
    nome = input("Nome do candidato: ")
    numero = input("Número do candidato: ")
    partido = input("Partido: ")

    for c in candidatos:
        if c["numero"] == numero:
            print("Erro: Já existe candidato com esse número!")
            return

    candidato = {
        "nome": nome,
        "numero": numero,
        "partido": partido
    }

    candidatos.append(candidato)
    print("Candidato cadastrado com sucesso!")


def listar_candidatos():
   
    if not candidatos:
        print("Nenhum candidato cadastrado.")
        return

    print("\nLista de candidatos:")
    for c in candidatos:
        print(f"Nome: {c['nome']} | Número: {c['numero']} | Partido: {c['partido']}")


def buscar_candidato():
  
    numero = input("Digite o número do candidato: ")

    for c in candidatos:
        if c["numero"] == numero:
            print("Candidato encontrado:")
            print(f"Nome: {c['nome']} | Número: {c['numero']} | Partido: {c['partido']}")
            return

    print("Candidato não encontrado.")


def editar_candidato():
 
    numero = input("Digite o número do candidato para editar: ")

    for c in candidatos:
        if c["numero"] == numero:
            novo_nome = input("Novo nome do candidato: ")
            novo_numero = input("Novo número do candidato: ")
            novo_partido = input("Novo partido: ")

            for candidato in candidatos:
                if candidato["numero"] == novo_numero and candidato != c:
                    print("Erro: Já existe candidato com esse número!")
                    return

            c["nome"] = novo_nome
            c["numero"] = novo_numero
            c["partido"] = novo_partido

            print("Candidato editado com sucesso!")
            return

    print("Candidato não encontrado.")


def remover_candidato():
  
    numero = input("Digite o número do candidato para remover: ")

    for c in candidatos:
        if c["numero"] == numero:
            candidatos.remove(c)
            print("Candidato removido com sucesso!")
            return

    print("Candidato não encontrado.")


def menu_candidato():
  
    opcao = ""

    while opcao != "6":
        print("\n=== MENU DE CANDIDATOS ===")
        print("1 - Cadastrar candidato")
        print("2 - Listar candidatos")
        print("3 - Buscar candidato")
        print("4 - Editar candidato")
        print("5 - Remover candidato")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_candidato()
        elif opcao == "2":
            listar_candidatos()
        elif opcao == "3":
            buscar_candidato()
        elif opcao == "4":
            editar_candidato()
        elif opcao == "5":
            remover_candidato()
        elif opcao == "6":
            print("Saindo do menu...")
        else:
            print("Opção inválida!")


menu_candidato()
