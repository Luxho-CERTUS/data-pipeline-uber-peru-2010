import pandas as pd
import os

archivo_csv = 'output/uber_transform.csv'

try:
    os.makedirs('output', exist_ok=True)

    data = pd.read_csv(archivo_csv)

    archivo_excel = 'output/uber_final.xlsx'

    data.to_excel(archivo_excel, index=False)

    print(f"Datos exportados correctamente a {archivo_excel}")

except Exception as e:
    print(f"Error al exportar: {e}")