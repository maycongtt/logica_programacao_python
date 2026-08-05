produtos = []
estoques = []

for nome in range(5):
    produto = input(f"Digite nome dos produtos: ")
    produtos.append(produto)
    
    estoque = int(input(f"digite a quantidadeque aida tem: "))
    estoques.append(estoque)
    
print("\nProdutos com quantidade infeiro ou gua a cinco: ")
    
for i in range(len(produtos)):
    if estoques [i] <=5:
        print(f"{produtos[i]}: {estoques}")


