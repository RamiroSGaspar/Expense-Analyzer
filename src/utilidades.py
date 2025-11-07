# Funciones de apoyo
def pedir_año(año_min=1900, año_max=2100):
    while True:
        x = input("Ingresa el año: ").strip() # Se ingresa primero en str para aplicar la funcion len()
        if len(x) != 4 or not x.isdigit(): # Se verifica si cumple con el formato y si contiene digitos
            print("Error: el año debe tener formato 0000 (4 dígitos).")
            continue

        # Se convierte y se verifica el rango
        try: año = int(x)
        except ValueError:
            print("Error: el año no es un número válido.")
            continue

        if año_min <= año <= año_max: return año
        else: print(f"Error: el año debe estar entre {año_min} y {año_max}.")
        
def pedir_mes():
    while True:
        try:
            mes = int(input("Ingresa el mes: "))
            if mes >= 1 and mes <= 12:
                return mes
            else: print("Error: el mes debe ser valido")
        except ValueError: print("Error: ingreso no valido")
        
# Diccionario util para graficar:
nombres_meses = {1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo",
    6:"Junio", 7:"Julio", 8:"Agosto", 9:"Septiembre",
    10:"Octubre", 11:"Noviembre", 12:"Diciembre"}