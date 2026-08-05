# Salario Mínimo Legal Vigente (ajusta este valor según el año que necesites)
SMLV = 1300000


def calcular_nomina(salario_mensual, dias_trabajados):
    """
    Calcula el monto a pagar de nómina quincenal.
    - Si el salario es 0, retorna 0.
    - Si los días trabajados son 0, retorna 0.
    - Los días trabajados se limitan a un máximo de 15 (quincena).
    - Se aplica un descuento de ley del 8% (4% salud + 4% pensión).
    """
    if salario_mensual == 0:
        return 0

    if dias_trabajados == 0:
        return 0

    # Tope de días por quincena
    if dias_trabajados > 15:
        dias_trabajados = 15

    salario_diario = salario_mensual / 30
    monto_bruto = salario_diario * dias_trabajados

    # Descuento de ley (8%)
    monto_neto = monto_bruto * 0.92

    return monto_neto


# ------------------ PRUEBAS ------------------

def probar_salario0():
    # Datos de entrada
    salario_mensual = 0
    dias_trabajados = 15

    # Dato esperado
    monto_esperado = 0

    # Ejecutar función
    nomina_calculada = calcular_nomina(salario_mensual, dias_trabajados)

    # Validar resultado
    if nomina_calculada == monto_esperado:
        print("✅ probar_salario0: Prueba pasó correctamente")
    else:
        print(f"❌ probar_salario0: se esperaba {monto_esperado}, se obtuvo {nomina_calculada}")


def probar_menor_SMLV():
    salario_mensual = 900000
    dias_trabajados = 15

    monto_esperado = 414000

    nomina_calculada = calcular_nomina(salario_mensual, dias_trabajados)

    if nomina_calculada == monto_esperado:
        print("✅ probar_menor_SMLV: Prueba pasó correctamente")
    else:
        print(f"❌ probar_menor_SMLV: se esperaba {monto_esperado}, se obtuvo {nomina_calculada}")


def probar_dias_en_cero():
    salario_mensual = 3500000
    dias_trabajados = 0

    monto_esperado = 0

    nomina_calculada = calcular_nomina(salario_mensual, dias_trabajados)

    if nomina_calculada == monto_esperado:
        print("✅ probar_dias_en_cero: Prueba pasó correctamente")
    else:
        print(f"❌ probar_dias_en_cero: se esperaba {monto_esperado}, se obtuvo {nomina_calculada}")


def probar_dias_mayores_a_15():
    salario_mensual = 3500000
    dias_trabajados = 20

    monto_esperado = 1610000

    nomina_calculada = calcular_nomina(salario_mensual, dias_trabajados)

    if nomina_calculada == monto_esperado:
        print("✅ probar_dias_mayores_a_15: Prueba pasó correctamente")
    else:
        print(f"❌ probar_dias_mayores_a_15: se esperaba {monto_esperado}, se obtuvo {nomina_calculada}")


# Ejecutar todas las pruebas
if __name__ == "__main__":
    probar_salario0()
    probar_menor_SMLV()
    probar_dias_en_cero()
    probar_dias_mayores_a_15()