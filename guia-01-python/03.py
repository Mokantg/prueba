horas_diurno = 10
horas_nocturno = 10

tarifa_diurna = 12000
tarifa_nocturna = 16000

domingo_d= 2000
domingo_n= 3000


if domingo_d:
        tarifa_diurna = tarifa_diurna + domingo_d
elif domingo_n:
        tarifa_nocturna= tarifa_nocturna + domingo_n

pagar_diurno = horas_diurno * tarifa_diurna
pagar_nocturno = horas_nocturno * tarifa_nocturna

pago1= (pagar_diurno*2) + (pagar_nocturno*3)
pago2= (pagar_diurno*1) + (pagar_nocturno*3) + domingo_d
pago3= (pagar_diurno*3) + (pagar_nocturno*2) + domingo_n

empleado_1 = {
    'Turnos' : {'Lunes' : 'Nocturno', 'Martes' : 'Nocturno', 'Miercoles' : 'Nocturno', 'Jueves' : 'Diurno', 'Viernes' : 'Diurno'},
    'Pago Diario' : {'Lunes' : pagar_nocturno, 'Martes' : pagar_nocturno, 'Miercoles' : pagar_nocturno, 'Jueves' : pagar_diurno, 'Viernes' : pagar_diurno},
    'Pago Semanal' : pago1

}

empleado_2 = {
    'Turnos' : {'Martes' : 'Nocturno', 'Miercoles' : 'Nocturno', 'Jueves' : 'Nocturno', 'Domingo' : 'Diurno'},
    'Pago Diario' : {'Lunes' : pagar_nocturno, 'Martes' : pagar_nocturno, 'Miercoles' : pagar_nocturno, 'Jueves' : pagar_diurno, 'Viernes' : pagar_diurno},
    'Pago Semanal' : pago2

}

empleado_3 = {
    'Turnos' : {'Miercoles' : 'Diurno', 'Jueves' : 'Diurno', 'Viernes' : 'Diurno', 'Sabado' : 'Nocturno', 'Domingo' : 'Nocturno'},
    'Pago Diario' : {'Lunes' : pagar_nocturno, 'Martes' : pagar_nocturno, 'Miercoles' : pagar_nocturno, 'Jueves' : pagar_diurno, 'Viernes' : pagar_diurno},
    'Pago Semanal' : pago3

}
print('Empleado 1:\n', empleado_1)
print('Empleado 2:\n', empleado_2)
print('Empleado 3:\n', empleado_3)