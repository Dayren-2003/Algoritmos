'''
Redondear decimales
'''
def redondear_a_dos_decimales(numero):
    return format(round(numero, 2), '.2f')


def main():
    # Solicita al usuario varios números, separados por espacios
    entrada = input("Ingresa números separados por espacios: ")
    numeros = map(float, entrada.split())

    # Redondea cada número y lo imprime
    resultados = [redondear_a_dos_decimales(num) for num in numeros]
    print("Números redondeados:", ' '.join(resultados))


if __name__ == "__main__":
    main()
