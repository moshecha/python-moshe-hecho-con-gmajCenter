
nota = int(input('su nota '))

if nota > 0 and nota <= 10:
    print('Nota ok')
else:
    print('no valida')

while nota < 0 and nota >= 10:
    print('incorrrecto')
