quantidade = 0 
total = 0

venda = float(input("digite o valor da venda ou (0 para encerrar): "))

if venda != 0:
    maior = venda
    menor = venda
    
while venda != 0:
    quantidade += 1
    total += venda
    
    if venda > maior:
        maior = venda
        
    if venda < menor:
        menor = venda
        
    venda = float(input("digite o valor da venda(0 para encerrar): "))
    
if quantidade > 0:
    media = total / quantidade
    
    print("relatorio de vendas")
    print(f"quantidade de vendas: {quantidade}")
    print(f"valor total vendido: {total:.2f}")
    print(f"valor medio das vendas: {media:.2f}")
    print(f"maior venda: {maior}")
    print(f"menor venda: {menor}")
    
else:
    print("nenhuma venda foi registrada.")