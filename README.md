# Liquidador de Nómina Quincenal

Programa en Python que calcula el salario neto a pagar a un trabajador por
una quincena, a partir de su salario mensual y los días trabajados.

## Estructura del proyecto

El proyecto separa la **lógica de negocio** de la **interfaz de usuario**,
siguiendo el principio de responsabilidad única:

| Archivo | Responsabilidad |
|---|---|
| `liquidador_nomina.py` | Lógica de cálculo de la nómina (`calcular_nomina`) y validaciones. |
| `NominaConsole.py` | Interfaz de consola: pide datos al usuario y muestra el resultado. |
| `test_liquidador_nomina.py` | Pruebas unitarias (`unittest`) que validan la lógica. |

## Cómo funciona el cálculo

```
salario_devengado = salario_mensual / 30 * días_trabajados
deducciones        = salario_devengado * 8%   (4% salud + 4% pensión)
salario_neto       = salario_devengado - deducciones
```

### Parámetros del sistema

| Parámetro | Valor |
|---|---|
| SMLV de referencia | $1.300.000 |
| Tasa de deducción (salud + pensión) | 8% |
| Días base del mes | 30 |
| Días máximos por quincena | 15 |

### Validaciones

La función `calcular_nomina` lanza `ValueError` si:
- El salario mensual es menor o igual a 0.
- El salario mensual es menor al SMLV.
- Los días trabajados no están entre 1 y 15.

### Pendiente por implementar

Estas reglas **aún no están implementadas** en el liquidador:
- Auxilio de transporte (salarios ≤ 2 SMLV).
- Aporte al Fondo de Solidaridad Pensional (salarios > 4 SMLV).
- Modalidad de Salario Integral (salarios > 10 SMLV).

Los casos de prueba correspondientes documentan este comportamiento
pendiente para que se actualicen cuando se implementen.

## Cómo ejecutar el programa

```bash
python3 NominaConsole.py
```

El programa pedirá el salario mensual y los días trabajados, y mostrará
el valor de la nómina quincenal a pagar.

## Cómo ejecutar las pruebas

Desde la terminal, en la carpeta del proyecto:

```bash
python3 -m unittest test_liquidador_nomina -v
```

También puedes ejecutarlas desde el panel **Testing** de VSCode una vez
configurado con `unittest` como framework de pruebas.

### Casos de prueba cubiertos

- **Casos normales**: quincenas completas con distintos rangos de salario.
- **Casos extraordinarios**: ingreso a mitad de quincena, un solo día
  trabajado, salario exacto en el SMLV.
- **Casos de error**: salario en cero, negativo o menor al SMLV; días en
  cero, negativos o mayores a 15.
- **Casos especiales (pendientes)**: solidaridad pensional, salario
  integral y auxilio de transporte — documentan el comportamiento actual
  mientras esas reglas no se implementan.

## Requisitos

- Python 3.x (no requiere librerías externas).

## Autores

David Ríos Arias, Juan José García
