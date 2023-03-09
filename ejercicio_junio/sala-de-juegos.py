edad = int(input('TU EDAD: '))

if edad < 4:
    print('Entras Gratis')
elif edad >= 4 and edad <= 18:
    print('PAGAS 5$')
elif edad > 18:
    print('PAGAS 10$')
