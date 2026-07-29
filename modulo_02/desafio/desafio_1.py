saldo = float(input("Digite seu saldo: "))
saque = float(input("Digite o valor do seu saque: "))
novo_saldo = saldo - saque

if saldo >= saque: 
    print("saldo realizado com sucesso")
    print(f"novo saldo: R$ {novo_saldo:.2f}")
else:
    print("saldo insuficiente!")
    
print("fim da operação")