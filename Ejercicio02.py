# Escribir una función que lea dos ficheros csv con una lista larga de datos
# de personas (50 personas y 1000 personas) y llame a dos funciones que pongan
# su nombre en formato capitalizado y calculen la letra de DNI correspondiente.
# Realiza la comprobación de rendimiento con la librería cProfile y muestra
# los datos. Describe que indica cada dato que nos proporciona cProfile.
import csv
import cProfile
import pstats
def calcular_letra_dni(numero_dni):
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    return letras[numero_dni % 23]
def capitalizar_nombre(nombre):
    return nombre.strip().title()
def procesar_csv(ruta_archivo):
    datos_procesados = []
    with open(ruta_archivo, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            nombre_capitalizado = capitalizar_nombre(row['Nombre'])
            dni = int(row['DNI'])
            letra_dni = calcular_letra_dni(dni)
            datos_procesados.append({
                'Nombre': nombre_capitalizado,
                'DNI': f"{dni}-{letra_dni}"
            })
    return datos_procesados
def main():
    ruta_archivo_50 = '/mnt/data/50.csv'
    ruta_archivo_1000 = '/mnt/data/1000.csv'
    print("Procesando archivo con 50 personas...")
    datos_50 = procesar_csv(ruta_archivo_50)
    print(f"Procesadas {len(datos_50)} entradas del archivo de 50 personas.")
    print("Procesando archivo con 1000 personas...")
    datos_1000 = procesar_csv(ruta_archivo_1000)
    print(f"Procesadas {len(datos_1000)} entradas del archivo de 1000 personas.")
if __name__ == "__main__":
    with cProfile.Profile() as pr:
        main()
    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()