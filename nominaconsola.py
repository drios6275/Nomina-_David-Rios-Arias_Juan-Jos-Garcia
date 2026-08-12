import calcular_nomina
 
"""
La interfaz de usuario del programa debe separarse del modulo
que contiene la lógica.
En este caso, la interfaz de usuario queda en NominaConsole.py
y la lógica queda en liquidador_nomina.py
"""
try:
    print("Este programa le permite calcular la nómina quincenal a pagar a un trabajador")
    salario_mensual = float( input("Salario mensual del trabajador:") )
    dias_trabajados = int( input("Número de días trabajados en la quincena:") )
    nomina = round( liquidador_nomina.calcular_nomina(salario_mensual, dias_trabajados) , 2)
    print( f"El valor de la nómina quincenal a pagar es de: {nomina}" )
except Exception as err:
    print("No se pudo calcular la nómina")
    print( str(err) )