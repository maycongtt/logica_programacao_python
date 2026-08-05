alunos = []
medias = []

quantidade = int(input("Quantos alunos deseja cadastrar? "))

for i in range(quantidade):
    print(f"\nCadastro do aluno {i + 1}")
    
    nome = input ("Nome: ")
    
    notas = []
    for j in range(4):
        nota = float(input(f"Digite a {j + 1}ª nota: "))
        notas.append(nota)
        
    media = sum(notas) / 4
    
    if media >= 7:
        situação = "Aprovado"
    elif media >= 5:
        situação = "Recuperação"
    else:
        situação = "Reprovado"
        
        alunos.append([nome, media, situação])
        medias.append(media)
        
    print("\n + = * 50")
    print("Relatorio da Turma")
    print("= * 50")

    for aluno in alunos:
        print(f"Nome: {aluno[0]}")
        print(f"Media Final: {aluno[2]}")
        print(f"situação: {aluno[2]}")
        print("-" * 50)
        
    maior_media = {max(medias)}
    menor_media = {min(medias)}
    media_geral = {sum(medias) / len(medias)}

print(f"maior media da turma: {maior_media:.2f}")
print(f"menor media da turma: {menor_media:.2f}")
print(f"media geral da turma: {media_geral:.2f}")        