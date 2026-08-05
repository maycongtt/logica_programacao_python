#Entrada
total_segundos = int(input("Digite os segundos: "))

#Cálculos
horas = total_segundos // 3600
resto = total_segundos % 3600

minutos = resto // 60
segundos = resto % 60

#Saídas
print (f'{horas} hora')
print (f'{minutos} minutos')
print (f'{segundos}segundos')