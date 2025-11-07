# Función especifica para poder obtener los datos dentro de .csv
import csv
from config import CSV

def analisis_csv():
    # Listas para recolectar datos del .csv
    gastos = []
    meses = []
    años = []
    categorias = []
    dias = [] # nueva lista
    descripciones = [] # nueva lista
    
    with open(CSV,'r') as archivo:
        lector = csv.DictReader(archivo)
        
        for fila in lector:
            gastos.append(float(fila['precio'].strip()))
            dias.append(int(fila['dia'].strip())) # ahora se recibe el dia de los gastos
            meses.append(int(fila['mes'].strip()))
            años.append(int(fila['año'].strip()))
            categorias.append(fila['categoria'].strip().lower()) 
            descripciones.append(fila['descripcion'].strip().lower()) # Se agrego la columna descripcion
    
    return gastos,dias,meses,años,categorias,descripciones