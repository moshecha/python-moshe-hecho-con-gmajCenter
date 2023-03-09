from tkinter import *

def contarpalabras(a):
    a = a.split()
    a = len(a)
    return print('---',a,'Palabras contadas en la frase')

def guardafrase (a,b):
    c = open(a, 'a')
    c.write(b + '\n')
    c.close()
    return print('--Frase Ingresada:',b)

def contarfrases(a):
    archivo = open(a)
    cant_frases =0
    
    for lineas in archivo:
        cant_frases += 1
    print('---En el archivo hay', cant_frases, 'frases')#cuantas frases hay?

def contarpalabrasArchivo(a):
    numpalabras = 0
    simbolos = ['¿', '?', '.', ',', ';', ':', '¡', '!']
    with open(a) as fichero:
        for linea in fichero:
                for simbolo in simbolos:
                    # remplaza los simbolos por espacios
                    linea = linea.replace(simbolo, ' ')
                palabras = linea.split()  # hace una lista de palabras

                for palabra in palabras:
                    numpalabras += 1
    print('---En el archivo hay', numpalabras, 'palabras')#cuantas palabras hay en el archivo?
    
    
def imprimirFrases(a):
    print(' FRASES EN EL ARCHIVO --')
    archivo = open(a)
    for lineas in archivo:
        print ('-', lineas)
        
'''
frase = input('ingrese frase: ')
archivo = 'archivo.txt'
guardafrase(archivo,frase)
contarpalabras(frase)
contarpalabrasArchivo(archivo)
contarfrases(archivo)
imprimirFrases(archivo)

'''



archivo = 'archivo.txt'
###
def hacer_click():
 try:
  _valor = (entrada_texto.get())
  
  etiqueta.config(text=_valor)
  guardafrase(archivo,_valor)
  contarpalabras(_valor)
  contarpalabrasArchivo(archivo)
  contarfrases(archivo)
  imprimirFrases(archivo)
  
 except ValueError:
  etiqueta.config(text="Introduce un numero!")


app = Tk()
app.title("Mi segunda App Grafica")

#Ventana Principal
vp = Frame(app)
vp.grid(column=0, row=0, padx=(500,500), pady=(100,100))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

etiqueta = Label(vp, text="Frase ingresada")
etiqueta.grid(column=2, row=2, sticky=(W,E))

boton = Button(vp, text="Guardar!", command=hacer_click)
boton.grid(column=1, row=1)

valor = ""
entrada_texto = Entry(vp, width=10, textvariable=valor)
entrada_texto.grid(column=2, row=1)

app.mainloop()