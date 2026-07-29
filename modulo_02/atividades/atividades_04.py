print("1 - Novo cadastro")
print("2 - Consultar cadastro")
print("3 - Atualizar cadastro")
print("4 - Remover cadastro")
print("_ - Opcao invalida")

sistema_cadastro = int(input("Escolha uma opcao"))

match sistema_cadastro:

    case 1:
        print("Novo cadastro.")
        
    case 2:
        print("Consultar cadastro")
     
    case 3:
        print("Atualizar cadastro")
    
    case 4:
        print("Remover cadastro")
        
    case _:
        print("opcao invalida")    
        
print ("cabou")        