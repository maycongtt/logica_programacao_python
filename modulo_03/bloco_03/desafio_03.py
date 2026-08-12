Cadastro = {}

Cadastro = [titulo] = input("informe o titulo do livro: ")
Cadastro = [autor] = input("informe o autor: ")
Cadastro = [ano] = input("informe o ano do livro: ")
Cadastro = [paginas] = input("informe a quantidade de paginas: ")
Cadastro = [disponibilidade] = input("Informe se está 'disponivel' ou 'indisponivel': ")

print ("1 - consultar uma informação")
print ("2 - alterar um valor")
print ("2 - adicionar novas informaçoes")
print ("4 - remover informação")
print ("5 - visaulizar todo o cadastro")
print ("6 - encerrar o programa")

while True:
    opcao = int(input("digite a opcao desejada: "))
    if opcao == 6:
        print("programa encerrado!")
