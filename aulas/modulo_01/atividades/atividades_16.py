nome_produto = input("Digite o nome do produto: ")
preco_unitario = float(input("Digite o preço unitário: "))
quantidade = int(input("Digite a quantidade: "))
percentual_desconto = float(input("Digite o desconto: "))

subtotal = preco_unitario * quantidade
valor_desconto = subtotal * percentual_desconto / 100
total = subtotal - valor_desconto

print (f"\nO Subtotal é: {subtotal}")
print (f"O valor do desconto é: {valor_desconto}")
print (f"O total da compra: {total}")
print (f"A quantidade é maior que zero?: {quantidade > 0}")
print (f"O total é maior que 100?: {total > 100}")
print (f"No nome do produto contém a letra 'A'?: {'A' in nome_produto}")
print (f"Desconto é diferente de 'None? '{percentual_desconto is not None}")