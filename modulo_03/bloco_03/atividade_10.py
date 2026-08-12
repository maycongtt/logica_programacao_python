produtos = {}

produtos["nome"] = input("Digite o nome: ")
produtos["preço"] = input("Digite o valor do preço: ")
produtos["quantidade"] = input("Digite a quantidade: ")

for chave, valor in produtos.items():
    print (f"{chave} : {valor}")
    
produtos["categoria"] = input("Digite a categoria: ")
produtos["preço"] = input("Digite valor do preço: ")
produtos["estoque"] = input("Digite quantidade que tem no estoque: ")

for chave, valor in produtos.items():
    print (f"{chave} : {valor}")