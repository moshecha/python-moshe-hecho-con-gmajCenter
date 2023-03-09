def verificar(letra):
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        return ('VOCAL OK')
    else:
        return ('Consonante')


#letra = input('ingrese una vocal: ')
veces = 0
letra = []
letras_ing = [1, 2, 2]
while letra != '0' and veces < 10:
    letra = input('ingrese una vocal: ')
    print(veces, verificar(letra))
    veces += 1
    letras_ing = letras_ing, letra
print(letras_ing)

