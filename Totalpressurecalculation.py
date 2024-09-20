'''
Calcula la presion
'''
def calcular_presion_total(M1, M2, m1, m2, V, T):
    # Convertir temperatura de Celsius a Kelvin
    T_kelvin = T + 273.15

    # Constante del gas
    R = 0.082  # dm³·atm·K⁻¹·mol⁻¹

    # Calcular la presión total
    P_total = (m1 / M1 + m2 / M2) * R * T_kelvin / V
    return P_total


# Ejemplo de uso:
M1 = 32.0  # g·mol⁻¹ (masa molar del gas 1)
M2 = 28.0  # g·mol⁻¹ (masa molar del gas 2)
m1 = 4.0  # g (masa del gas 1)
m2 = 2.0  # g (masa del gas 2)
V = 1.0  # dm³ (volumen del recipiente)
T = 25.0  # °C (temperatura)

presion_total = calcular_presion_total(M1, M2, m1, m2, V, T)
print(f"La presión total es: {presion_total:.2f} atm")
