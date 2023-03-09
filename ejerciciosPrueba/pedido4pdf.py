from fpdf import FPDF
from datetime import date
from pedido4Tk import *

pdf = FPDF(orientation='P', unit='mm', format='A4')

pdf.add_page()

if paquetes.get() == '':
    paquetes.set(1)
etiqueta = (f" Nombre: {nombre.get().title()}  Tel: {telefono.get()} DNI: {dni.get()} \nDireccion: {direccion.get()} / {localidad.get()} / {provincia.get()} ({cp.get()}) \nTransporte: {transporte.get()}   Cantidad: {paquetes.get()}  ")


pdf.set_font('Arial', '', 12)
pdf.multi_cell(w=0, h=7, txt=(f"Pedido \n{pedido.get()}"), border=1,
            align='L', fill=0)  # pedido
pdf.ln(5)  # linea vacia

cant_etiquetas =int( paquetes.get())
pdf.set_font('Arial', 'BI', 14)
for i in range(cant_etiquetas):
    pdf.multi_cell(w=0, h=10, txt=(f"{etiqueta}"), border='TB',
                   align='C', fill=0)  # etiqueta envio
    pdf.ln(5)

pdf.output('pedidoTk.pdf', 'F')

#A = subprocess.call(["open",'/Users/familiachami/Desktop/python_Moshe/pedidoTk.pdf' ])
