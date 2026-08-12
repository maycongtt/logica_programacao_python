dados = {}

dados["nome"] = input("Digite seu nome: ")
dados["e-mail"] = input("Digite seu e-mail: ")
dados["cidade"] = input("Digite sua cidade: ")

chave = input("Digite o nome da chave que voce procura: ")
print (f"{dados.get(chave, 'Chave não cadastrada')}")