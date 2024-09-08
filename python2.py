import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("=================================================")
print("        Jesus Nahir Borjas Morales 2059158       ")
print("=================================================")

while True:
    print("\nOpciones:")
    print("a) Pandas")
    print("b) Numpy")
    print("c) Salir")
    
    opcion = input("Ingrese la opción deseada (a/b/c): ").strip().lower()

    if opcion == 'a':
        print("\n" + "="*50)
        print("Pandas es una biblioteca de Python fundamental para análisis de datos.")
        print("Es especialmente útil para trabajar con datos estructurados como tablas, hojas de cálculo o bases de datos,")
        print("ya que permite manejar grandes cantidades de información de manera eficiente.")
        print("="*50)

        print("Creación de estructuras de información:")
        Diccionario = {
            'Nombre': ['Jesus', 'Franco', 'Miguel'],
            'Edad': [18, 19, 25],
            'Ciudad': ['Monterrey', 'Barcelona', 'Escobedo']
        }
        df = pd.DataFrame(Diccionario)
        print("\nConvertimos un diccionario a un DataFrame con pd.DataFrame(Diccionario):")
        print(df)
        print("Con esto podemos crear gráficas y exportar a Excel.")
        df.to_excel('datos.xlsx', index=False)
        print("Guardamos el DataFrame en 'datos.xlsx' con df.to_excel('datos.xlsx', index=False).")

        df.plot(x='Nombre', y='Edad', kind='bar', color='skyblue', legend=False)
        plt.title('Edades de las Personas')
        plt.xlabel('Nombre')
        plt.ylabel('Edad')
        plt.xticks(rotation=0)
        plt.tight_layout()
        print("\nGracias a pandas y matplotlib, podemos crear gráficas y guardarlas como imagen.")
        
        while True:
            guardar_imagen = input("¿Desea guardar la imagen? (si/no): ").strip().lower()
            if guardar_imagen in ['si', 'no']:
                break
            else:
                print("Opción no válida. Responda con 'si' o 'no'.")

        if guardar_imagen == 'si':
            plt.savefig('grafico_edades.png', dpi=300, bbox_inches='tight')
            print("La imagen se ha guardado como 'grafico_edades.png'.")
            plt.show()

        print("\n" + "="*50)
        print("Esos son algunos de los usos más comunes para la herramienta pandas.")
        print("="*50)

    elif opcion == 'b':
        print("\n" + "="*50)
        print("Numpy es una biblioteca de Python fundamental para el cálculo científico y la manipulación de matrices.")
        print("Proporciona estructuras de datos eficientes y herramientas para cálculos numéricos con matrices multidimensionales.")
        print("="*50)

        print("Creación de matrices y operaciones matemáticas básicas:")
        matriz1 = np.array([1, 2, 3, 4, 5])
        print("\nMatriz unidimensional creada:")
        print(matriz1)
        
        matriz2 = np.array([[1, 2, 3], [4, 5, 6]])
        print("\nMatriz bidimensional creada:")
        print(matriz2)
        
        suma = matriz1 + 10
        print("\nSuma de 10 a cada elemento de la matriz1:")
        print(suma)
        
        producto = matriz2 * 2
        print("\nMultiplicación por 2 de cada elemento de la matriz2:")
        print(producto)
        
        media = np.mean(matriz1)
        desviacion_estandar = np.std(matriz1)
        print("\nMedia de la matriz1:", media)
        print("Desviación estándar de la matriz1:", desviacion_estandar)
        
        np.savetxt('matriz1.txt', matriz1, fmt='%d')
        print("\nLa matriz1 se ha guardado en 'matriz1.txt'. Utilizando np.savetxt('matriz1.txt', matriz1, fmt='%d').")
        
        matriz_leida = np.loadtxt('matriz1.txt', dtype=int)
        print("\nMatriz leída desde el archivo:")
        print(matriz_leida)
        
        print("\n" + "="*50)
        print("Estos son algunos de los usos más comunes de la herramienta numpy.")
        print("="*50)

    elif opcion == 'c':
        print("\Gracias por su atencion.")
        break
    
    else:
        print("Opción no válida. Por favor, ingrese 'a', 'b' o 'c'.")

