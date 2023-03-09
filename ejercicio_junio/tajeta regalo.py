tarjeta = 1000
#gasto = float(input('valor gastado: $'))
gastos = 'Tus gastos:'
while tarjeta > 0:
    gasto = int(input('valor gastado: $'))
    if gasto <= tarjeta:
        tarjeta -= gasto
        print('restan $', tarjeta)
        gasto = str(gasto)
        gastos = gastos+' $' + gasto
    else:
        print('saldo insuficiente, Te quedan $', tarjeta)


print(gastos)
