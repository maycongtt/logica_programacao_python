# Cadastre três contatos em uma lista de dicionários, armazenando nome, telefone e e-mail. Em seguida, solicite ao usuário o nome de um contato, pesquise-o na lista e apresente seus dados. Caso o contato não seja encontrado, informe ao usuário.

lista = [
    {"nome": "jose",
     "telefone": "(99)99999-9999",
     "email": "aaaaa123@gmail.com",
     },
    
    {"nome": "maria",
     "telefone": "(77)77777-7777",
     "email": "bbbbb123@gmail.com",
     },
    {"nome": "carlos",
     "telefone": "(89)99999-9999",
     "email": "ccccc123@gmail.com",
     },
    
]


contatos = input("digite o contato desejavel: ")
for i in lista:
    if i ["nome"] == contatos:
        print ("encontrado!!!")
        break
        
    else:
        print ("Dados informado nao encontrado.")