def nombres(n):
    nombres= []
    c=0
    for i in range(n):
        nom = input(f'ingrese el {i+1}° nombre: ')
        nombres.append(nom)
        c=c+len(nom)
    print(nombres)
    print(f'Cantidad de caracteres total: {c}')



n= int(input('Cuantos nombres desea ingresar:\n'))
nombres(n)
