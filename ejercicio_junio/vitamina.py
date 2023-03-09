nombre = input('Como te llamas? ')
oreo = input('Comes Oreo?')
frutas = input('Comes frutas?')
verduras = input('Comes Verduras')

if oreo == 'si' and frutas == 'no' and verduras == 'no':
    print('Te faltan vitaminas y tenes 1000 carbohidratos!!!')
elif oreo == 'no' and frutas == 'si' and verduras == 'si':
    print('Vida Sana!!!! Tenes Vitaminas pero un poco de carbohidratos no te haria mal')
else:
    print('Estas masomenos')
