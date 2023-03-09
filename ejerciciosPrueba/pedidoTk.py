from fpdf import FPDF
from datetime import date

def fecha():
    today = date.today()  # Para la fecha
    return (f'{format(today.day)}/{format(today.month)}/{(today.year)}')



# empieza pdf
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()

nombre_cliente = 'Jorge niuvery'
class PDF(FPDF):

    def header(self):
        self.set_font('Arial', 'B', 18)
        self.multi_cell(w=0, h=7, txt=(f"Pedido     {fecha()}     {nombre_cliente} "), border=0,
                        align='C', fill=0)  # , ln=1
        self.ln(5)  # linea vacia


pdf = PDF()
pdf.alias_nb_pages()

pdf.add_page()


pedido = 'Este es el pedido'
nombre_cliente = 'Jorge niuvery'
direccion = 'calle uruguay'
localidad = 'Mar del plata'
provincia = 'Buenos dias'
cp = '1214'
telefono = 'Tel: 12344321'
dni = 'DNI: 098778987'
transporte = 'compania aerea'
paquetes = '100'

etiqueta = (f"Nombre: {nombre_cliente}      {telefono}     {dni}\nDireccion: {direccion} / {localidad} / {provincia} ({cp})\nTransporte: {transporte}     Cant: {paquetes} paquetes ")

pdf.set_font('Arial', '', 12)
pdf.multi_cell(w=0, h=7, txt=(f"Pedido \n{pedido}"), border=1,
               align='L', fill=0)  # pedido
pdf.ln(5)  # linea vacia
pdf.set_font('Arial', 'B', 14)
for i in range(5):
    pdf.multi_cell(w=0, h=10, txt=(f"{etiqueta}"), border='TB',
                   align='C', fill=0)  # etiqueta envio
    pdf.ln(5)

# pdf.multi_cell(w = 100, h = 7, txt = (f"{etiqueta}"), border = 1,
#          align = 'L', fill = 0) #etiqueta envio

pdf.output('pedido.pdf', 'F')
