import sys
from tkinter import *

lista_aleatoria = []

def es_palindromo(x):
    return x == x[::-1]

def no_es_palindromo(x):
    return x != x[::-1]

lista_de_palindromos = list( filter( es_palindromo, lista_aleatoria ) )


lista_de_no_palindromos = list( filter( no_es_palindromo, lista_aleatoria ) )




###
def hacer_click():
 lista_aleatoria = []
 #lista_de_no_palindromos = list( filter( no_es_palindromo, lista_aleatoria ) )  
 #lista_de_palindromos = list( filter( es_palindromo, lista_aleatoria ) )
 try:
  _valor = (entrada_texto.get())
  lista_aleatoria.append(_valor)
  lista_de_palindromos = 'Palindromos:',list( filter( es_palindromo, lista_aleatoria ) )
  lista_de_no_palindromos = 'No Palindromos:',list( filter( no_es_palindromo, lista_aleatoria ) )
  etiqueta.config(text=lista_de_palindromos)
  etiqueta2.config(text=lista_de_no_palindromos)
  etiqueta3.config(text=lista_aleatoria)
  
 except ValueError:
  etiqueta.config(text="Introduce un numero!")


def total (_valor,lista):
 try:
  lista.append(_valor)
  etiqueta3.config(text=lista)
 except ValueError:
  etiqueta.config(text="Introduce un numero!")
  
app = Tk()
app.title("Verificar Palabra Si Es Palindromo")



#Ventana Principal
vp = Frame(app)
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

etiqueta = Label(vp, text="Palindromos")
etiqueta.grid(column=1, row=2, sticky=(W,E))

etiqueta2 = Label(vp, text="No Palindromos")
etiqueta2.grid(column=1, row=3, sticky=(W,E))

etiqueta3 = Label(vp, text="Palabras Ingresadas")
etiqueta3.grid(column=1, row=4, sticky=(W,E))

boton = Button(vp, text="Verificar!", command=hacer_click)
boton.grid(column=2, row=1)

boton2 = Button(vp, text="Todas!", command=total)
boton2.grid(column=2, row=2)


valor = ""
entrada_texto = Entry(vp, width=10, textvariable=valor)
entrada_texto.grid(column=1, row=1)

app.mainloop()

root = Tk()                     # Creamos la ventana de fondo
                                # Creamos una lista con nombres
li = []
li.append(entrada_texto)
li = []
listb = Listbox(root)           # Creamos un Widgets Listbox
for item in li:                 # Insertamos los nombres de la lista en el Listbox
    listb.insert(0,item)

listb.pack()                    # Hacemos el pack del widget
root.mainloop()   

