notas = []


for numero in range(4):
    nota = int(input("Digite sua nota: "))
    notas.append(nota)

print(f" Todas as notas: {notas}\n maior nota: {max(notas)}\n menor nota: {min(notas)}\n média da turma: {sum(notas) / len(notas)}")