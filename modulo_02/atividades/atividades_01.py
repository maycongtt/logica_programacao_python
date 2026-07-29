idade = int(input("Digite sua idade: "))

if idade >= 20:
    print("maior de idade.")
    print("pode realizar o cadastro.")

elif idade >= 17:
    print("menor de idade.")
    print("acesso negado.")

else:
    print("de menor.")
    print("acesso negado.")

print("programa encerrado") 