livros = []

while True:
    print("\n===== SISTEMA DE GERENCIAMENTO DE LIVROS =====")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Pesquisar livro")
    print("4 - Atualizar disponibilidade")
    print("5 - Remover livro")
    print("6 - Encerrar")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Título: ")
        autor = input("Autor: ")
        ano = int(input("Ano de publicação: "))

        livro = {
            "titulo": titulo,
            "autor": autor,
            "ano": ano,
            "disponibilidade": "Disponível"
        }

        livros.append(livro)
        print("Livro cadastrado com sucesso!")

    elif opcao == "2":
        if len(livros) == 0:
            print("Nenhum livro cadastrado.")
        else:
            print("\n--- Lista de Livros ---")
            for livro in livros:
                print(f"Título: {livro['titulo']}")
                print(f"Autor: {livro['autor']}")
                print(f"Ano: {livro['ano']}")
                print(f"Disponibilidade: {livro['disponibilidade']}")
                print("-" * 30)

    elif opcao == "3":
        titulo = input("Digite o título do livro: ")
        encontrado = False

        for livro in livros:
            if livro["titulo"].lower() == titulo.lower():
                print("\nLivro encontrado:")
                print(f"Título: {livro['titulo']}")
                print(f"Autor: {livro['autor']}")
                print(f"Ano: {livro['ano']}")
                print(f"Disponibilidade: {livro['disponibilidade']}")
                encontrado = True
                break

        if not encontrado:
            print("Livro não encontrado.")

    elif opcao == "4":
        titulo = input("Digite o título do livro: ")
        encontrado = False

        for livro in livros:
            if livro["titulo"].lower() == titulo.lower():
                nova_disponibilidade = input(
                    "Nova disponibilidade (Disponível/Indisponível): "
                )
                livro["disponibilidade"] = nova_disponibilidade
                print("Disponibilidade atualizada com sucesso!")
                encontrado = True
                break

        if not encontrado:
            print("Livro não encontrado.")

    elif opcao == "5":
        titulo = input("Digite o título do livro que deseja remover: ")
        encontrado = False

        for livro in livros:
            if livro["titulo"].lower() == titulo.lower():
                livros.remove(livro)
                print("Livro removido com sucesso!")
                encontrado = True
                break

        if not encontrado:
            print("Livro não encontrado.")

    elif opcao == "6":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida! Tente novamente.")