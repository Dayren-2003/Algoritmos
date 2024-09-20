def costo_mangos(cantidad, precio_por_mango):
    # Calculamos cuántos mangos se pagan
    mangos_a_pagar = (cantidad // 3) * 2 + (cantidad % 3)
    total_costo = mangos_a_pagar * precio_por_mango
    return total_costo

# Ejemplo de uso:
cantidad = 7  # Cambia este valor por la cantidad deseada
precio_por_mango = 1.5  # Cambia este valor por el precio por mango
total = costo_mangos(cantidad, precio_por_mango)
print(f"El costo total por {cantidad} mangos es: ${total:.2f}")
