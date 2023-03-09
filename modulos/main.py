from funciones import suma, resta
import funciones

num_a = int(input(' Ingrese numero a: '))
num_b = int(input(' Ingrese numero a: '))

print('sumas:', funciones.suma(num_a, num_b))
print('resta:', funciones.resta(num_a, num_b))


print(suma(num_a, num_b))
print(resta(num_a, num_b))
