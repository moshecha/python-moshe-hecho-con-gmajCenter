import webbrowser

f = open('holamundo.html','w')

mensaje = """<html>
<head></head>
<body><p>Hola Mundo!</p></body>
input('hola')
</html>"""



f.write(mensaje)
f.close()

nombreArchivo = 'file:///Users/familiachami/Desktop/python_Moshe/HTML/' + 'holamundo.html'
webbrowser.open_new_tab(nombreArchivo)

