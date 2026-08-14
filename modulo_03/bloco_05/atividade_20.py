def calcular_media(notas):
  return(sum(notas)/len(notas))


def classificar(media):
    if media >=7:
        return 'aprovado'
    elif media >=5:
        return 'recuperação'
    return 'reprovação'

notas = []
for i in range(4):
    notas.append(float(input(f"Digite {i+1} nota: ")))
    
media = calcular_media(notas)
print(f"o aluno esta: {classificar(media)}")