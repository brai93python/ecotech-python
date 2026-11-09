import json

class StockInvalidoError(Exception):
    #stock negativo.
    pass

#
class DispositivoEcologico:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock          # llamado setter

    #
    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, valor):
        #el stock no puede ser negativo
        if valor < 0:
            raise StockInvalidoError(
                f"Stock invalido: {valor}. El stock no puede ser negativo."
            )
        self.__stock = valor

    def ficha_tecnica(self):
        return f"{self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.stock} unidades"

    def a_diccionario(self):
        # Convertidor de objeto en un dict para poder guardarlo en JSON
        return {
            "tipo": "DispositivoEcologico",
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
        }


# herencia
class PanelSolar(DispositivoEcologico):
    def __init__(self, nombre, precio, stock, potencia_watts, eficiencia):
        # super() reutiliza el __init__ de la clase base
        super().__init__(nombre, precio, stock)
        self.potencia_watts = potencia_watts
        self.eficiencia = eficiencia

   #poli
    def ficha_tecnica(self):
        return (
            f"PANEL SOLAR - {self.nombre}\n"
            f"  Potencia: {self.potencia_watts} W\n"
            f"  Eficiencia: {self.eficiencia}%\n"
            f"  Precio: ${self.precio:.2f}\n"
            f"  Stock: {self.stock} unidades"
        )

    def a_diccionario(self):
        datos = super().a_diccionario()      # datos de la clase base
        datos["tipo"] = "PanelSolar"
        datos["potencia_watts"] = self.potencia_watts
        datos["eficiencia"] = self.eficiencia
        return datos


#Persis
class GestorInventario:
    def guardar_catalogo_json(self, lista_dispositivos, ruta_archivo):
        # Convertimos cada objeto a diccionario
        catalogo = []
        for dispositivo in lista_dispositivos:
            catalogo.append(dispositivo.a_diccionario())

        # Escritura json
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(catalogo, archivo, indent=4, ensure_ascii=False)


#prueba
if __name__ == "__main__":
    #stock inválido 
    try:
        panel_malo = PanelSolar("Panel Defectuoso", 300.0, -5, 300, 18.0)
    except StockInvalidoError as error:
        print(f"Error capturado: {error}")

    # validacion
    panel1 = PanelSolar("Panel Solar Aurora", 450.0, 20, 400, 21.5)
    panel2 = PanelSolar("Panel Solar Sol Max", 620.0, 10, 550, 22.8)
    cargador = DispositivoEcologico("Cargador Solar Portatil", 85.0, 35)

    try:
        panel1.stock = -1
    except StockInvalidoError as error:
        print(f"Error capturado: {error}")

    #polimorfismo
    productos = [panel1, panel2, cargador]
    print("\n--- Fichas tecnicas ---")
    for producto in productos:
        print(producto.ficha_tecnica())

    #Guardar
    gestor = GestorInventario()
    gestor.guardar_catalogo_json(productos, "catalogo_ecotech.json")
    print(f"\nCatalogo guardado en catalogo_ecotech.json ({len(productos)} productos)")

