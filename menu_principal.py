



from menu_votacao import menu_votacao
from menu_gerenciamento import menu_gerenciamento

def menu_principal():
    print("Menu principal")
    
    opcao = ""
    
    while opcao != "0":
        print("=" * 50)
        print("Sistema de votação digital")
        print("=" * 50)
        print("1- Módulo de gerenciamento")
        print("2- Módulo de votação")
        print("0- Sair")
        print("=" * 50)
        
        opcao = input("Escolha uma opção:").strip()
        
        if opcao == "1":
           menu_gerenciamento()
        
        elif opcao == "2":
            menu_votacao()
        
        elif opcao == "0":
            print("\nEncerrando o sistema...")
        
        else:
            print("\nOpção inválida!")                
 
menu_principal()            
