dados = {}

dados["nome"] = input ("Digite seu nome: ")
dados["cargo"] = input ("Digite seu cargo: ")
dados["setor"] = input ("Digite seu setor: ")
dados["salario"] = input ("Digite seu salario: ")

for chave, valor in dados.items():
    print(f"{chave} : {valor}")
    
remover_chave = input("Digite o chave que quer remover: ")

if remover_chave in dados:
    dados.pop(remover_chave)
    for chave, valor in dados.items():
        print(f"{chave} : {valor}")
    
else:
    print("Chave não cadastrada")