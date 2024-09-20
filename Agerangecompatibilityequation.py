'''
Calcula rango de edad
'''
import math


def calcular_rango_edad(edad):
    if edad <= 14:
        # Para edades menores o iguales a 14
        min_edad = math.floor(edad - 0.10 * edad)
        max_edad = math.floor(edad + 0.10 * edad)
    else:
        # Para edades mayores a 14, aplica la regla
        min_edad = math.floor((edad / 2) + 7)
        max_edad = math.floor((edad - 7) * 2)

    return f"{min_edad}-{max_edad}"


def main():
    # Solicita al usuario su edad
    edad_usuario = int(input("Ingresa tu edad (1-100): "))

    # Verifica que la edad esté en el rango permitido
    if 1 <= edad_usuario <= 100:
        # Calcula el rango de edad
        rango_edad = calcular_rango_edad(edad_usuario)
        print(f"Según la regla, puedes salir con alguien entre {rango_edad} años.")
    else:
        print("Por favor, ingresa una edad válida entre 1 y 100.")


if __name__ == "__main__":
    main()
