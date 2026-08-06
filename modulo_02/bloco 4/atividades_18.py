notas = []
nome_aluno = []

for numero in range(10):
    nome = input("digite o nome do aluno: ")
    nome_aluno.append(nome)
    
    nota = float(input("digite sua nota: "))
    notas.append(nota)
    
    

notas.sort()
print(f"todas as notas em crescente: {notas}")

notas.sort(reverse=True)
print(f"todas as notas em descrente: {notas} ")

maior = max(notas)
print(f"maior nota: {maior}")

menor = min(notas)
print(f"menor nota: {menor}")

media = sum(notas) / len(notas)
print(f"media da turma: {media}")