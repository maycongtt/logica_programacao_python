nome = input ("digite seu nome: ")
altura = float(input("digite sua altura: "))
peso = float(input("digite seu peso: "))

imc = peso / (altura * altura)

if imc >= 40:
    print("obesidade grau III")
elif imc >= 35:
    print("obesidade grau II")
elif imc >= 30:
    print("obesidade grau I") 
elif imc >= 25:
    print("sobrepeso")
elif imc >= 20:
    print("peso normal")          
else:
    print("abaixo do peso")
    
print("Jornal encerrado")