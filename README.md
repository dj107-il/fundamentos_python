# Fundamentos de Python - Variables, Operadores y Manipulación de Cadenas

Repositorio del proyecto de la actividad **GA1-220501093-04-AA1-EV01**, donde se desarrollan los laboratorios de las secciones 1 a 4 de la guía "Fundamentos de Python": funciones de salida (`print()`), literales, operadores matemáticos y variables.

## Estructura del repositorio

```
fundamentos_python/
├── seccion1/   # Función print(), argumentos y formato de salida
├── seccion2/   # Literales de Python (cadenas)
├── seccion3/   # Operadores matemáticos
├── seccion4/   # Variables, convertidor simple, operadores y expresiones
└── README.md
```

## Cómo ejecutar los scripts

Cada archivo `.py` es independiente y se ejecuta directamente con Python 3:

```bash
python seccion1/trabajando_funcion_print.py
python seccion3/operadores_matematicos.py
```

No se requieren librerías externas, solo tener Python 3 instalado.

## Sección 1 – La función `print()`

Se trabajó con los argumentos `sep` y `end`, el uso de `\n` para saltos de línea y la construcción de figuras con texto.

**Ejemplo de salida** (`trabajando_funcion_print.py`):

```
¡Hola, Mundo!-
La Witsi Witsi Araña
subió a su telaraña.

Vino la lluvia
y se la llevó.
Mi-nombre-es-Diego
```

## Sección 2 – Literales de Python

Se practicó el manejo de cadenas con comillas anidadas, usando `\"` para escapar comillas dobles dentro de un mismo string.

**Ejemplo de salida** (`literales_python.py`):

```
"Estoy"""aprendiendo"""""Python"""
```

## Sección 3 – Operadores matemáticos

Se resolvieron 15 expresiones aritméticas aplicando la precedencia de operadores de Python: primero paréntesis, luego potencias (`**`), después multiplicación/división/módulo (de izquierda a derecha), y por último suma/resta.

Cada ejercicio fue resuelto primero a mano y luego comprobado ejecutando la expresión en Python. Se observó que el operador `/` siempre devuelve un resultado `float`, por lo que varios resultados exactos aparecen con `.0` (por ejemplo, `8 / 2 + 4 * 3` da `16.0` en vez de `16`).

**Ejemplo:**

```python
5 + 3 * 2   # Primero se multiplica: 3*2=6, luego se suma: 5+6 = 11
```

La documentación completa de los 15 ejercicios, con el paso a paso de cada uno, está en [`seccion3/operadores.md`](./seccion3/operadores.md). El código que comprueba cada resultado en Python está en [`seccion3/operadores_matematicos.py`](./seccion3/operadores_matematicos.py).

## Sección 4 – Variables

- **`variables_manzana.py`**: creación de variables para cantidades (manzanas de Juan, María y Adán), cálculo de totales y operaciones aritméticas básicas (suma, resta, multiplicación, división, división entera y módulo).
- **`convertidor_millas.py`**: convertidor simple entre millas y kilómetros, con un experimento adicional de conversión de Celsius a Fahrenheit.
- **`operadores y expresiones.py`**: evaluación de la expresión polinómica `3x³ - 2x² + 3x - 1` para un valor de `x`.
- **`Ejercicios_algoritmo.py`**: conjunto de algoritmos aplicados a un caso de gameplay (cálculo de puntajes, tiempos, daño, experiencia, etc.), usando variables y operadores para resolver problemas prácticos.

**Ejemplo de salida** (`variables_manzana.py`):

```
3, 5, 6
14
Número total de manzanas: 14
Suma: 14
Resta: 6
Multiplicación: 40
División: 2.5
División entera: 2
Módulo: 2
```

## Conclusión

El proyecto permitió aplicar de forma práctica los conceptos básicos de Python: literales, variables, tipos de datos y operadores aritméticos, reforzando además el uso de `print()` para formatear salidas de manera clara. Se evidenció la importancia de conocer la precedencia de operadores para predecir correctamente el resultado de una expresión antes de ejecutarla.