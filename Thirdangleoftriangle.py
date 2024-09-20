def calculate_third_angle(angle1, angle2):
    # La suma de los ángulos de un triángulo es 180 grados
    third_angle = 180 - (angle1 + angle2)
    return third_angle

# Ejemplo de uso
print(calculate_third_angle(60, 90))  # Output: 30
print(calculate_third_angle(45, 45))  # Output: 90
print(calculate_third_angle(30, 60))  # Output: 90
