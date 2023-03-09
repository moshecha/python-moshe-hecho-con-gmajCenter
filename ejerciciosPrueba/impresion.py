from reportlab.pdfgen import canvas

from reportlab.lib.pagesizes import A4

w, h = A4
c = canvas.Canvas("hola-mundo.pdf", pagesize=A4)
c.drawString(50, h - 50, "¡Hola, mundo!")
#c.showPage() #crea una nueva pagina

c.setFont("Helvetica", 10)
c.drawString(300, h - 50, "¡Hola, mundo!")
c.setFont("Times-Roman", 20)
c.drawString(130, h - 50, "¡Hola, mundo!")

x = 50
y = h - 100
c.line(x, y, x + 200, y)#crea una linea

c.rect(200, h - 350, 350, 200)# crea un rectangulo
c.roundRect(300, h - 300, 300, 200, 10)#rectangulo esquinas redondeadas

c.ellipse(400, h - 50, x + 150, y - 50) #ovalo


c.showPage()#nueva pag

nombre = 'Jorge'#input('nombre: ')
texto1 = 'Una vez hecho esto, procedemos a configurar'
texto2=  'A partir del objeto creado los distintos estilos. '
numeros = '0123456789'
etiqueta1 = (f"{nombre[:30]}\n {nombre[30:]}\n {texto1[:43]}\n {texto1[50:]}\n {texto2[:43]}\n \n{numeros}{numeros}{numeros}1234567\nTotal 37 caracteres\n------------")

x=50
text = c.beginText(40, h - 50)
text.setFont("Times-Roman", 14)
#text.textLines(f"{nombre}\n {texto1}\n {texto2}\n¡Desde ReportLab y Python!\n{numeros}{numeros}{numeros}")

text.textLines(etiqueta1)
text.textLines(etiqueta1)
text.textLines(etiqueta1)
text.textLines(etiqueta1)
text.textLines(etiqueta1)
text.textLines(etiqueta1)

c.drawText(text)

nombre = input('Nombre: ')
apellido = input('Apellido: ')
lugar = input('Lugar: ')
contacto = (f"{nombre} \n {apellido} \n {lugar} \n ---- ")

text = c.beginText(310, h - 50)
text.setFont("Times-Roman", 14)

text.textLines(contacto)

for i in range (3):
    nombre = input('Nombre: ')
    apellido = input('Apellido: ')
    lugar = input('Lugar: ')
    contacto = (f"{nombre} \n {apellido} \n {lugar} \n ---- ") 
    text.textLines(contacto)

c.drawText(text)

c.save()

