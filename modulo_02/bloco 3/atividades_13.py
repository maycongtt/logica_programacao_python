produtos = []

while True:
    print("MENU")
    print("Adicionar produto")
    print("Remover produto")
    print("Listar produtos")
    print("Encerrar")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            produto = input("Digite o nome do produto: ").lower()
            produtos.append(produto)
            print(f"Produto '{produto}' adicionado com sucesso!")

        case "2":
            produto = input("Digite o nome do produto a remover: ").lower()
            if produto in produtos:
                produtos.remove(produto)
                print(f"Produto '{produto}' removido com sucesso!")
            else:
                print("Produto não encontrado!")

        case "3":
            if produtos:
                print("\nLista de produtos:")
                for i, produto in enumerate(produtos, start=1):
                    print(f"{i}. {produto}")
            else:
                print("Nenhum produto cadastrado.")

        case "4":
            print("Programa encerrado.")
            break

        case _:
            print("Opção inválida! Tente novamente.")