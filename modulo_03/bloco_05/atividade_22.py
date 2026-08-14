def buscar_produto(produtos, nome):
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            return produto
        return None
    
produtos = [
    {"nome" : "mesa",
     "preço": "100,00",
     "quantidade": "350"},
    
    {"nome" : "cadeira",
     "preço" : "45,00",
     "quantidade" : "80"},
    
    {"nome" : "faca",
     "preço" : "12,00",
     "quantidade" : "600"},
    
]

nome_busca = input ("Digite o nome do produto")

resultado = buscar_produto(produtos, nome_busca)

if resultado is not None:
    print("produto encontrado:")
    for chave, valor in resultado.items():
        print(f"{chave}: {valor}")

else: 
    print("produto não encontrado: ")
    