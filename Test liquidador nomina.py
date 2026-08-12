"""
Pruebas unitarias del liquidador de nómina.
 
Los casos de prueba y sus valores esperados provienen del archivo
"liquidador_nomina_casos_prueba.xlsx".
"""
 
import unittest
from  calcular_nomina import calcular_nomina
 
 
class TestCasosNormales(unittest.TestCase):
    """Quincenas completas (15 días), distintos rangos de salario."""
 
    def test_caso_normal_1_quincena_completa(self):
        self.assertEqual(calcular_nomina(3_500_000, 15), 1_610_000)
 
    def test_caso_normal_2_salario_bajo_quincena_completa(self):
        self.assertEqual(calcular_nomina(2_000_000, 15), 920_000)
 
    def test_caso_normal_3_salario_alto_quincena_completa(self):
        self.assertEqual(calcular_nomina(4_800_000, 15), 2_208_000)
 
 
class TestCasosExtraordinarios(unittest.TestCase):
    """Situaciones límite pero válidas: ingreso a mitad de quincena,
    un solo día trabajado, salario exacto en el SMLV."""
 
    def test_ingreso_a_mitad_de_quincena_8_dias(self):
        self.assertEqual(calcular_nomina(3_500_000, 8), 858_667)
 
    def test_un_solo_dia_trabajado(self):
        self.assertEqual(calcular_nomina(1_300_000, 1), 39_867)
 
    def test_salario_exacto_en_el_smlv(self):
        self.assertEqual(calcular_nomina(1_300_000, 15), 598_000)
 
 
class TestCasosDeError(unittest.TestCase):
    """Entradas inválidas: deben lanzar ValueError con el mensaje
    correspondiente."""
 
    def test_error_salario_cero(self):
        with self.assertRaises(ValueError) as ctx:
            calcular_nomina(0, 15)
        self.assertIn("mayor que cero", str(ctx.exception))
 
    def test_error_salario_menor_al_smlv(self):
        with self.assertRaises(ValueError) as ctx:
            calcular_nomina(900_000, 15)
        self.assertIn("salario mínimo legal vigente", str(ctx.exception))
 
    def test_error_dias_en_cero(self):
        with self.assertRaises(ValueError) as ctx:
            calcular_nomina(3_500_000, 0)
        self.assertIn("entre 1 y 15", str(ctx.exception))
 
    def test_error_dias_excedidos_mayor_a_15(self):
        with self.assertRaises(ValueError) as ctx:
            calcular_nomina(3_500_000, 20)
        self.assertIn("entre 1 y 15", str(ctx.exception))
 
    def test_error_salario_negativo(self):
        # Caso adicional no cubierto explícitamente en el Excel, pero
        # cae bajo la misma regla que "salario <= 0".
        with self.assertRaises(ValueError):
            calcular_nomina(-100_000, 15)
 
    def test_error_dias_negativos(self):
        # Caso adicional: días negativos también deben rechazarse.
        with self.assertRaises(ValueError):
            calcular_nomina(3_500_000, -5)
 
 
class TestCasosEspecialesPendientesDeImplementar(unittest.TestCase):
    """
    Estos casos documentan reglas que el liquidador AÚN NO calcula:
    - Aporte al Fondo de Solidaridad Pensional (salario > 4 SMLV)
    - Modalidad de Salario Integral (salario > 10 SMLV)
    - Auxilio de Transporte (salario <= 2 SMLV)
 
    Por ahora el liquidador aplica la fórmula base (devengado -
    deducciones) sin ninguna de estas reglas adicionales, así que
    las pruebas verifican ese comportamiento actual. Cuando se
    implementen las reglas, estos valores esperados deberán
    actualizarse.
    """
 
    def test_solidaridad_gana_mas_de_4_smlv(self):
        # Pendiente: no se aplica aporte adicional al Fondo de
        # Solidaridad Pensional todavía.
        self.assertEqual(calcular_nomina(6_000_000, 15), 2_760_000)
 
    def test_salario_integral_gana_mas_de_10_smlv(self):
        # Pendiente: no se aplica la modalidad de Salario Integral
        # (factor prestacional) todavía.
        self.assertEqual(calcular_nomina(14_000_000, 15), 6_440_000)
 
    def test_auxilio_transporte_gana_2_smlv_o_menos(self):
        # Pendiente: no se suma el Auxilio de Transporte todavía.
        self.assertEqual(calcular_nomina(2_500_000, 15), 1_150_000)
 
 
if __name__ == "__main__":
    unittest.main(verbosity=2)