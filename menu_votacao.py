def menu_votacao() -> None:
    opcao = ""
    
    while opcao != "0":
        print("=" * 50)   
        print("Módulo de votação")
        print("=" * 50)   
        print("1- Abrir sistema de votação")
        print("2- Auditoria de votção")
        print("3- Resultados da votação")
        print("0- Voltar")
        print("=" * 50)   

        opcao = input("Escolha uma opção:").strip()
        
        if opcao == 1:
            menu_abertura_votacao()
        
        elif opcao == 2:
            menu_auditoria()
        
        elif opcao == 3:
            menu_resultados()        
        
        elif opcao == 0:
            print("\nVoltando...")
        
        else:
            print("Opção inválida!")    

menu_votacao()        