# Escribir una función que lea dos ficheros csv con una lista larga de datos
# de personas (50 personas y 1000 personas) y llame a dos funciones que pongan
# su nombre en formato capitalizado y calculen la letra de DNI correspondiente.
# Realiza la comprobación de rendimiento con la librería cProfile y muestra
# los datos. Describe que indica cada dato que nos proporciona cProfile.
import csv
import cProfile
import pstats

ruta_50 = 'C:\\Users\\david\\Documents\\GitHub\\practica0301_csantilmuy\\50.csv'
ruta_1000 = 'C:\\Users\\david\\Documents\\GitHub\\practica0301_csantilmuy\\1000.csv'

LETRAS_DNI = "TRWAGMYFPDXBNJZSQVHLCKE"

def capitalizar_nombre(nombre):
    return nombre.title()

def calcular_letra_dni(numero_dni):
    return LETRAS_DNI[numero_dni % 23]

def procesar_archivo_csv(ruta_csv):
    resultados = []
    with open(ruta_csv, newline='', encoding='utf-8') as csvfile:
        lector = csv.reader(csvfile)
        next(lector)
        for fila in lector:
            nombre, dni = fila[0], int(fila[1])
            nombre_capitalizado = capitalizar_nombre(nombre)
            letra_dni = calcular_letra_dni(dni)
            resultados.append((nombre_capitalizado, dni, letra_dni))
    return resultados

def main():
    print("Procesando archivo con 50 personas...")
    resultados_50 = procesar_archivo_csv(ruta_50)
    print(f"Procesado {len(resultados_50)} registros del archivo de 50 personas.")

    print("\nProcesando archivo con 1000 personas...")
    resultados_1000 = procesar_archivo_csv(ruta_1000)
    print(f"Procesado {len(resultados_1000)} registros del archivo de 1000 personas.")

if __name__ == "__main__":
    with cProfile.Profile() as pr:
        main()

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()