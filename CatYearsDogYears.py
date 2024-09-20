def calculate_age(human_years):
    if human_years < 1:
        return None  # Debe ser un valor mayor o igual a 1

    # Cálculo de años de gato
    if human_years == 1:
        cat_years = 15
    elif human_years == 2:
        cat_years = 15 + 9
    else:
        cat_years = 15 + 9 + (human_years - 2) * 4

    # Cálculo de años de perro
    if human_years == 1:
        dog_years = 15
    elif human_years == 2:
        dog_years = 15 + 9
    else:
        dog_years = 15 + 9 + (human_years - 2) * 5

    return [human_years, cat_years, dog_years]

# Ejemplo de uso
print(calculate_age(1))  # Output: [1, 15, 15]
print(calculate_age(2))  # Output: [2, 24, 24]
print(calculate_age(3))  # Output: [3, 28, 29]
print(calculate_age(4))  # Output: [4, 32, 34]
