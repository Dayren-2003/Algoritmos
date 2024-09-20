def extrapolar_ppg(ppg, mpg):
    if ppg == 0:
        return 0.0
    # Extrapolar ppg a 48 minutos
    ppg_48 = (ppg / mpg) * 48
    return round(ppg_48, 1)

# Ejemplo de uso:
ppg = 20  # Promedio de puntos por juego
mpg = 30  # Promedio de minutos jugados por juego

resultado = extrapolar_ppg(ppg, mpg)
print(f"Puntos extrapolados por 48 minutos: {resultado} puntos")
