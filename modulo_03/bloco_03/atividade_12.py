livro = {}

livro["Titulo"] = input("Digite o titulo: ")
livro["Autor"] = input("Digite o autor: ")
livro["Ano"] = input("Digite o Ano: ")
livro["Categoria"] = input("Digite a categoria que deseja: ")

for chave, valor in livro.keys():
    print (f"{chave} : {valor}")
    
for chave, valor in livro.values():
    print (f"{chave} : {valor}")
    
for chave, valor in livro.items():
    print (f"{chave} : {valor}")