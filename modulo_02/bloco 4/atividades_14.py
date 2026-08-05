produtos = []

for nome in range (10):
    produto = input(f"Digite o nome {nome + 1}º dos produtos: ") 
    produtos.append(produto)
    
produtos.sort()

print(produtos)