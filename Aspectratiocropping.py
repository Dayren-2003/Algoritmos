import math

def convert_to_16_9(x, y):
    # Calcular la nueva resolución X manteniendo la altura (y)
    # Proporción 16:9 => 16/9 = 1.777...
    new_x = math.ceil((16 / 9) * y)
    return (new_x, y)

# Ejemplo de uso
print(convert_to_16_9(1920, 1080))  # Output: (1920, 1080)
print(convert_to_16_9(1440, 1080))  # Output: (1920, 1080)
print(convert_to_16_9(800, 600))    # Output: (1067, 600)
