#Biobio
habitantes1 = 1556805
superficie1 = 23890

#Los Lagos
habitantes2 = 828708
superficie2 = 48583

#A
censo2017 = {
    'ID': {8, 10},
    'Nombre': {'BioBío', 'Los Lagos'},
    'Superficie (km2)': {'8°': superficie1, '10°': superficie2},
    'Habitantes (2017)': {'8°': habitantes1, '10°': habitantes2}
}

print('Censo del 2017:\n',censo2017)

#B
densidad1 = habitantes1/superficie1
densidad2 = habitantes2/superficie2

densidad = {
    'BioBío densidad': {round(densidad1, 1)},
    'Los Lagos densidad': {round(densidad2, 1)}    
}

censo2017.update(densidad)
#C
capital = {
    'BioBío capital' : 'Concepción',
    'Los Lagos capital': 'Puerto Montt'
}

censo2017.update(capital)

#D
comunas = {
    'BioBío comunas' : {'Lota', 'Lebu', 'Los Angeles'},
    'Los Lagos comunas': {'Castro', 'Puerto Varas', 'Purranque'}
}

censo2017.update(comunas)

#E
provincia= {
    'Biobio provincias': ('Biobío', 'Arauco', 'Concepción'),
    'Los lagos provincias': ('Osorno', 'Llanquihue', 'Chiloé')
}

censo2017.update(provincia)
#F
print('\nCenso del 2017 actualizado:\n',censo2017)