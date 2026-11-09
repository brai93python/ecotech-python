import unittest
from .calculos import calcular_emisiones_carbono


class TestCalculoEmisiones(unittest.TestCase):

    def test_calculo_con_factor_por_defecto(self):
        # 100 kWh * 0.4 = 40
        self.assertAlmostEqual(calcular_emisiones_carbono(100), 40.0)

    def test_calculo_con_factor_personalizado(self):
        # 100 kWh * 0.5 = 50
        self.assertAlmostEqual(calcular_emisiones_carbono(100, 0.5), 50.0)

    def test_consumo_cero(self):
        # Caso límite: sin consumo, sin emisiones
        self.assertEqual(calcular_emisiones_carbono(0), 0)

    def test_consumo_negativo_lanza_error(self):
        # Verifica que se eleve ValueError
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-10)


if __name__ == "__main__":
    unittest.main()
