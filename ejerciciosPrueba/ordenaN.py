

numeros = [1,2,3,4,5,6,7,8,9,0,2,3,9,8,7,6,5,4,3,2,1,0]
numeros2 = [1,2,3,4,5,6,7,8,9,0,2,3,9,8,7,6,5,4,3,2,1,0]

numeros.sort()
numeros = str(numeros)
print("".join(numeros))

numeros2.sort(reverse=True)
numeros2 = str(numeros2)
print("".join(numeros2))

letras = ['q','qe','f','n','1','4','2']
#letras = str(letras)


letras.sort()
print("," .join(letras))

lista = list()
letras2 = "q,w,e,r,t,y,u,i,o,p,l,k,j,h,g,f,d,s,a,z,x,c,v,b,n,m,"
h = letras2.replace(',','')
print(' '.join(h))
for i in h:
    lista.append(i)
lista.sort()

print (" " .join(lista))#\n