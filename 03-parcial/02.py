a = input("Ingrese el nombre de la primera asignatura: ")
notas1 = []
for i in range(3):
    nota = float(input(f"Ingrese la nota {i+1} de laboratorio para {a}: "))
    while nota < 1 or nota > 7:
        nota = float(input("Ingrese una nota válida: "))
    notas1.append(nota)



b = input("Ingrese el nombre de la segunda asignatura: ")
notas2 = []
for i in range(3):
    nota = float(input(f"Ingrese la nota {i+1} de laboratorio para {b}: "))
    while nota < 1 or nota > 7:
        nota = float(input("La nota debe estar entre 1.0 y 7.0. Ingrese una nota válida: "))
    notas2.append(nota)


#A
def promedio_simple(notas_a):
    return sum(notas_a) / len(notas_a)

promedio1 = promedio_simple(notas1)
print(f"El promedio simple de {a} es: {round(promedio1, 1)}")

promedio2 = promedio_simple(notas2)
print(f"El promedio simple de {b} es: {round(promedio2, 1)}")

#B
def nota_minima(notas):
    return min(notas)

nota_baja1 = nota_minima(notas1)
print(f"La nota más baja de {a} es: {round(nota_baja1, 1)}")

nota_baja2 = nota_minima(notas2)
print(f"La nota más baja de {b} es: {round(nota_baja2, 1)}")

#C
def nota_maxima(notas):
    return max(notas)

nota_alta1 = nota_maxima(notas1)
print(f"La nota más alta de {a} es: {round(nota_alta1, 1)}")

nota_alta2 = nota_maxima(notas2)
print(f"La nota más alta de {b} es: {round(nota_alta2, 1)}")

#D
def promedio_final(promedio1, promedio2):
    return (promedio1 + promedio2) / 2

promedio_f = promedio_final(promedio1,promedio2)
print(f"El promedio final es: {round(promedio_f, 1)}")

