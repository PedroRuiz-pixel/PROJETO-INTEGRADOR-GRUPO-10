def menu_resultados():
    opcao = ""
    while opcao != "0":
        print("=" * 50)
        print("    Resultados da votação ")
        print("=" * 50)
        print("1- Boletim de Urna")
        print("2- Estatistica de Comparecimento")
        print("3- Votos por Partido")
        print("4- Validação de integridade")
        print("0- Voltar")
        print("=" * 50)

        opcao = input("Escolha uma opção: ").strip()
        
        if opcao =="1":
            print("\n[Boletim de Urna ]")

        elif opcao == "2":
            print("\n[Estatisticas de Comparecimento")
        elif opcao == "3":
            print("\n[Votos por partido ]")
        elif opcao  == "4":
            print("\n[Validação de integridade]")
        elif opcao == "0":
            print(\nVoltando...)
        else:
            print("\nOpção inválida!")
          
