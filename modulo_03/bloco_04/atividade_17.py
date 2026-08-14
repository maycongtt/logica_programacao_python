# Lista de dicionários com os estudantes
estudantes = [
    {"nome": "Ana", "idade": 20, "curso": "Engenharia"},
    {"nome": "Bruno", "idade": 22, "curso": "Direito"},
    {"nome": "Carla", "idade": 19, "curso": "Medicina"}
]

# Solicita o nome do estudante
nome_estudante = input("Digite o nome do estudante que deseja remover: ")

# Procura o estudante
encontrado = False

for estudante in estudantes:
    if estudante["nome"].lower() == nome_estudante.lower():
        encontrado = True

        confirmacao = input(
            f"Tem certeza que deseja remover {estudante['nome']}? (S/N): "
        )

        if confirmacao.lower() == "s":
            estudantes.remove(estudante)
            print("Estudante removido com sucesso!")
        else:
            print("Remoção cancelada.")

        break

# Caso o estudante não seja encontrado
if not encontrado:
    print("Estudante não encontrado.")

# Exibe os registros restantes
print("\nLista de estudantes:")
for estudante in estudantes:
    print(
        f"Nome: {estudante['nome']}, "
        f"Idade: {estudante['idade']}, "
        f"Curso: {estudante['curso']}"
    )