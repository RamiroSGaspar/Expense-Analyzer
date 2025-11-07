from utilidades import pedir_año, pedir_mes, nombres_meses
import matplotlib.pyplot as plt

# Funciones Graficas
def grafico_gastos_generales_plot(gastos,meses,años,dias):
    '''
    permite graficar los gastos generales
    el usuario elige si quiere ver los gastos por mes, año o años
    retorna el grafico segun la eleccion del usuario
    '''
    datos = {} # Diccionario para el manejo de valores para graficar
    
    try: 
        desicion = input("¿Que gastos quieres ver en el gráfico? (opciones: 'mes','año' o 'años'):  ").strip().lower()
        if desicion == "año":
            print("Ingresa el año donde quieres ver los gastos mensaules (Formato: 0000): ")
            año_filtro = pedir_año()
            
            for g, m, a in zip(gastos,meses,años): # Se emparejan en una tupla los valores mediante zip() y se recorren
                if a == año_filtro:
                    if m not in datos: datos[m] = g # Se agrega dentro de el diccionario la clave m (el numero del mes) y se le da como valor el gasto
                    else: datos[m] += g # Se acumula el gasto dentro de una clave ya existente
            
            if len(datos.values()) <= 1:
                print(f"\nMENSAJE: El {año_filtro} no tiene los suficientes datos para graficar")
            
            # grafica opcion: año
            elif datos:
                plt.title(f"GRAFICO ANUAL: {año_filtro} - Grafico Plot")
                datos_ordenados = dict(sorted(datos.items())) # se ordena para mostrar la linea continua
                
                plt.plot(datos_ordenados.keys(), datos_ordenados.values())
                plt.scatter(datos_ordenados.keys(), datos_ordenados.values())
                
                # Para el eje x se muestan los meses exactos, convirtiendo las claves en una lista.
                # Despues se crea una lista comprimida que genera los nombres de los meses con ayuda
                # de el diccionario nombre_meses:
                plt.xticks(list(datos_ordenados.keys()), [nombres_meses[m] for m in datos_ordenados.keys()]) 
                
                plt.yticks(list(datos_ordenados.values()))
                plt.grid(True, alpha=0.3)
                plt.xlabel("Mes")
                plt.ylabel("Gastos")
                plt.show()

        elif desicion == "años": 
            for g, m, a in zip(gastos,meses,años):
                if a not in datos: datos[a] = g
                else: datos[a] += g
            
            if len(datos.values()) <= 1:
                print(f"\nMENSAJE: No tiene los suficientes datos para graficar")
            
            # grafica opcion: años
            elif datos:
                datos_ordenados = dict(sorted(datos.items())) # se ordena datos por año
                plt.title("GRAFICO POR AÑOS - Grafico Plot")
                plt.plot(datos_ordenados.keys(), datos_ordenados.values())
                plt.scatter(datos_ordenados.keys(), datos_ordenados.values())
                plt.xticks(list(datos_ordenados.keys()))
                plt.yticks(list(datos_ordenados.values()))
                plt.grid(True, alpha=0.3)
                plt.xlabel("Año")
                plt.ylabel("Gastos")
                plt.show()
        
        # adicion: grafico plot nuevo, muestra los gastos de un mes en especifico, en un año especifico
        elif desicion == "mes":
            print("Ingresa el año donde quieres ver los gastos mensuales (Formato: 0000)")
            año_filtro = pedir_año()
            print("Ingresa el mes donde quieres ver los gastos por mes (1-12): ")
            mes_filtro = pedir_mes()
            
            for g, m, a, d in zip(gastos,meses,años,dias):
                if a == año_filtro and m == mes_filtro:
                    if d not in datos: datos[d] = g
                    else: datos[d] += g
            
            if len(datos.values()) <= 1:
                print(f"\nMENSAJE: El mes {mes_filtro} del {año_filtro} no tiene los suficientes datos para graficar")
            
            # grafica opcion: mes     
            elif datos:
                datos_ordenados = dict(sorted(datos.items())) # se ordena datos por dia
                plt.title(f"GRAFICO DEL MES: {mes_filtro}/{año_filtro} - Grafico Plot")
                plt.plot(datos_ordenados.keys(), datos_ordenados.values())
                plt.scatter(datos_ordenados.keys(), datos_ordenados.values())
                plt.xticks(list(datos_ordenados.keys()))
                plt.yticks(list(datos_ordenados.values()))
                plt.grid(True, alpha=0.3)
                plt.xlabel("Dia")
                plt.ylabel("Gastos")
                plt.show()
        
        else: print("Error. Se ingreso una palabra no valido, vuelve a intentar")
    
    except ValueError: print("Error: Se ingreso un dato invalido, vuelve a intentar")
    
def grafico_gastos_generales_barra(gastos,meses,años,dias):
    '''
    permite graficar los gastos generales
    el usuario elige si quiere ver los gastos por mes, año o años
    retorna el grafico segun la eleccion del usuario
    '''
    datos = {}
    
    try:
        desicion = input("¿Que gastos quieres ver en el gráfico? (opciones: 'mes','año' o 'años'):  ").strip().lower()
        if desicion == "año":
            print("Ingresa el año donde quieres ver los gastos mensuales (Formato: 0000)")
            año_filtro = pedir_año()
            
            for g,m,a in zip(gastos,meses,años):
                if a == año_filtro:
                    if m not in datos: datos[m] = g
                    else: datos[m] += g
            
            if len(datos.values()) <= 1:
                print(f"\nMENSAJE: El {año_filtro} no tiene los suficientes datos para graficar")
            
            elif datos:
                datos_ordenados = dict(sorted(datos.items()))
                plt.title(f"GRAFICO ANUAL: {año_filtro} - Grafico de Barras")
                plt.bar(datos_ordenados.keys(), datos_ordenados.values())
                plt.xticks(list(datos_ordenados.keys()), [nombres_meses[m] for m in datos_ordenados.keys()])
                plt.yticks(list(datos_ordenados.values()))
                plt.grid(True, alpha=0.3)
                plt.xlabel("Mes")
                plt.ylabel("Gastos")
                plt.show()
        
        elif desicion == "años":
            for g,m,a in zip(gastos,meses,años):
                if a not in datos: datos[a] = g
                else: datos[a] += g
            
            if len(datos.values()) <= 1:
                print(f"\nMENSAJE: no tiene los suficientes datos para graficar")
            
            elif datos:
                datos_ordenados = dict(sorted(datos.items()))
                plt.title("GRAFICO POR AÑOS - Grafico de Barras")
                plt.bar(datos_ordenados.keys(), datos_ordenados.values())
                plt.xticks(list(datos_ordenados.keys()))
                plt.yticks(list(datos_ordenados.values()))
                plt.grid(True, alpha=0.3)
                plt.xlabel("Año")
                plt.ylabel("Gastos")
                plt.show()
        
        elif desicion == "mes":
            print("Ingresa el año donde quieres ver los gastos mensuales (Formato: 0000)")
            año_filtro = pedir_año()
            print("Ingresa el mes donde quieres ver los gastos por mes (1-12): ")
            mes_filtro = pedir_mes()

            for g,m,a,d in zip(gastos,meses,años,dias):
                if a == año_filtro and m == mes_filtro:
                    if d not in datos: datos[d] = g
                    else: datos[d] += g
            
            if len(datos.values()) <= 1:
                print(f"\nMENSAJE: El mes {mes_filtro} del {año_filtro} no tiene los suficientes datos para graficar")
            
            elif datos:
                datos_ordenados = dict(sorted(datos.items()))
                plt.title(f"GRAFICO DEL MES: {mes_filtro}/{año_filtro} - Grafico de Barras") 
                plt.bar(datos_ordenados.keys(), datos_ordenados.values())
                plt.xticks(list(datos_ordenados.keys()))
                plt.yticks(list(datos_ordenados.values()))
                plt.grid(True, alpha=0.3)
                plt.xlabel("Dia")
                plt.ylabel("Gastos")
                plt.show()
            
        else: print("Error. Se ingreso una palabra no valido, vuelve a intentar")
        
    except ValueError: print("Error: Se ingreso un dato no valido, vuelve a intentar")
    
def grafico_gastos_por_categoria(gastos, meses, años, categorias, dias):
    '''
    permite graficar los gastos por categoria
    el usuario elige si quiere ver los gastos por mes, año o años
    retorna el grafico segun la eleccion del usuario
    '''
    datos = {}
    
    try:
        desicion = input("¿Que gastos quieres ver en el gráfico? (opciones: 'mes','año' o 'años'):  ").strip().lower()
        if desicion == "año":
            print("Ingresa el año donde quieres ver los gastos por categoría (Formato: 0000): ")
            año_filtro = pedir_año()
            
            for g, m, a, c in zip(gastos, meses, años, categorias):
                if a == año_filtro:
                    if c not in datos: datos[c] = g
                    else: datos[c] += g
                    
            if len(datos.values()) <= 1:
                print(f"\nMENSAJE: El {año_filtro} no tiene los suficientes datos para graficar")
            
            elif datos:
                plt.title(f"GASTOS POR CATEGORÍA - Año {año_filtro} - Gráfico de Barras")
                plt.bar(datos.keys(), datos.values())
                plt.xticks(rotation=45)
                plt.grid(True, alpha=0.3)
                plt.xlabel("Categorías")
                plt.ylabel("Total Gastado")
                plt.tight_layout()
                plt.show()
                
        elif desicion == "años":
            # Se encuentra el rango de años para mostrarlo en el título
            año_min = min(años)
            año_max = max(años)
            
            for g, m, a, c in zip(gastos, meses, años, categorias):
                if c not in datos: datos[c] = g
                else: datos[c] += g
            
            if len(datos.values()) <= 1:
                print(f"\nMENSAJE: no tiene los suficientes datos para graficar")
            
            elif datos:
                if año_min == año_max:
                    plt.title(f"GASTOS POR CATEGORÍA - Año {año_min} - Gráfico de Barras")
                else:
                    plt.title(f"GASTOS POR CATEGORÍA - Período {año_min}-{año_max} - Gráfico de Barras")
                
                plt.bar(datos.keys(), datos.values())
                plt.xticks(rotation=45)
                plt.grid(True, alpha=0.3)
                plt.xlabel("Categorías")
                plt.ylabel("Total Gastado")
                plt.tight_layout()
                plt.show()
        
        elif desicion == "mes":
            print("Ingresa el año donde quieres ver los gastos por categoría (Formato: 0000): ")
            año_filtro = pedir_año()
            print("Ingresa el mes donde quieres ver los gastos por categoria (1-12): ")
            mes_filtro = pedir_mes()
            
            for g, m, a, d, c in zip(gastos, meses, años, dias,categorias):
                if a == año_filtro and m == mes_filtro:
                    if c not in datos: datos[c] = g
                    else: datos[c]+= g
            
            if len(datos.values()) <= 1:
                    print(f"\nMENSAJE: El mes {mes_filtro} del {año_filtro} no tiene los suficientes datos para graficar")
                
            elif datos:
                plt.title(f"GASTOS POR CATEGORÍA - Mes {mes_filtro}/{año_filtro} - Gráfico de Barras")
                plt.bar(datos.keys(), datos.values())
                plt.xticks(rotation=45)
                plt.grid(True, alpha=0.3)
                plt.xlabel("Categorías")
                plt.ylabel("Total Gastado")
                plt.tight_layout()
                plt.show()
        
        else: print("Error. Se ingresó una palabra no válida, vuelve a intentar")
            
    except ValueError: print("Error: Se ingresó un dato no válido, vuelve a intentar")