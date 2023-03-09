from datetime import date
from tkinter import *
import subprocess

def fecha():
    today = date.today()  # Para la fecha
    return (f'{format(today.day)}/{format(today.month)}/{(today.year)}')

def click_boton():
    A = subprocess.call(["open",'/Users/familiachami/Desktop/python_Moshe/pedidoTk.pdf' ])


root = Tk()
root.geometry('500x500')
root.title('Pedido')

def click_boton2():
    etiqueta = Label(f" Nombre: {nombre.get().title()}  Tel: {telefono.get()} DNI: {dni.get()} \nDireccion: {direccion.get()} / {localidad.get()} / {provincia.get()} ({cp.get()}) \nTransporte: {transporte.get()}   Cantidad: {paquetes.get()}  ").pack()





nombre = StringVar()
frame1 = Frame()
frame1.pack()
Label(frame1, text='Nombre', font='arial 12 bold').pack(side=LEFT)
Entry(frame1, textvariable=nombre, width=50).pack()

direccion = StringVar()
frame2 = Frame()
frame2.pack()
Label(frame2, text='Direcciion', font='arial 12 bold').pack(side=LEFT)
Entry(frame2, textvariable=direccion, width=50).pack()

localidad = StringVar()
frame3 = Frame()
frame3.pack()
Label(frame3, text='Localidad', font='arial 12 bold').pack(side=LEFT)
Entry(frame3, textvariable=localidad, width=50).pack()

provincia = StringVar()
frame4 = Frame()
frame4.pack()
Label(frame4, text='Provincia', font='arial 12 bold').pack(side=LEFT)
Entry(frame4, textvariable=provincia, width=50).pack()

cp = StringVar()
frame5 = Frame()
frame5.pack()
Label(frame5, text='Cp', font='arial 12 bold').pack(side=LEFT)
Entry(frame5, textvariable=cp, width=50).pack()

telefono = StringVar()
frame6 = Frame()
frame6.pack()
Label(frame6, text='Telefono', font='arial 12 bold').pack(side=LEFT)
Entry(frame6, textvariable=telefono, width=50).pack()

dni = StringVar()
frame7 = Frame()
frame7.pack()
Label(frame7, text='DNI', font='arial 12 bold').pack(side=LEFT)
Entry(frame7, textvariable=dni, width=50).pack()

transporte = StringVar()
frame8 = Frame()
frame8.pack()
Label(frame8, text='Transporte', font='arial 12 bold').pack(side=LEFT)
Entry(frame8, textvariable=transporte, width=50).pack()

paquetes = StringVar()
frame9 = Frame()
frame9.pack()
Label(frame9, text='Paquetes', font='arial 12 bold').pack(side=LEFT)
Entry(frame9, textvariable=paquetes, width=50).pack()

pedido = StringVar()
frame10 = Frame()
frame10.pack()
Label(frame10, text='Pedido', font='arial 12 bold').pack(side=LEFT)
Entry(frame10, textvariable=pedido, width=50).pack()

boton1 = Button(root,
                text="Imprimir",
                command=click_boton).pack()
boton2 = Button(root,
                text="boton2",
                command=quit).pack()
#boton2 = Button(root, text="Salir", command=quit) .pack()
 ##fin Tk
root.mainloop()

