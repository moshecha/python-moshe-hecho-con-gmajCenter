verduras = {
    'papa': 100,
    'zanahoria': 120,
    'remolacha': 145,
    'lechuga': 200,
    'endivia': 230,
    'calabaza': 201,
    'cebolla': 322
}

print('VERDURAS DISPONIBLES Y SUS PRECIOS:')

for clave, valor in verduras.items():
    print(" %s: $%s/kg." % (clave, valor))


total = 0
verdura = ''
cantidad = 1
verduras_elegidas = []
valor = ''
kilos = 0
a = ''
lista_totales = []
while verdura != '0':
    verdura = input(' INGRESE una verdura: ')

    if (verduras.get(verdura)):
        cantidad = int(input('  INGRESE cantidad en KG: '))
        total_unidad = cantidad * (verduras.get(verdura))
        total += total_unidad
        verduras_elegidas.append(verdura)  # agrega a una lista
        kilos += cantidad
        print(
            f"    Verdura elegida: {verdura} ${verduras[verdura]}/kg X {cantidad}kg = ${total_unidad}, Total hasta aqui: ${total}  ")
        a = (
            f"{verdura} ${verduras[verdura]}/kg X {cantidad}kg = ${total_unidad}")
        lista_totales.append(a)
    elif verdura == '0':
        print('----Fin de la compra----')

    else:
        print('---verdura no disponible!')


# print('   VERDURAS ELEGIDAS:')
# for i in verduras_elegidas:
#     print('    ', i)

print('   RESUMEN:')
for e in lista_totales:
    print('    ', e)

print(f" Total a pagar: ${total} ({kilos}kg en total )")


frutas = {}

fruta = input('ingrese una fruta: ')
precio = int(input('ingrese el precio de fruta: '))
frutas[fruta] = precio


for clave, valor in frutas.items():
    print(" %s: $%s/kg." % (clave, valor))
