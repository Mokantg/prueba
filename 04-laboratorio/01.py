pacientes = [['Pedro', 1.78], ['Constanza', 1.56], ['Amanda', 1.62], ['Dario', 1.89], ['Fernanda', 1.67]]

lista1,lista2,lista3,lista4,lista5 = pacientes

#A
def estatura_min():
    estatura_min = min(pacientes, float)
    print(f'La estatura mínima entre los pacientes es: {estatura_min}')

#B
def insertar():
    new= ['Ricardo', [1.71]]
    pacientes.append(new)
    print(pacientes)

#C
def encontrar():
    buscar = 'Dario'
    for buscar in pacientes:
        if buscar == True:
            print(lista4)
        else:
            print('No fue posible encontrar el paciente')

#D
estatura_min()
insertar()
encontrar()