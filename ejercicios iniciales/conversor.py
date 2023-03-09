dolares = int(input('ingrese cantidad de dolares:   '))
pais = input('ingrese su pais:   ')
mensaje = 'tus dolares son igual a: $'

if (pais == 'Argentina'):
    dolares = dolares * 200
    print(mensaje, dolares)

elif (pais == 'Colombia'):
    dolares = dolares*3950
    print(mensaje, dolares)

elif (pais == 'Bolivia'):
    dolares = dolares*100
    print(mensaje, dolares)
else:
    print('pais no valido')
