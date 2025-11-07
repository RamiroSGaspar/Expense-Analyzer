from analisis_datos import analisis_csv
from graficos import grafico_gastos_generales_plot, grafico_gastos_generales_barra, grafico_gastos_por_categoria
from calculos import calculos_generales, calculos_especificos
from crud import ver_gastos, modificar_gasto, eliminar_gasto, menu_agregar_gastos, guardar_csv

def main():
    gastos, dias, meses, años, categorias, descripciones = analisis_csv()

    while True:
        print("\n" + "="*55)
        print("            SISTEMA DE GESTIÓN DE GASTOS")
        print("="*55)
        print("\n--GRÁFICOS--")
        print("1. Gráfico de gastos por tiempo (plot)")
        print("2. Gráfico de gastos por tiempo (barras)")
        print("3. Gráfico de gastos por categoría")
        
        print("\n--CÁLCULOS--")
        print("4. Cálculos generales")
        print("5. Cálculos por categoría")
        
        print("\n--GESTIÓN DE DATOS--")
        print("6. Ver todos los gastos")
        print("7. Agregar nuevo/s gastos")
        print("8. Modificar un gasto")
        print("9. Eliminar un gasto")
        
        print("\n10. Salir")
        print("="*55)
        
        opcion = input("\nSelecciona una opción: ").strip()
        
        if opcion == "1": grafico_gastos_generales_plot(gastos, meses, años, dias)
        elif opcion == "2": grafico_gastos_generales_barra(gastos, meses, años, dias)
        elif opcion == "3": grafico_gastos_por_categoria(gastos, meses, años, categorias, dias)
        elif opcion == "4": calculos_generales(gastos, meses, años)
        elif opcion == "5": calculos_especificos(gastos, meses, años, categorias)
        elif opcion == "6": ver_gastos(gastos, dias, meses, años, categorias, descripciones)
        elif opcion == "7": menu_agregar_gastos(gastos, dias, meses, años, categorias, descripciones)
        elif opcion == "8": modificar_gasto(gastos, dias, meses, años, categorias, descripciones)
        elif opcion == "9": eliminar_gasto(gastos, dias, meses, años, categorias, descripciones)
        elif opcion == "10":
            print("\nSaliendo del programa...")
            break
        else: print("Error. opcion no valida, por favor, intenta de nuevo.")