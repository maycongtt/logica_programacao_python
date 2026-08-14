produtos = []

for i in range (2):
    nome = input(f"Digite o nome do {i+1}º produto: ")
    categoria = input("Digite a categoria do produto: ")
    preco = float(input("Digite o preço do produto: "))
    estoque = int(input("Digite a quantidade que resta no estoque: "))
    
    produto = {
        "nome": nome,
        "categoria": categoria,
        "preço": preco,
        "estoque": estoque,    
    }
    
    produtos.append(produto)
    

for produto in produtos:
    print(f"Nome do produto {produto["nome"]}")
    print(f"qual a categoria do produto {produto["categoria"]}")
    print(f"preço {produto["preço"]}")
    print(f"quantidade no estoque {produto["estoque"]}")