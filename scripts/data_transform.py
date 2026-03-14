import pandas as pd

archivo_csv = '../output/uber_clean.csv'

try:

    data = pd.read_csv(archivo_csv)

    # eliminar viajes cancelados
    data = data[data['end_state'] == 'drop off']

    # convertir fechas
    data['start_at'] = pd.to_datetime(data['start_at'], dayfirst=True)
    data['end_at'] = pd.to_datetime(data['end_at'], dayfirst=True)

    # calcular duración del viaje en minutos
    data['trip_duration_minutes'] = (
        data['end_at'] - data['start_at']
    ).dt.total_seconds() / 60

    # convertir precio de centavos a soles
    data['price_soles'] = data['price'] / 100

    # eliminar valores nulos
    data = data.dropna()

    # ordenar por duración del viaje
    data = data.sort_values(by='trip_duration_minutes', ascending=False)

    archivo_transform = '../output/uber_transform.csv'
    data.to_csv(archivo_transform, index=False)

    print("Transformación completada")

except Exception as e:
    print(f"Error al transformar datos: {e}")