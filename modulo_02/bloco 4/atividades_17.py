produtos = []

while True: 
    produto = input("digite o nome do produto ou (fim) para encerrar: ")    
    
    if produto == "fim":   
        break
    
    produtos.append(produto)


item = input("Nome do item procurado: ")    

if item in produtos:
    print(f"O produto esta na lista, sua posição é: {produtos.index(item)}")
else:
    print(f"O item procurado não esta na lista")


    

