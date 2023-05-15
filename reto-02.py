#Trabajo realizado con Aylin Oyarzún

enombre=input('Ingrese el nombre del estudiante:\n')
anombre=input('Ingrese nombre de la asignatura:\n')
nota1=float(input('Ingrese primera nota\n'))
nota2=float(input('Ingrese segunda nota\n'))

promedio=(nota1*0.30)+(nota2*0.70)


diccionario_nota= {
        'Nombre Alumno' : enombre,
        'Nombre Asignatura' : anombre,
        'Nota laboratorio 1' : nota1,
        'Nota laboratorio 2' : nota2,
        'Promedio ponderado' : round(promedio, 1)
}

print(diccionario_nota)
