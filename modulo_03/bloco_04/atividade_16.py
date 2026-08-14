# Lista de dicionários com os produtos
produtos = [
    {"nome": "Notebook", "preco": 3500.00, "quantidade": 10},
    {"nome": "Mouse", "preco": 80.00, "quantidade": 50},
    {"nome": "Teclado", "preco": 150.00, "quantidade": 20}
]

# Solicita o nome do produto
nome_produto = input("Digite o nome do produto que deseja atualizar: ")

# Procura o produto na lista
encontrado = False

for produto in produtos:
    if produto["nome"].lower() == nome_produto.lower():
        nova_quantidade = int(input("Digite a nova quantidade em estoque: "))
        produto["quantidade"] = nova_quantidade
        encontrado = True
        print("Quantidade atualizada com sucesso!")
        break

# Caso o produto não seja encontrado
if not encontrado:
    print("Produto não encontrado.")

# Exibe os dados atualizados
print("\nLista de produtos atualizada:")
for produto in produtos:
    print(
        f"Nome: {produto['nome']}, "
        f"Preço: R$ {produto['preco']:.2f}, "
        f"Quantidade: {produto['quantidade']}"
    )