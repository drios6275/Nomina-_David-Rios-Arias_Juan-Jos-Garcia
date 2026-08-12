
"""
Liquidador de nómina quincenal.
 
Calcula el salario neto a pagar a un trabajador por una quincena,
según el salario mensual y los días trabajados.
 
NOTA: El Auxilio de Transporte, el aporte al Fondo de Solidaridad
Pensional (salarios > 4 SMLV) y la modalidad de Salario Integral
(salarios > 10 SMLV) todavía NO están implementados en este
liquidador. Quedan pendientes para una siguiente iteración.
"""
 
# ---- Parámetros del sistema (ver hoja "Parámetros" del Excel) ----
SMLV = 1_300_000            # Salario mínimo legal vigente de referencia
DIAS_MES_BASE = 30          # Días del mes usados como base de cálculo
DIAS_MAX_QUINCENA = 15      # Días máximos que puede tener una quincena
TASA_DEDUCCION = 0.08       # 4% salud + 4% pensión
 
 
def calcular_nomina(salario_mensual: float, dias_trabajados: int) -> float:
    """
    Calcula el salario neto a pagar en una quincena.
 
    Parámetros
    ----------
    salario_mensual : float
        Salario mensual del trabajador. Debe ser > 0 y >= SMLV.
    dias_trabajados : int
        Días trabajados dentro de la quincena. Debe estar entre 1 y 15.
 
    Retorna
    -------
    float
        Salario neto a pagar, redondeado al entero más cercano.
 
    Lanza
    -----
    ValueError
        Si el salario o los días trabajados no son válidos.
    """
    if salario_mensual <= 0:
        raise ValueError("El salario debe ser mayor que cero")
 
    if salario_mensual < SMLV:
        raise ValueError(
            "El salario no puede ser inferior al salario mínimo legal "
            "vigente (SMLV)"
        )
 
    if not (1 <= dias_trabajados <= DIAS_MAX_QUINCENA):
        raise ValueError(
            f"Los días trabajados deben estar entre 1 y {DIAS_MAX_QUINCENA}"
        )
 
    salario_devengado = salario_mensual / DIAS_MES_BASE * dias_trabajados
    deducciones = salario_devengado * TASA_DEDUCCION
 
    return round(salario_devengado - deducciones)
 
 
if __name__ == "__main__":
    print("Este programa calcula la nómina a pagar de una empresa")
 
    salario_mensual = int(input("Ingrese el salario mensual: "))
    dias_trabajados = int(input("Ingrese el número de días trabajados: "))
 
    try:
        nomina = calcular_nomina(salario_mensual, dias_trabajados)
        print(f"El valor de la nómina quincenal es {nomina}")
    except ValueError as error:
        print(f"Error: {error}")