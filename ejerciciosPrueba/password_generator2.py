#string = ('abcdefghijklmnopqrsstvuwxyz')

import string
import random


## characters to generate password from
characters = list(string.ascii_letters + string.digits + "+-%$&#")
#characters = list('abcdefghijklmnopqrsstvuwxyz' + '1234567890' + "!@#$%^&*()")
def generate_random_password():
	## length of password from the user
	length = int(input("Enter password length: "))

	## shuffling the characters
	random.shuffle(characters)
	
	## picking random characters from the list
	password = []
	for i in range(length):
		password.append(random.choice(characters))

	## shuffling the resultant password
	random.shuffle(password)

	## converting the list to string
	## printing the list
	print("".join(password))



## invoking the function
generate_random_password()

#----------