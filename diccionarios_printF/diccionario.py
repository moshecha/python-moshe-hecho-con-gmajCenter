divisas = {
    'euro': "€",
    'peso': '$',
    'dolar':  'U$D'
}

divisa = input('ingrese una divisa: ')

while divisa != '0':
    if (divisas.get(divisa)):
        print(divisas.get(divisa))
        divisa = input('ingrese una divisa: ')
    else:
        print('divisa no encontrada')
        divisa = input('ingrese una divisa: ')


print(divisas.items())
print(divisas['peso'])


print('.........')

nombre = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")
edad = input("ingrese su edad: ")
ocupacion = input("ingrese su ocupacion: ")

datos = {
    'nombre': nombre,
    'apellido': apellido,
    'edad': edad,
    'ocupacion': ocupacion
}

while ocupacion != '0':
    print(
        f"Hola {datos['nombre']} {datos['apellido']}, tienes {datos['edad']} anos! , Salud!!!! {datos['ocupacion']}")
    ocupacion = input("ingrese su ocupacion: ")
    datos = {
        'nombre': nombre,
        'apellido': apellido,
        'edad': edad,
        'ocupacion': ocupacion
    }
