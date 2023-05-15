print("Mayor entre 3 números enteros\n")

n1= int(input("Ingrese primer número: "))
n2= int(input("Ingrese segundo número: "))
n3= int(input("Ingrese tercer número: "))

if n1>n2:
    if n1>n3:
        print("El número mayor es: ",n1)
    else:
        print("El número mayor es: ",n3)
else:
    if n2>n3:
        print("El número mayor es: ",n2)
    else:
        print("El número mayor es: ", n3)