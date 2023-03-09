import string
import random


## Aca estan los caracteres
alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("+-%$&#")
characters = list(string.ascii_letters + string.digits + "+-%$&#")

def generate_random_password():
	## ingreso de cantidad de digitos
	length = int(input("Ingrese cantidad de caracteres en la clave: "))

	## ingreso de tipo de caracteres
	alphabets_count = int(input("Cuantas letras quieres que contenga?: "))
	digits_count = int(input("Cuantos digitos?: "))
	special_characters_count = int(input("Cuantos caracteres especiales?: "))

	characters_count = alphabets_count + digits_count + special_characters_count

	## check the total length with characters sum count
	## print not valid if the sum is greater than length
	if characters_count > length:
		print("pediste mas caracteres que el total de la clave!")
		return


	## initializing the password
	password = []
	
	## picking random alphabets
	for i in range(alphabets_count):
		password.append(random.choice(alphabets))


	## picking random digits
	for i in range(digits_count):
		password.append(random.choice(digits))


	## picking random alphabets
	for i in range(special_characters_count):
		password.append(random.choice(special_characters))


	## if the total characters count is less than the password length
	## add random characters to make it equal to the length
	if characters_count < length:
		random.shuffle(characters)
		for i in range(length - characters_count):
			password.append(random.choice(characters))


	## shuffling the resultant password
	random.shuffle(password)

	## converting the list to string
	## printing the list
	print('Clave: ', "".join(password))



## invoking the function
generate_random_password()