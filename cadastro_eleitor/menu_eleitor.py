def menu_eleitor():
    print("\nVocê entrou no modulo de Eleitor!")
    print("Menu do eleitor")

    opcao = ""
    
    while opcao != "0":
        print("=" * 50)
        print("Gerenciamento de Eleitores")
        print("=" * 50)
        print("1- Cadastrar eleitor")
        print("2- Edição de eleitor")
        print("3- Remoção de eleitor")
        print("4- Busca de eleitores")
        print("5- Listar eleitores")
        print("0- Voltar")
        print("=" * 50)
        
        
        opcao = input("Digite uma opcão:").strip()
        
        if opcao == "1":
            print ("\nCadastro de eleitor")
        
        elif opcao == "2":
            print("\nEdição de eleitor") 
            
        elif opcao == "3":
            print("\nRemoção de eleitor")        
        
        elif opcao == "4":
            print("\nBusca de eleitores")        
            
        elif opcao == "5":
            print("\nListagem de eleitores")        
        
        elif opcao == "0":
            print("\nVoltando...")        
        
        else:
            print("\nOpção inválida!")
            


if __name__ == "__main__":
    menu_eleitor()      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    