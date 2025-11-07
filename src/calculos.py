
from utilidades import pedir_año, pedir_mes
import numpy as np

def calculos_generales(gastos, meses, años, dias):
    '''
    permite realizar calculos generales sobre todos los gastos
    el usuario elige el tipo de calculo
    retorna los resultados segun la eleccion del usuario
    '''
    lista_gastos = []
    
    print("--CALCULOS GENERALES--")
    desicion = input("¿En qué filtro quieres hacer cálculos? (opciones: 'mes', 'año' o 'años'): ").strip().lower()
    
    try: 
        if desicion == "año":
            print("\n--CALCULOS GENERALES (por año)--")
            print("Ingresa el año donde quieres ver los cálculos (Formato: 0000): ")
            año_filtro = pedir_año()
            
            # Filtrar solo los gastos del año específico
            for g, m, a in zip(gastos, meses, años):
                if a == año_filtro:
                    lista_gastos.append(g)
            
            if len(lista_gastos) == 0:
                print(f"\nMENSAJE: El año {año_filtro} no tiene datos para calcular")
                return
            
            array_gastos = np.array(lista_gastos)
            
            print("\n¿Qué quieres revisar?")
            print("- Ingresa 'total' para ver el total de gastos")
            print("- Ingresa 'promedio' para ver el promedio")
            print("- Ingresa 'maximo' para ver el gasto máximo")
            print("- Ingresa 'minimo' para ver el gasto mínimo")
            print("- Ingresa 'todo' para ver todas las opciones")
            
            desicion_2 = input("Ingresa la opción: ").strip().lower()
            
            if desicion_2 == "total": print(f"\nEl total de los gastos en {año_filtro}: ${np.sum(array_gastos):.2f}")
            elif desicion_2 == "promedio": print(f"\nEl promedio de los gastos en {año_filtro}: ${np.average(array_gastos):.2f}")
            elif desicion_2 == "maximo": print(f"\nEl gasto máximo en {año_filtro} es: ${np.max(array_gastos):.2f}")
            elif desicion_2 == "minimo": print(f"\nEl gasto mínimo en {año_filtro} es: ${np.min(array_gastos):.2f}")
            elif desicion_2 == "todo":
                print(f"\n--Todos los cálculos del año {año_filtro}--")
                print(f"Total de gastos: ${np.sum(array_gastos):.2f}")
                print(f"Promedio de gastos: ${np.average(array_gastos):.2f}")
                print(f"Gasto máximo: ${np.max(array_gastos):.2f}")
                print(f"Gasto mínimo: ${np.min(array_gastos):.2f}")
            else: print("Error. Opción no válida")
            
        elif desicion == "años":
            print("\n--CALCULOS GENERALES (todos los años)--")
            
            # Tomar todos los gastos
            for g in gastos:
                lista_gastos.append(g)
            
            if len(lista_gastos) == 0:
                print("\nMENSAJE: No hay datos para calcular")
                return
            
            array_gastos = np.array(lista_gastos)
            
            print("\n¿Qué quieres revisar?")
            print("- Ingresa 'total' para ver el total de gastos")
            print("- Ingresa 'promedio' para ver el promedio")
            print("- Ingresa 'maximo' para ver el gasto máximo")
            print("- Ingresa 'minimo' para ver el gasto mínimo")
            print("- Ingresa 'todo' para ver todas las opciones")
            
            desicion_2 = input("Ingresa la opción: ").strip().lower()
            
            if desicion_2 == "total": print(f"\nEl total de todos los gastos: ${np.sum(array_gastos):.2f}")
            elif desicion_2 == "promedio": print(f"\nEl promedio de todos los gastos: ${np.average(array_gastos):.2f}")
            elif desicion_2 == "maximo": print(f"\nEl gasto máximo es: ${np.max(array_gastos):.2f}")
            elif desicion_2 == "minimo": print(f"\nEl gasto mínimo es: ${np.min(array_gastos):.2f}")
            elif desicion_2 == "todo":
                print("\n--Todos los cálculos (histórico completo)--")
                print(f"Total de gastos: ${np.sum(array_gastos):.2f}")
                print(f"Promedio de gastos: ${np.average(array_gastos):.2f}")
                print(f"Gasto máximo: ${np.max(array_gastos):.2f}")
                print(f"Gasto mínimo: ${np.min(array_gastos):.2f}")
            else: print("Error. Opción no válida")
        
        elif desicion == "mes":
            print("\n--CALCULOS GENERALES (por mes)--")
            print("Ingresa el año donde quieres ver los cálculos (Formato: 0000): ")
            año_filtro = pedir_año()
            print("Ingresa el mes donde quieres ver los cálculos (1-12): ")
            mes_filtro = pedir_mes()
            
            # Filtrar solo los gastos del mes y año específico
            for g, m, a in zip(gastos, meses, años):
                if a == año_filtro and m == mes_filtro:
                    lista_gastos.append(g)
            
            if len(lista_gastos) == 0:
                print(f"\nMENSAJE: El mes {mes_filtro}/{año_filtro} no tiene datos para calcular")
                return
            
            array_gastos = np.array(lista_gastos)
            
            print("\n¿Qué quieres revisar?")
            print("- Ingresa 'total' para ver el total de gastos")
            print("- Ingresa 'promedio' para ver el promedio")
            print("- Ingresa 'maximo' para ver el gasto máximo")
            print("- Ingresa 'minimo' para ver el gasto mínimo")
            print("- Ingresa 'todo' para ver todas las opciones")
            
            desicion_2 = input("Ingresa la opción: ").strip().lower()
            
            if desicion_2 == "total": print(f"\nEl total de gastos en {mes_filtro}/{año_filtro}: ${np.sum(array_gastos):.2f}")
            elif desicion_2 == "promedio": print(f"\nEl promedio de gastos en {mes_filtro}/{año_filtro}: ${np.average(array_gastos):.2f}")
            elif desicion_2 == "maximo": print(f"\nEl gasto máximo en {mes_filtro}/{año_filtro} es: ${np.max(array_gastos):.2f}")
            elif desicion_2 == "minimo": print(f"\nEl gasto mínimo en {mes_filtro}/{año_filtro} es: ${np.min(array_gastos):.2f}")
            elif desicion_2 == "todo":
                print(f"\n--Todos los cálculos del mes {mes_filtro}/{año_filtro}--")
                print(f"Total de gastos: ${np.sum(array_gastos):.2f}")
                print(f"Promedio de gastos: ${np.average(array_gastos):.2f}")
                print(f"Gasto máximo: ${np.max(array_gastos):.2f}")
                print(f"Gasto mínimo: ${np.min(array_gastos):.2f}")
            else: print("Error. Opción no válida")
        
        else: print("Error: Se ingresó una palabra no válida, vuelve a intentar")
        
    except ValueError: print("Error: Se ingresó un dato no válido, vuelve a intentar")
        
def calculos_especificos(gastos, meses, años, categorias, dias):
    '''
    permite realizar calculos especificos por categoria
    el usuario elige la categoria y el tipo de calculo
    retorna los resultados segun la eleccion del usuario
    '''
    diccionario = {}
    
    print("\n--CALCULOS ESPECIFICOS POR CATEGORIA--")
    desicion = input("¿En qué filtro quieres hacer cálculos? (opciones: 'mes', 'año' o 'años'): ").strip().lower()
    
    try:
        if desicion == "año":
            print("\n--CALCULOS POR CATEGORIA (por año)--")
            print("Ingresa el año donde quieres ver los cálculos por categoría (Formato: 0000): ")
            año_filtro = pedir_año()
            
            # Agrupar gastos por categoría dentro del año especificado
            for g, m, a, c in zip(gastos, meses, años, categorias):
                if a == año_filtro:
                    if c not in diccionario: 
                        diccionario[c] = []
                    diccionario[c].append(g)
            
            if len(diccionario) == 0:
                print(f"\nMENSAJE: El año {año_filtro} no tiene datos por categoría")
                return
            
            print("\nEstas son las categorías disponibles:")
            for i, elemento in enumerate(diccionario.keys(), 1):
                print(f"{i}. '{elemento}'")
            
            desicion_2 = input("\nIngresa la categoría: ").strip().lower()
            
            if desicion_2 in diccionario:
                array_gastos = np.array(diccionario[desicion_2])
            
                print("\n¿Qué quieres revisar?")
                print("- Ingresa 'total' para ver el total de gastos por categoría")
                print("- Ingresa 'promedio' para ver el promedio de gastos por categoría")
                print("- Ingresa 'maximo' para ver el gasto máximo por categoría")
                print("- Ingresa 'minimo' para ver el gasto mínimo por categoría")
                print("- Ingresa 'todo' para ver todas las opciones")
                
                desicion_3 = input("Ingresa la opción: ").strip().lower()
                
                if desicion_3 == "total": print(f"\nEl total de la categoría '{desicion_2}' en {año_filtro}: ${np.sum(array_gastos):.2f}")
                elif desicion_3 == "promedio": print(f"\nEl promedio de la categoría '{desicion_2}' en {año_filtro}: ${np.average(array_gastos):.2f}")
                elif desicion_3 == "maximo": print(f"\nEl gasto máximo de la categoría '{desicion_2}' en {año_filtro}: ${np.max(array_gastos):.2f}")
                elif desicion_3 == "minimo": print(f"\nEl gasto mínimo de la categoría '{desicion_2}' en {año_filtro}: ${np.min(array_gastos):.2f}")
                elif desicion_3 == "todo":
                    print(f"\n--Todos los cálculos sobre '{desicion_2}' en {año_filtro}--")
                    print(f"Total de gastos: ${np.sum(array_gastos):.2f}")
                    print(f"Promedio de gastos: ${np.average(array_gastos):.2f}")
                    print(f"Gasto máximo: ${np.max(array_gastos):.2f}")
                    print(f"Gasto mínimo: ${np.min(array_gastos):.2f}")
                else: print("Error. Opción no válida")
                
            else: print("Error. No se encontró la categoría")

        elif desicion == "años":
            print("\n--CALCULOS POR CATEGORIA (todos los años)--")
            
            # Agrupar gastos por categoría en todos los años
            for g, m, a, c in zip(gastos, meses, años, categorias):
                if c not in diccionario: 
                    diccionario[c] = []
                diccionario[c].append(g)
            
            if len(diccionario) == 0:
                print("\nMENSAJE: No hay datos por categoría")
                return
            
            print("\nEstas son las categorías disponibles:")
            for i, elemento in enumerate(diccionario.keys(), 1):
                print(f"{i}. '{elemento}'")
            
            desicion_2 = input("\nIngresa la categoría: ").strip().lower()
            
            if desicion_2 in diccionario:
                array_gastos = np.array(diccionario[desicion_2])
            
                print("\n¿Qué quieres revisar?")
                print("- Ingresa 'total' para ver el total de gastos por categoría")
                print("- Ingresa 'promedio' para ver el promedio de gastos por categoría")
                print("- Ingresa 'maximo' para ver el gasto máximo por categoría")
                print("- Ingresa 'minimo' para ver el gasto mínimo por categoría")
                print("- Ingresa 'todo' para ver todas las opciones")
            
                desicion_3 = input("Ingresa la opción: ").strip().lower()
                
                if desicion_3 == "total": print(f"\nEl total de la categoría '{desicion_2}' (histórico): ${np.sum(array_gastos):.2f}")
                elif desicion_3 == "promedio": print(f"\nEl promedio de la categoría '{desicion_2}' (histórico): ${np.average(array_gastos):.2f}")
                elif desicion_3 == "maximo": print(f"\nEl gasto máximo de la categoría '{desicion_2}' (histórico): ${np.max(array_gastos):.2f}")
                elif desicion_3 == "minimo": print(f"\nEl gasto mínimo de la categoría '{desicion_2}' (histórico): ${np.min(array_gastos):.2f}")
                elif desicion_3 == "todo":
                    print(f"\n--Todos los cálculos sobre '{desicion_2}' (histórico)--")
                    print(f"Total de gastos: ${np.sum(array_gastos):.2f}")
                    print(f"Promedio de gastos: ${np.average(array_gastos):.2f}")
                    print(f"Gasto máximo: ${np.max(array_gastos):.2f}")
                    print(f"Gasto mínimo: ${np.min(array_gastos):.2f}")
                else: print("Error. Opción no válida")
                
            else: print("Error. No se encontró la categoría")
        
        elif desicion == "mes":
            print("\n--CALCULOS POR CATEGORIA (por mes)--")
            print("Ingresa el año donde quieres ver los cálculos por categoría (Formato: 0000): ")
            año_filtro = pedir_año()
            print("Ingresa el mes donde quieres ver los cálculos por categoría (1-12): ")
            mes_filtro = pedir_mes()
            
            # Agrupar gastos por categoría dentro del mes y año especificados
            for g, m, a, c in zip(gastos, meses, años, categorias):
                if a == año_filtro and m == mes_filtro:
                    if c not in diccionario: 
                        diccionario[c] = []
                    diccionario[c].append(g)
            
            if len(diccionario) == 0:
                print(f"\nMENSAJE: El mes {mes_filtro}/{año_filtro} no tiene datos por categoría")
                return
            
            print("\nEstas son las categorías disponibles:")
            for i, elemento in enumerate(diccionario.keys(), 1):
                print(f"{i}. '{elemento}'")
            
            desicion_2 = input("\nIngresa la categoría: ").strip().lower()
            
            if desicion_2 in diccionario:
                array_gastos = np.array(diccionario[desicion_2])
            
                print("\n¿Qué quieres revisar?")
                print("- Ingresa 'total' para ver el total de gastos por categoría")
                print("- Ingresa 'promedio' para ver el promedio de gastos por categoría")
                print("- Ingresa 'maximo' para ver el gasto máximo por categoría")
                print("- Ingresa 'minimo' para ver el gasto mínimo por categoría")
                print("- Ingresa 'todo' para ver todas las opciones")
                
                desicion_3 = input("Ingresa la opción: ").strip().lower()
                
                if desicion_3 == "total": print(f"\nEl total de la categoría '{desicion_2}' en {mes_filtro}/{año_filtro}: ${np.sum(array_gastos):.2f}")
                elif desicion_3 == "promedio": print(f"\nEl promedio de la categoría '{desicion_2}' en {mes_filtro}/{año_filtro}: ${np.average(array_gastos):.2f}")
                elif desicion_3 == "maximo": print(f"\nEl gasto máximo de la categoría '{desicion_2}' en {mes_filtro}/{año_filtro}: ${np.max(array_gastos):.2f}")
                elif desicion_3 == "minimo": print(f"\nEl gasto mínimo de la categoría '{desicion_2}' en {mes_filtro}/{año_filtro}: ${np.min(array_gastos):.2f}")
                elif desicion_3 == "todo":
                    print(f"\n--Todos los cálculos sobre '{desicion_2}' en {mes_filtro}/{año_filtro}--")
                    print(f"Total de gastos: ${np.sum(array_gastos):.2f}")
                    print(f"Promedio de gastos: ${np.average(array_gastos):.2f}")
                    print(f"Gasto máximo: ${np.max(array_gastos):.2f}")
                    print(f"Gasto mínimo: ${np.min(array_gastos):.2f}")
                else:  print("Error. Opción no válida")
                
            else: print("Error. No se encontró la categoría")
        
        else: print("Error. Se ingresó una palabra no válida, vuelve a intentar")
        
    except ValueError: print("Error: Se ingresó un dato no válido, vuelve a intentar")
