import pandas as pd 
import csv 
  
headerList = ['Nombre', 'Apellido', 'Direccion', 'Telefono', 'Fecha Inscripcion', 'ID'] 
  
from datetime import date
import uuid
ID = uuid.uuid1(51)
#ID = ID[:10]

today = date.today()  # Para la fecha

nombre = input('Nombre: ')
apellido = input('Apellido: ')
direccion = input('Direccion: ')
numero = input('Telefono: ')
fecha = (f'{format(today.day)}/{format(today.month)}/{(today.year)}')

  
  
  
with open("hola.csv", 'a+') as csvfile: 
    dw = csv.DictWriter( csvfile, delimiter=',',  
                        fieldnames=headerList) 
    
    dw.writeheader() 
    dw.writerow({'Nombre':' '+ nombre[:10], 'Apellido': apellido,
                    'Direccion': direccion, 'Telefono': numero, 'Fecha Inscripcion': fecha, 'ID': ID})
    #dw.writerow( nombre,  apellido,
                #     direccion,  numero,  fecha,  ID)
#fileContent = pd.read_csv("hola.csv") 
#fileContent 



