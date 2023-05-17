nombre = input('Ingrese nombre del contacto:\n')
direccion = input('Ingrese direccion del contacto:\n')
ciudad = input('Ingrese ciudad del contacto:\n')
telefono = int(input('Ingrese el numero telefonico del contacto:\n'))


agenda = {
    'Nombre' : nombre, 
    'Direccion': direccion, 
    'Ciudad': ciudad, 
    'Numero telefonico': telefono}

print(f'Informacion del contacto: {agenda}')

facebook = input('Ingrese usuario de Facebook:\n')
insta= input('Ingrese usuario de instagram:\n')
twitter = input('Ingrese usuario de twitter:\n')

redes_sociales = {
    'Usuario Facebook': facebook, 
    'Usuario Instagram': insta, 
    'Usuario Twitter': twitter}

print(f'Usuario de Facebook: {redes_sociales["Usuario Facebook"]}')

nueva_agenda= {
    'Nombre' : nombre, 
    'Direccion': direccion, 
    'Ciudad': ciudad, 
    'Numero telefonico': telefono,
    'Usuario de Facebook': facebook
}

print(f'Esta es la nueva agenda actualizada: {nueva_agenda}')

