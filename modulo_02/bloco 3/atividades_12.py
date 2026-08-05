alunos = [
    "Ana",
    "Carlos",
    "Maria",
    "Pedro",
    "Lucas", 
]

busca_aluno = input("digite o nome do aluno que voçe procura: ")

for i, aluno in enumerate(alunos):
    if busca_aluno.lower() == aluno.lower():
        print(f"Aluno encontrado na posição{i}!")
        break
    if busca_aluno.lower() != aluno.lower():
        print("aluno nao encontrado!")