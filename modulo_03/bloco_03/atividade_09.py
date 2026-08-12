dados = {}

dados["nome"] = input("Digite seu nome: ")
dados["idade"] = input("Digite sua idade: ")
dados["cidade"] = input("Digite sua cidade: ")
dados["profissão"] = input ("Fale a sua profissão: ")

for chave, valor in dados.items():
    print (f"{chave} : {valor}")