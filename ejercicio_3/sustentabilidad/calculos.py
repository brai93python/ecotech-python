def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    # Regla: no existe un consumo negativo
    if consumo_kwh < 0:
        raise ValueError("El consumo no puede ser negativo")
    return consumo_kwh * factor_emision


def obtener_metricas_consumo(registros):
    total_emisiones = 0
    planta_mayor = None
    mayor_consumo = -1
    emisiones_por_planta = {}

    # Recorremos cada planta con su lista de consumos
    for planta, consumos in registros.items():
        consumo_planta = 0
        emisiones_planta = 0

        for consumo in consumos:
            consumo_planta += consumo
            emisiones_planta += calcular_emisiones_carbono(consumo)

        emisiones_por_planta[planta] = round(emisiones_planta, 2)
        total_emisiones += emisiones_planta

        # Guardamos la planta con más kWh acumulados
        if consumo_planta > mayor_consumo:
            mayor_consumo = consumo_planta
            planta_mayor = planta

    return {
        "total_emisiones": round(total_emisiones, 2),
        "planta_mayor_consumo": planta_mayor,
        "emisiones_por_planta": emisiones_por_planta,
    }
