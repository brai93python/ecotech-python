from django.shortcuts import render
from .calculos import obtener_metricas_consumo


def vista_panel_sustentabilidad(request):
    # Datos de ejemplo (en un caso real vendrían de la base de datos)
    registros = {
        "Planta Norte": [1200, 1350, 1100],
        "Planta Sur": [900, 950],
        "Planta Este": [1500, 1600, 1450],
    }

    # Invocamos el procesamiento
    metricas = obtener_metricas_consumo(registros)

    # Diccionario de contexto para la plantilla
    contexto = {
        "total_emisiones": metricas["total_emisiones"],
        "planta_mayor_consumo": metricas["planta_mayor_consumo"],
        "emisiones_por_planta": metricas["emisiones_por_planta"],
    }

    return render(request, "sustentabilidad/panel.html", contexto)
