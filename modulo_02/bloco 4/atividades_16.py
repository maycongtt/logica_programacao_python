alunos = []
medias = []
situacao = []


for i in range (5):

    aluno = input ("digite seu nome: ")
    media = int(input("digite sua nota: "))

    alunos.append(aluno)
    medias.append(media)

    if media >= 7:
        situacao.append("aprovado")
        
    elif media >= 5:
        situacao.append("recuperação")
        
    else:
        situacao.append("reprovado")
        

print(f"aprovados: {situacao.count("aprovado")}")
print(f"recuperação: {situacao.count("recuperação")}")
print(f"reprovado: {situacao.count("reprovado")}")