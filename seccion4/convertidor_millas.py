# Sección 4 - Variables
# Laboratorio: Variables: un convertidor simple

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")

# Experimento adicional: conversión de temperatura
celsius = 25
fahrenheit = (celsius * 9 / 5) + 32

print(celsius, "grados Celsius son", round(fahrenheit, 2), "grados Fahrenheit")