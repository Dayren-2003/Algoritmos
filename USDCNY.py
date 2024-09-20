'''
Convertidor de USD => CNY
'''

def convert_usd_to_cny(usd):
    # Tasa de conversión (puedes actualizarla según la tasa actual)
    conversion_rate = 6.4  # Ejemplo de tasa de conversión
    cny = usd * conversion_rate
    return f"{cny:.2f} Chinese Yuan"

# Ejemplo de uso
print(convert_usd_to_cny(10))  # Output: "64.00 Chinese Yuan"
print(convert_usd_to_cny(50))  # Output: "320.00 Chinese Yuan"
