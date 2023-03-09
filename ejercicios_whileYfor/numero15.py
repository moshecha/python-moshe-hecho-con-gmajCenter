a = int(input('numero 1: '))
b = int(input('numero 2: '))

if a % 2 == 0:
    for i in range(a, b+1, 2):
        print(i)
else:
    for i in range(a+1, b+1, 2):
        print(i)

