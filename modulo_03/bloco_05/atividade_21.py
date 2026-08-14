def cadastrar_produto(nome, preco, quantidade):
    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }
    return produto

# Entrada de dados
nome = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: R$ "))
quantidade = int(input("Digite a quantidade em estoque: "))


produto = cadastrar_produto(nome, preco, quantidade)


print("\n=== Cadastro do Produto ===")
print(f"Nome: {produto['nome']}")
print(f"Preço: R$ {produto['preco']:.2f}")
print(f"Quantidade em estoque: {produto['quantidade']}")