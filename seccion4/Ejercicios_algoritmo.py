"""
LAB - Ejercicios de Algoritmos
Desarrollador de mecánicas de gameplay
"""
 
# ============================================
# 1. Puntaje total de un jugador
# ============================================
print("--- Ejercicio 1: Puntaje total ---")
nivel1 = float(input("Puntos obtenidos en el nivel 1: "))
nivel2 = float(input("Puntos obtenidos en el nivel 2: "))
nivel3 = float(input("Puntos obtenidos en el nivel 3: "))
puntaje_total = nivel1 + nivel2 + nivel3
print(f"El puntaje total del jugador es: {puntaje_total}\n")
 
 
# ============================================
# 2. Tiempo total de juego (en segundos)
# ============================================
print("--- Ejercicio 2: Tiempo total en segundos ---")
horas = float(input("Horas jugadas: "))
minutos = float(input("Minutos jugados: "))
segundos = float(input("Segundos jugados: "))
tiempo_total_seg = horas * 3600 + minutos * 60 + segundos
print(f"El tiempo total jugado es: {tiempo_total_seg} segundos\n")
 
 
# ============================================
# 3. Daño total causado por un personaje
# ============================================
print("--- Ejercicio 3: Daño total ---")
ataque1 = float(input("Daño del ataque 1: "))
ataque2 = float(input("Daño del ataque 2: "))
ataque3 = float(input("Daño del ataque 3: "))
danio_total = ataque1 + ataque2 + ataque3
print(f"El daño total causado es: {danio_total}\n")
 
 
# ============================================
# 4. Experiencia total ganada
# ============================================
print("--- Ejercicio 4: Experiencia total ---")
mision1 = float(input("Experiencia ganada en la misión 1: "))
mision2 = float(input("Experiencia ganada en la misión 2: "))
mision3 = float(input("Experiencia ganada en la misión 3: "))
exp_total = mision1 + mision2 + mision3
print(f"La experiencia total acumulada es: {exp_total}\n")
 
 
# ============================================
# 5. Porcentaje de vida restante
# ============================================
print("--- Ejercicio 5: Porcentaje de vida restante ---")
vida_maxima = float(input("Vida máxima del personaje: "))
vida_actual = float(input("Vida actual del personaje: "))
porcentaje_vida = (vida_actual / vida_maxima) * 100
print(f"El porcentaje de vida restante es: {porcentaje_vida}%\n")
 
 
# ============================================
# 6. Oro total recolectado
# ============================================
print("--- Ejercicio 6: Oro total recolectado ---")
oro1 = float(input("Oro recolectado en la misión 1: "))
oro2 = float(input("Oro recolectado en la misión 2: "))
oro3 = float(input("Oro recolectado en la misión 3: "))
oro_total = oro1 + oro2 + oro3
print(f"El oro total acumulado es: {oro_total}\n")
 
 
# ============================================
# 7. Velocidad promedio de un vehículo
# ============================================
print("--- Ejercicio 7: Velocidad promedio ---")
distancia = float(input("Distancia recorrida (km): "))
tiempo = float(input("Tiempo tomado (horas): "))
velocidad_promedio = distancia / tiempo
print(f"La velocidad promedio del vehículo es: {velocidad_promedio} km/h\n")
 
 
# ============================================
# 8. Costo total de mejoras
# ============================================
print("--- Ejercicio 8: Costo total de mejoras ---")
mejora1 = float(input("Costo de la mejora 1: "))
mejora2 = float(input("Costo de la mejora 2: "))
mejora3 = float(input("Costo de la mejora 3: "))
costo_total_mejoras = mejora1 + mejora2 + mejora3
print(f"El costo total de las mejoras es: {costo_total_mejoras}\n")
 
 
# ============================================
# 9. Tiempo restante para completar una misión
# ============================================
print("--- Ejercicio 9: Tiempo restante de misión ---")
tiempo_total_mision = float(input("Tiempo total de la misión (minutos): "))
tiempo_transcurrido = float(input("Tiempo transcurrido (minutos): "))
tiempo_restante = tiempo_total_mision - tiempo_transcurrido
print(f"El tiempo restante para completar la misión es: {tiempo_restante} minutos\n")
 
 
# ============================================
# 10. Nivel promedio de un equipo de jugadores
# ============================================
print("--- Ejercicio 10: Nivel promedio del equipo ---")
jugador1 = float(input("Nivel del jugador 1: "))
jugador2 = float(input("Nivel del jugador 2: "))
jugador3 = float(input("Nivel del jugador 3: "))
nivel_promedio = (jugador1 + jugador2 + jugador3) / 3
print(f"El nivel promedio del equipo es: {nivel_promedio}\n")
 
 
# ============================================
# 11. Daño crítico en un ataque
# ============================================
print("--- Ejercicio 11: Daño crítico ---")
danio_base = float(input("Daño base del ataque: "))
multiplicador_critico = float(input("Multiplicador crítico: "))
danio_critico = danio_base * multiplicador_critico
print(f"El daño crítico es: {danio_critico}\n")
 
 
# ============================================
# 12. Tiempo total de juego en horas y minutos
# ============================================
print("--- Ejercicio 12: Conversión de minutos a horas y minutos ---")
tiempo_total_min = float(input("Tiempo total jugado (minutos): "))
horas_convertidas = int(tiempo_total_min // 60)
minutos_restantes = int(tiempo_total_min % 60)
print(f"El tiempo total jugado es: {horas_convertidas} horas y {minutos_restantes} minutos\n")
 
 
# ============================================
# 13. Porcentaje de misiones completadas
# ============================================
print("--- Ejercicio 13: Porcentaje de misiones completadas ---")
total_misiones = float(input("Número total de misiones: "))
misiones_completadas = float(input("Número de misiones completadas: "))
porcentaje_misiones = (misiones_completadas / total_misiones) * 100
print(f"El porcentaje de misiones completadas es: {porcentaje_misiones}%\n")
 
 
# ============================================
# 14. Costo total de objetos comprados
# ============================================
print("--- Ejercicio 14: Costo total de objetos comprados ---")
objeto1 = float(input("Costo del objeto 1: "))
objeto2 = float(input("Costo del objeto 2: "))
objeto3 = float(input("Costo del objeto 3: "))
costo_total_objetos = objeto1 + objeto2 + objeto3
print(f"El costo total de los objetos comprados es: {costo_total_objetos}\n")
 
 
# ============================================
# 15. Tiempo promedio de una partida
# ============================================
print("--- Ejercicio 15: Tiempo promedio de partidas ---")
partida1 = float(input("Tiempo de la partida 1 (minutos): "))
partida2 = float(input("Tiempo de la partida 2 (minutos): "))
partida3 = float(input("Tiempo de la partida 3 (minutos): "))
tiempo_promedio = (partida1 + partida2 + partida3) / 3
print(f"El tiempo promedio de las partidas es: {tiempo_promedio} minutos\n")
 
 
# ============================================
# 16. Porcentaje de enemigos derrotados
# ============================================
print("--- Ejercicio 16: Porcentaje de enemigos derrotados ---")
total_enemigos = float(input("Número total de enemigos: "))
enemigos_derrotados = float(input("Número de enemigos derrotados: "))
porcentaje_enemigos = (enemigos_derrotados / total_enemigos) * 100
print(f"El porcentaje de enemigos derrotados es: {porcentaje_enemigos}%\n")