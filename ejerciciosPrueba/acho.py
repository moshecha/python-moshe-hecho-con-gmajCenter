f = open ('/Users/familiachami/Desktop/python_Moshe/pedidoTk.pdf','r')

import sys
import subprocess

# """#Clase heredada de QMainWindow (Constructor de ventanas)"""
# def abrirTabla(this):
#         this.openFile(r'/Users/familiachami/Desktop/python_Moshe/pedidoTk.pdf') 

#     #Abrir tabla AWG
# def openFile(this, file):
#         if sys.platform == 'darwin':
#             #MacOSx detectado
#             subprocess.call(["open", file])

# abrirTabla('/Users/familiachami/Desktop/python_Moshe/pedidoTk.pdf')

#subprocess.call(["open",'/Users/familiachami/Desktop/python_Moshe/pedidoTk.pdf' ])

# import aspose.words as aw

# doc = aw.Document("Input.pdf")
# builder = aw.DocumentBuilder(doc)

# # Insertar texto al principio del documento.
# builder.move_to_document_start()
# builder.writeln("Morbi enim nunc faucibus a.")
# doc.update_page_layout()

# doc.save("Output.pdf")