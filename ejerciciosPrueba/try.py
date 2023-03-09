'''
from cmd import IDENTCHARS

h=True
while h:
    try:
        f = int(input('pone numero: '))
        print('ok')
        h=False
    except:
        print('algo salio mal')
        pass
'''
from tkinter import Tk,ttk, Label, Button
class VentanaEjemplo:
    def __init__(self, master):
        self.master = master
        master.title("Una simple interfaz gráfica")
        self.etiqueta = Label(master, text="Esta es la primera ventana!")
        self.etiqueta.pack()
        self.botonSaludo = Button(master, text="Saludar", command=self.saludar)
        self.botonSaludo.pack()
        self.botonCerrar = Button(master, text="Cerrar", command=master.quit)
        self.botonCerrar.pack()
        
    def saludar(self):
        saludo = ttk.Label(text="Hola Mundo")
        saludo.place(x=20, y=20)
       
root = Tk()
miVentana = VentanaEjemplo(root)

root.mainloop()