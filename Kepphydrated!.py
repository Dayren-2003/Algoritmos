'''
Mantantente Hidratado
'''
import math

def litros_de_agua(tiempo_horas):
    litros_por_hora = 0.5
    litros_totales = tiempo_horas * litros_por_hora
    return math.floor(litros_totales)

# Ejemplo de uso:
tiempo = 3.7  # Puedes cambiar este valor
litros = litros_de_agua(tiempo)
print(f"Nathan beberá {litros} litros de agua.")