info_socios = {'Socio no. 1':('Amanda Nuñez', 'Ingreso: 17/03/2009', 'cuota al dia'),
               'Socio no. 2': ('Barbara Molina', 'Ingreso: 17/03/2009', 'cuota al dia'),
               'Socio no. 3':('Lautaro Campos', 'Ingreso: 17/03/2009', 'cuota al dia'),
               'Socio no. 4': ('Daniel Valencia', 'Ingreso: 13/03/2018', 'deudor')}

print(info_socios)

contador = len(info_socios)
print(f'El numero de socios es {contador}')

ingre_num_socio = input('Ingresa el numero de socio: ')

for b in info_socios:
    if b == ingre_num_socio:
        # Acceder a la tupla actual del socio específico
        info_socio = info_socios[b]
        # Crear una nueva tupla con el valor actualizado
        info_socios[b] = (info_socio[0], info_socio[1], 'cuota al dia')

print(info_socios)

fecha_vieja = 'Ingreso: 13/03/2018'
fecha_nueva = input('Ingrese la fecha de ingreso: ')

for socio, datos in info_socios.items():
    if datos[1] == fecha_vieja:
        info_socios[socio] = (datos[0], fecha_nueva, datos[2])

print(info_socios)

nombre_apellido = input('Ingrese el nombre y apellido del socio a dar de baja (formato: Nombre Apellido): ')

# Buscar y eliminar el socio con el nombre y apellido proporcionado
socio_a_eliminar = None
for clave, datos in info_socios.items():
    if datos[0] == nombre_apellido:
        socio_a_eliminar = clave
        break

if socio_a_eliminar:
    del info_socios[socio_a_eliminar]
    print(f'El socio {nombre_apellido} ha sido dado de baja.')
else:
    print(f'No se encontró ningún socio con el nombre {nombre_apellido}.')

print(info_socios)