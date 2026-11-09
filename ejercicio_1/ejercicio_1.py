
def limpiar_registro_sensor(registro):
    
    sensor_id = registro["sensor_id"].strip()

    # si la clave existe la limpiamos; si no, queda en None
    if "temperatura" in registro:
        texto = registro["temperatura"]
        texto = texto.replace("C", "")    # fuera unidad
        texto = texto.replace("°", "")    #fuera simbolo
        texto = texto.strip()            
        temperatura = float(texto)        # conversion
    else:
        temperatura = None

    #siestá vacía, usamos un valor por defecto
    ubicacion = registro.get("ubicacion", "").strip()
    if ubicacion == "":
        ubicacion = "Sin ubicación"

    # Diccionsrio
    return {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion,
    }


def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    sensores_alerta = []   #valores fuera del umbral
    suma = 0               # acumulador temperatura
    cantidad = 0           # cuántos sensores tienen lectura válida

    for sensor in lista_sensores_limpios:
        # Si no tiene temperatura, lo salteamos
        if sensor["temperatura"] is None:
            continue

        suma += sensor["temperatura"]
        cantidad += 1

        # Si supera el umbral, guardamos su id
        if sensor["temperatura"] > umbral_temperatura:
            sensores_alerta.append(sensor["sensor_id"])

    # Promedio = suma / cantidad (evitamos dividir por cero)
    if cantidad > 0:
        promedio = suma / cantidad
    else:
        promedio = 0

    return sensores_alerta, promedio   # devuelve una tupla


#Ejecucion
registros_crudos = [
    {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
    {"sensor_id": "SENSOR-002", "temperatura": " 31.2 C "},
    {"sensor_id": " SENSOR-003", "temperatura": "28°C", "ubicacion": "Planta Sur"},
    {"sensor_id": "SENSOR-004 ", "temperatura": "35.8C", "ubicacion": ""},
    {"sensor_id": "SENSOR-005", "ubicacion": "Planta Este"},  # sin temperatura
]
umbral = 30.0 #prueba de sensores

#limpia cada registro
registros_limpios = []
for registro in registros_crudos:
    registros_limpios.append(limpiar_registro_sensor(registro))

# generar el resumen
alertas, promedio = generar_resumen_sensores(registros_limpios, umbral)

#Imprimir el reporte
print("===== REPORTE ECOTECH SOLUTIONS =====")
print(f"Sensores procesados: {len(registros_limpios)}")
print(f"Umbral de alerta: {umbral} °C")
print(f"Promedio global: {promedio:.2f} °C")
print(f"Sensores en alerta: {alertas}")