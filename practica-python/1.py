trabajadores=[['Juan',[700000, 650000, 690000] ],['Maria', [681000, 710000, 590000]], ['Pedro', [590000, 635000, 705000]]]
lista1, lista2, lista3 = trabajadores

l1, l2 =lista1
l3, l4 = lista2
l5, l6 = lista3

def promedio_sueldo():
    p1 = sum(l2)/len(l2)
    print(f'El promedio de sueldo de {l1} es: {round(p1, 2)}')
    p2 = sum(l4)/len(l4)
    print(f'El promedio de sueldo de {l3} es: {round(p2, 2)}')
    p3 = sum(l6)/len(l6)
    print(f'El promedio de sueldo de {l5} es: {round(p3, 2)}')

def sueldo_max():
    print(f'Sueldo máximo de Juan: {max(l2)}')
    print(f'Sueldo máximo de Maria: {max(l4)}')
    print(f'Sueldo máximo de Pedro: {max(l6)}')

def honorarios():
    impuesto1 = (sum(l2))*0.1225
    print(f'honoarios de {l1} : {round(impuesto1,0)}')
    impuesto2 = (sum(l4))*0.1225
    print(f'honoarios de {l3} : {round(impuesto2,0)}')
    impuesto3 = (sum(l6))*0.1225
    print(f'honoarios de {l5} : {round(impuesto3,0)}')



promedio_sueldo()
print('\n')
sueldo_max()
print('\n')
honorarios()