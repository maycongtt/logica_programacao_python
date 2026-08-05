usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

while usuario != "admin" or senha != "python123":
    print ("usuario ou senha incorreta. tente novamente!")
    
    usuario = input("digite seu usuario: ")
    senha = input("digite sua senha: ")
    
print ("Login realizado com sucesso!")