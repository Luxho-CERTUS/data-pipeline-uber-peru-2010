import pandas as pd

archivo_csv = 'uber_peru_2010.csv'

try:
    data = pd.read_csv(archivo_csv, delimiter=";")

    print("Datos cargados correctamente")
    print(data.head())

    archivo_salida = 'output/uber_clean.csv'
    data.to_csv(archivo_salida, index=False)

    print(f"Datos guardados en {archivo_salida}")

except Exception as e:
    print(f"Error al leer los datos: {e}")