import calendar
import os
import shutil
import csv
from datetime import datetime
from config import CSV, BACKUP_DIR

# CRUD  
def guardar_csv(gastos, dias, meses, años, categorias, descripciones, archivo=CSV):
    '''
    permite guardar los datos en el archivo .csv
    crea un backup del archivo original antes de guardar los cambios
    retorna True si se guardo exitosamente, False en caso de error
    '''
    try:
        # se crea un backup antes de guardar
        if os.path.exists(archivo):  # verifica si el archivo existe
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # genera timestamp: 20251022_143025
            filename = os.path.basename(archivo)  # extrae solo el nombre del archivo: Gastos.csv
            backup = os.path.join(BACKUP_DIR, f"{filename}.backup_{timestamp}")  # nombre: backups/Gastos.csv.backup_20251022_143025
            shutil.copy2(archivo, backup)  # copia el archivo con el nuevo nombre (incluye metadatos)
            print(f"- Backup creado: {backup}")  # muestra confirmación
        
        # verificacion para confirmar la misma longitud de elementos
        if not (len(gastos) == len(dias) == len(meses) == len(años) == len(categorias) == len(descripciones)):
            print("Error: Las listas de datos tienen longitudes diferentes")
            return False
        
        # se abre el archivo en modo escritura
        with open(archivo, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['año', 'mes', 'dia', 'categoria', 'precio', 'descripcion'])
            
            # se recorre respetando el formato de fecha consistente con 2 dígitos
            for i in range(len(gastos)):
                writer.writerow([
                    años[i],
                    str(meses[i]).zfill(2),   # 5 → "05"
                    str(dias[i]).zfill(2),    # 7 → "07"
                    categorias[i],
                    gastos[i],
                    descripciones[i]
                ])
        
        print(f"+ Datos guardados exitosamente en '{archivo}'")
        print(f"+ Total de registros guardados: {len(gastos)}")
        return True
        
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")
        return False

def agregar_gasto(gastos, dias, meses, años, categorias, descripciones):
    '''
    permite agregar un nuevo gasto al sistema
    '''
    # Se guardan datos que pueden cambiar en el tiempo
    año_actual = datetime.now().year
    print("\n--Agregar un nuevo gasto--")
    
    # VALIDACIÓN DEL AÑO
    while True:
        try:
            año = int(input("Ingresa el año del gasto (ej: 2025): "))
            if año < 2000 or año > año_actual:
                print(f"Año invalido. Por favor ingrese un año entre 2000 y {año_actual}")
                continue
            break
        except ValueError: 
            print("Error: ingreso no valido.")
    
    # VALIDACIÓN DEL MES
    while True:
        try:
            mes = int(input("Ingresa el mes (1-12): "))
            if mes < 1 or mes > 12:
                print("Mes inválido. Por favor ingrese un mes entre 1 y 12")
                continue
            break
        except ValueError: 
            print("Error: Por favor ingresa un número válido.")
        
    # VALIDACIÓN DEL DIA
    while True:
        try:
            dia = int(input("Ingresa el numero del dia del gasto: "))
            num_dias_mes = calendar.monthrange(año, mes)[1]
            
            if dia > num_dias_mes or dia < 1:
                print(f"Dia invalido. Este mes tiene {num_dias_mes} días")
                continue
            break
        except ValueError: 
            print("Error: ingreso no valido")
        
    # VALIDACIÓN DE LA CATEGORIA
    print("\nCategorias Existentes: ")
    categorias_unicas = list(set(categorias))
    categorias_unicas.sort()
    
    # se muestran las categorias existentes:
    for i, cat in enumerate(categorias_unicas, 1):
        print(f"{i}. {cat}")
        
    opcion_nueva = len(categorias_unicas) + 1
    print(f"{opcion_nueva}. Crear nueva categoría")
    
    while True:
        try:
            opcion = int(input("\nElige una opción: "))
                
            # se verifica que la opción sea válida
            if opcion < 1 or opcion > opcion_nueva:
                print(f"Por favor elige una opción entre 1 y {opcion_nueva}")
                continue
            
            # opcion de categoria existente
            if opcion <= len(categorias_unicas):
                categoria_elegida = categorias_unicas[opcion - 1]
                
            # opcion de crear una nueva categoria
            else:
                categoria_elegida = input("Nombre de la nueva categoría: ").strip().lower()
                while categoria_elegida == "":
                    print("La categoría no puede estar vacía")
                    categoria_elegida = input("Nombre de la nueva categoría: ").strip().lower()
            
            break
        except ValueError: 
            print("Error: ingreso no valido")

    # VALIDACION DEL PRECIO
    while True:
        try:
            precio = float(input("\nIngresa el precio del gasto: $"))
            if precio <= 0: 
                print("El precio debe ser mayor que 0")
                continue
            break
        except ValueError: 
            print("Error: ingreso no valido")
        
    # VALIDACION DE LA DESCRIPCION (OPCIONAL)
    print("\n¿Deseas agregar una descripción?")
    descripcion = input("Descripcion (presiona enter para omitir): ").strip()
    
    if descripcion == "": 
        descripcion = "-"
    
    # Agregado a las listas
    años.append(año)
    meses.append(mes)
    dias.append(dia)
    categorias.append(categoria_elegida)
    gastos.append(precio)
    descripciones.append(descripcion)
    
    print(f"\nGasto agregado exitosamente:")
    print(f"- Fecha: {dia:02d}/{mes:02d}/{año}")
    print(f"- Categoría: {categoria_elegida}")
    print(f"- Precio: ${precio:.2f}")
    if descripcion != "-":
        print(f"- Descripción: {descripcion}")

def menu_agregar_gastos(gastos, dias, meses, años, categorias, descripciones):
    '''
    permite agregar varios gastos seguidos
    al finalizar, se pregunta si se quieren guardar los cambios
    en caso de no guardar, se pide confirmacion clara
    ''' 
    gastos_agregados = 0
    
    while True:
        # se llama a la función que agrega UN gasto
        agregar_gasto(gastos, dias, meses, años, categorias, descripciones)
        gastos_agregados += 1
        
        print("\n" + "="*40)
        continuar = input("¿Quieres agregar otro gasto? (s/n): ").lower().strip()
        
        if continuar != 's':
            break
    
    print(f"\nSe agregaron {gastos_agregados} gasto(s) en total")
    
    # confirmacion clara al no guardar
    respuesta = input("¿Quieres guardar los cambios en el archivo? (s/n): ").lower().strip()
    
    if respuesta == 's': 
        guardar_csv(gastos, dias, meses, años, categorias, descripciones)
    else:
        print("\nADVERTENCIA: Los gastos agregados NO se guardarán en el archivo")
        confirmar = input("¿Estás seguro de NO guardar? (s/n): ").lower().strip()
        if confirmar != 's':
            print("\nGuardando cambios...")
            guardar_csv(gastos, dias, meses, años, categorias, descripciones)
        else:
            print("- Cambios descartados")

def eliminar_gasto(gastos, dias, meses, años, categorias, descripciones):
    '''
    permite eliminar un gasto existente
    el usuario selecciona el gasto por numero
    se pide confirmacion antes de eliminar
    '''
    if len(gastos) == 0:
        print("\nNo hay gastos para eliminar")
        return
    
    ver_gastos(gastos, dias, meses, años, categorias, descripciones)
    
    try:
        num = int(input("\n¿Qué gasto deseas eliminar? (número o 0 para cancelar): "))
        
        if num == 0:
            print("Operación cancelada")
            return
            
        if num < 1 or num > len(gastos):
            print("Número inválido")
            return
        
        idx = num - 1
        
        print(f"\n¿Eliminar este gasto?")
        print(f"- Fecha: {dias[idx]:02d}/{meses[idx]:02d}/{años[idx]}")
        print(f"- Categoría: {categorias[idx]}")
        print(f"- Precio: ${gastos[idx]:.2f}")
        print(f"- Descripción: {descripciones[idx]}")
        
        confirmar = input("\nConfirmar eliminación (s/n): ").lower().strip()
        
        if confirmar == 's':
            # eliminar de todas las listas
            del gastos[idx]
            del dias[idx]
            del meses[idx]
            del años[idx]
            del categorias[idx]
            del descripciones[idx]
            
            print("- Gasto eliminado correctamente")
            
            # se pregunta para guardar
            guardar = input("¿Guardar cambios en archivo? (s/n): ").lower().strip()
            if guardar == 's': guardar_csv(gastos, dias, meses, años, categorias, descripciones)
                
        else: print("Operación cancelada")
            
    except ValueError: print("Error: Entrada inválida")

def ver_gastos(gastos, dias, meses, años, categorias, descripciones):
    '''
    permite ver todos los gastos registrados en el sistema
    muestra la fecha, categoria, precio y descripcion de cada gasto
    ademas muestra el total de gastos y la suma total de los mismos
    '''
    if len(gastos) == 0:
        print("\nNo hay gastos registrados")
        return
    
    print("\n--GASTOS REGISTRADOS--")
    for i in range(len(gastos)):
        print(f"{i+1}. {dias[i]:02d}/{meses[i]:02d}/{años[i]} - {categorias[i]} - ${gastos[i]:.2f} - {descripciones[i]}")
    
    print(f"\nTotal: {len(gastos)} gastos | ${sum(gastos):.2f}")

def modificar_gasto(gastos, dias, meses, años, categorias, descripciones):
    """
    Permite modificar un gasto existente.
    El usuario selecciona el gasto por número y puede cambiar cualquier campo.
    Presionando ENTER mantiene el valor actual.
    """
    
    # se verifica que hay gastos para modificar
    if len(gastos) == 0:
        print("\nNo hay gastos para modificar")
        return
    
    ver_gastos(gastos, dias, meses, años, categorias, descripciones)
    
    try:
        num = int(input("\n¿Qué gasto deseas modificar? (número o 0 para cancelar): "))
        if num == 0:
            print("Operación cancelada")
            return
        if num < 1 or num > len(gastos):
            print("Número inválido")
            return
        
        idx = num - 1  # Se converte a índice (las listas empiezan en 0)
        
        # Se muestrar los datos actuales del gasto seleccionado
        print(f"\n--GASTO ACTUAL--")
        print(f"Fecha: {dias[idx]:02d}/{meses[idx]:02d}/{años[idx]}")
        print(f"Categoría: {categorias[idx]}")
        print(f"Precio: ${gastos[idx]:.2f}")
        print(f"Descripción: {descripciones[idx]}")
        
        print("\n--MODIFICAR GASTO--")
        print("(Presiona ENTER para mantener el valor actual)")
        
        # MODIFICAR AÑO
        año_nuevo = input(f"Nuevo año [{años[idx]}]: ").strip()
        if año_nuevo != "":  # si el usuario ingreso algo
            try:
                año_nuevo = int(año_nuevo)
                año_actual = datetime.now().year
                # validar rango de año
                if año_nuevo < 2000 or año_nuevo > año_actual:
                    print(f"Año inválido. Se mantiene: {años[idx]}")
                    año_nuevo = años[idx]
            except ValueError:
                print("Entrada inválida. Se mantiene el año actual")
                año_nuevo = años[idx]
        else: año_nuevo = años[idx] # si se  presionó ENTER, mantener el valor actual

        
        # MODIFICAR MES
        mes_nuevo = input(f"Nuevo mes (1-12) [{meses[idx]}]: ").strip()
        if mes_nuevo != "":
            try:
                mes_nuevo = int(mes_nuevo)
                if mes_nuevo < 1 or mes_nuevo > 12:
                    print(f"Mes inválido. Se mantiene: {meses[idx]}")
                    mes_nuevo = meses[idx]
            except ValueError:
                print("Entrada inválida. Se mantiene el mes actual")
                mes_nuevo = meses[idx]
        else: mes_nuevo = meses[idx]
        
        # MODIFICAR DÍA
        dia_nuevo = input(f"Nuevo día [{dias[idx]}]: ").strip()
        if dia_nuevo != "":
            try:
                dia_nuevo = int(dia_nuevo)
                # obtener la cantidad de días del mes ingresado
                num_dias_mes = calendar.monthrange(año_nuevo, mes_nuevo)[1]
                # validar que el día sea válido para ese mes
                if dia_nuevo < 1 or dia_nuevo > num_dias_mes:
                    print(f"Día inválido. Se mantiene: {dias[idx]}")
                    dia_nuevo = dias[idx]
            except ValueError:
                print("Entrada inválida. Se mantiene el día actual")
                dia_nuevo = dias[idx]
        else: dia_nuevo = dias[idx]
        
        # MODIFICAR CATEGORÍA
        print("\nCategorías disponibles:")
        # se obtiene las categorias unicas y ordenarlas
        categorias_unicas = sorted(list(set(categorias)))
        # muestra la lista numerada
        for i, cat in enumerate(categorias_unicas, 1):
            print(f"{i}. {cat}")
        print(f"{len(categorias_unicas) + 1}. Crear nueva categoría")
        print(f"{len(categorias_unicas) + 2}. Mantener actual ({categorias[idx]})")
        
        opcion_cat = input("\nElige una opción: ").strip()
        if opcion_cat == "": categoria_nueva = categorias[idx] # si presiono ENTER sin escribir
        else:
            try:
                opcion_cat = int(opcion_cat)
                # si eligio una categoria existente
                if 1 <= opcion_cat <= len(categorias_unicas):
                    categoria_nueva = categorias_unicas[opcion_cat - 1]
                    
                # si eligio crear nueva categoria
                elif opcion_cat == len(categorias_unicas) + 1:
                    categoria_nueva = input("Nombre de la nueva categoría: ").strip().lower()
                    if categoria_nueva == "":
                        print("Categoría vacía. Se mantiene la actual")
                        categoria_nueva = categorias[idx]
                        
                # si eligio mantener actual o cualquier otra opcion
                else: categoria_nueva = categorias[idx]
            except ValueError:
                print("Entrada inválida. Se mantiene la categoría actual")
                categoria_nueva = categorias[idx]
        
        # MODIFICAR PRECIO
        precio_nuevo = input(f"Nuevo precio [${gastos[idx]:.2f}]: $").strip()
        if precio_nuevo != "":
            try:
                precio_nuevo = float(precio_nuevo)
                # validar que sea mayor que 0
                if precio_nuevo <= 0:
                    print("Precio inválido. Se mantiene el precio actual")
                    precio_nuevo = gastos[idx]
            except ValueError:
                print("Entrada inválida. Se mantiene el precio actual")
                precio_nuevo = gastos[idx]
        else:
            precio_nuevo = gastos[idx]
        
        # MODIFICAR DESCRIPCIÓN
        descripcion_nueva = input(f"Nueva descripción [{descripciones[idx]}]: ").strip()
        if descripcion_nueva == "":  # si se resiona ENTER, mantener la actual
            descripcion_nueva = descripciones[idx]
        
        # MOSTRAR RESUMEN DE CAMBIOS
        print("\n--RESUMEN DE CAMBIOS--")
        print(f"Fecha: {dias[idx]:02d}/{meses[idx]:02d}/{años[idx]} -> {dia_nuevo:02d}/{mes_nuevo:02d}/{año_nuevo}")
        print(f"Categoría: {categorias[idx]} -> {categoria_nueva}")
        print(f"Precio: ${gastos[idx]:.2f} -> ${precio_nuevo:.2f}")
        print(f"Descripción: {descripciones[idx]} -> {descripcion_nueva}")
        
        # CONFIRMAR Y APLICAR CAMBIOS
        confirmar = input("\n¿Confirmar cambios? (s/n): ").lower().strip()
        
        if confirmar == 's':
            # se aplican todos los cambios a las listas
            años[idx] = año_nuevo
            meses[idx] = mes_nuevo
            dias[idx] = dia_nuevo
            categorias[idx] = categoria_nueva
            gastos[idx] = precio_nuevo
            descripciones[idx] = descripcion_nueva
            
            print("\n- Gasto modificado exitosamente")
            
            guardar = input("¿Guardar cambios en archivo? (s/n): ").lower().strip()
            if guardar == 's':
                guardar_csv(gastos, dias, meses, años, categorias, descripciones)
        else:
            print("Cambios descartados")
            
    except ValueError:
        print("Error: Entrada inválida")
