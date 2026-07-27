# Ejercicios de Operadores Matemáticos

En este documento se presentan las soluciones y explicaciones de los ejercicios de operadores matemáticos. Cada expresión fue resuelta manualmente aplicando la prioridad de los operadores y posteriormente comprobada utilizando Python.

---

## Ejercicio 1

**Expresión:**

```python
5 + 3 * 2
```

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

### Solución y Explicación

**Paso a paso:**

1. **Identificar las operaciones y su prioridad:**

   * Suma (`+`)
   * Multiplicación (`*`)

   La multiplicación tiene mayor prioridad que la suma.

2. **Realizar la multiplicación primero:**

   * `3 * 2 = 6`

3. **Realizar la suma:**

   * `5 + 6 = 11`

**Resultado final:**

```python
11
```

---

## Ejercicio 2

**Expresión:**

```python
8 / 2 + 4 * 3
```

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

### Solución y Explicación

**Paso a paso:**

1. **Identificar las operaciones y su prioridad:**

   * División (`/`)
   * Suma (`+`)
   * Multiplicación (`*`)

   La división y la multiplicación tienen mayor prioridad que la suma. Como tienen la misma prioridad entre sí, se resuelven de izquierda a derecha.

2. **Realizar la división:**

   * `8 / 2 = 4`

3. **Realizar la multiplicación:**

   * `4 * 3 = 12`

4. **Realizar la suma:**

   * `4 + 12 = 16`

**Resultado final:**

```python
16
```

**Comprobación en Python:**

```python
8 / 2 + 4 * 3
```

Python muestra:

```python
16.0
```

Esto ocurre porque el operador `/` realiza una división que devuelve un resultado de tipo `float`.

---

## Ejercicio 3

**Expresión:**

```python
(7 + 3) * 2 - 5
```

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

### Solución y Explicación

**Paso a paso:**

1. **Identificar las operaciones y su prioridad:**

   * Paréntesis (`()`)
   * Multiplicación (`*`)
   * Resta (`-`)

   Las operaciones dentro de los paréntesis tienen prioridad.

2. **Resolver el paréntesis:**

   * `7 + 3 = 10`

3. **Realizar la multiplicación:**

   * `10 * 2 = 20`

4. **Realizar la resta:**

   * `20 - 5 = 15`

**Resultado final:**

```python
15
```

---

## Ejercicio 4

**Expresión:**

```python
10 - 4 + 2 * 3
```

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

### Solución y Explicación

**Paso a paso:**

1. **Identificar las operaciones y su prioridad:**

   * Resta (`-`)
   * Suma (`+`)
   * Multiplicación (`*`)

   La multiplicación tiene mayor prioridad que la suma y la resta.

2. **Realizar la multiplicación:**

   * `2 * 3 = 6`

3. **Resolver las operaciones restantes de izquierda a derecha:**

   * `10 - 4 = 6`

4. **Realizar la suma:**

   * `6 + 6 = 12`

**Resultado final:**

```python
12
```

---

## Ejercicio 5

**Expresión:**

```python
(10 / 2) * (3 + 2) - 4
```

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

### Solución y Explicación

**Paso a paso:**

1. **Resolver el primer paréntesis:**

   * `10 / 2 = 5`

2. **Resolver el segundo paréntesis:**

   * `3 + 2 = 5`

3. **Realizar la multiplicación:**

   * `5 * 5 = 25`

4. **Realizar la resta:**

   * `25 - 4 = 21`

**Resultado final:**

```python
21
```

**Comprobación en Python:**

```python
(10 / 2) * (3 + 2) - 4
```

Python muestra:

```python
21.0
```

Esto ocurre porque el operador `/` devuelve un resultado de tipo `float`.

---

## Ejercicio 6

**Expresión:**

```python
2 + 3 * (4 - 1)
```

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

### Solución y Explicación

**Paso a paso:**

1. **Resolver el paréntesis:**

   * `4 - 1 = 3`

2. **Realizar la multiplicación:**

   * `3 * 3 = 9`

3. **Realizar la suma:**

   * `2 + 9 = 11`

**Resultado final:**

```python
11
```

---

## Ejercicio 7

**Expresión:**

```python
5 * 2 ** 3
```

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

### Solución y Explicación

**Paso a paso:**

1. **Identificar las operaciones y su prioridad:**

   * Multiplicación (`*`)
   * Potencia (`**`)

   La potencia tiene mayor prioridad que la multiplicación.

2. **Realizar la potencia:**

   * `2 ** 3 = 8`

3. **Realizar la multiplicación:**

   * `5 * 8 = 40`

**Resultado final:**

```python
40
```

---

## Ejercicio 8

**Expresión:**

```python
6 + 4 / 2 ** 2
```

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

### Solución y Explicación

**Paso a paso:**

1. **Identificar las operaciones y su prioridad:**

   * Suma (`+`)
   * División (`/`)
   * Potencia (`**`)

   La potencia tiene mayor prioridad que la división y la división tiene mayor prioridad que la suma.

2. **Realizar la potencia:**

   * `2 ** 2 = 4`

3. **Realizar la división:**

   * `4 / 4 = 1`

4. **Realizar la suma:**

   * `6 + 1 = 7`

**Resultado final:**

```python
7
```

**Comprobación en Python:**

```python
6 + 4 / 2 ** 2
```

Python muestra:

```python
7.0
```

Esto ocurre porque el operador `/` devuelve un resultado de tipo `float`.

---

## Ejercicio 9

**Expresión:**

```python
10 % 3 + 2 * 5
```

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

### Solución y Explicación

**Paso a paso:**

1. **Identificar las operaciones y su prioridad:**

   * Módulo (`%`)
   * Suma (`+`)
   * Multiplicación (`*`)

   El módulo y la multiplicación tienen mayor prioridad que la suma. Como tienen la misma prioridad, se resuelven de izquierda a derecha.

2. **Realizar el módulo:**

   * `10 % 3 = 1`

   El operador módulo (`%`) devuelve el residuo de una división. Al dividir 10 entre 3, el residuo es 1.

3. **Realizar la multiplicación:**

   * `2 * 5 = 10`

4. **Realizar la suma:**

   * `1 + 10 = 11`

**Resultado final:**

```python
11
```

---

## Ejercicio 10

**Expresión:**

```python
(8 + 2) * 3 ** 2
```

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

### Solución y Explicación

**Paso a paso:**

1. **Identificar las operaciones y su prioridad:**

   * Paréntesis (`()`)
   * Multiplicación (`*`)
   * Potencia (`**`)

2. **Resolver el paréntesis:**

   * `8 + 2 = 10`

3. **Realizar la potencia:**

   * `3 ** 2 = 9`

4. **Realizar la multiplicación:**

   * `10 * 9 = 90`

**Resultado final:**

```python
90
```

---

## Ejercicio 11

**Expresión:**

```python
7 + 2 * (3 + 5) / 4
```

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

### Solución y Explicación

**Paso a paso:**

1. **Identificar las operaciones y su prioridad:**

   * Suma (`+`)
   * Multiplicación (`*`)
   * Paréntesis (`()`)
   * División (`/`)

   Primero se resuelve el contenido de los paréntesis. Después se realizan la multiplicación y la división de izquierda a derecha. Finalmente se realiza la suma.

2. **Resolver el paréntesis:**

   * `3 + 5 = 8`

3. **Realizar la multiplicación:**

   * `2 * 8 = 16`

4. **Realizar la división:**

   * `16 / 4 = 4`

5. **Realizar la suma:**

   * `7 + 4 = 11`

**Resultado final:**

```python
11
```

**Comprobación en Python:**

```python
7 + 2 * (3 + 5) / 4
```

Python muestra:

```python
11.0
```

Esto ocurre porque el operador `/` devuelve un resultado de tipo `float`.

---

## Ejercicio 12

**Expresión:**

```python
2 ** 3 * 4 / 2
```

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

### Solución y Explicación

**Paso a paso:**

1. **Identificar las operaciones y su prioridad:**

   * Potencia (`**`)
   * Multiplicación (`*`)
   * División (`/`)

   La potencia tiene mayor prioridad. La multiplicación y la división tienen la misma prioridad y se resuelven de izquierda a derecha.

2. **Realizar la potencia:**

   * `2 ** 3 = 8`

3. **Realizar la multiplicación:**

   * `8 * 4 = 32`

4. **Realizar la división:**

   * `32 / 2 = 16`

**Resultado final:**

```python
16
```

**Comprobación en Python:**

```python
2 ** 3 * 4 / 2
```

Python muestra:

```python
16.0
```

Esto ocurre porque el operador `/` devuelve un resultado de tipo `float`.

---

## Ejercicio 13

**Expresión:**

```python
9 - 6 + 3 ** 2
```

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

### Solución y Explicación

**Paso a paso:**

1. **Identificar las operaciones y su prioridad:**

   * Resta (`-`)
   * Suma (`+`)
   * Potencia (`**`)

   La potencia tiene mayor prioridad que la suma y la resta.

2. **Realizar la potencia:**

   * `3 ** 2 = 9`

3. **Resolver la resta:**

   * `9 - 6 = 3`

4. **Realizar la suma:**

   * `3 + 9 = 12`

**Resultado final:**

```python
12
```

---

## Ejercicio 14

**Expresión:**

```python
(7 - 2) * 5 + 3 ** 2
```

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

### Solución y Explicación

**Paso a paso:**

1. **Identificar las operaciones y su prioridad:**

   * Paréntesis (`()`)
   * Multiplicación (`*`)
   * Suma (`+`)
   * Potencia (`**`)

   Primero se resuelve el contenido del paréntesis y la potencia tiene prioridad sobre la multiplicación y la suma.

2. **Resolver el paréntesis:**

   * `7 - 2 = 5`

3. **Realizar la potencia:**

   * `3 ** 2 = 9`

4. **Realizar la multiplicación:**

   * `5 * 5 = 25`

5. **Realizar la suma:**

   * `25 + 9 = 34`

**Resultado final:**

```python
34
```

---

## Ejercicio 15

**Expresión:**

```python
4 * 2 ** 3 / 8 + 1
```

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

### Solución y Explicación

**Paso a paso:**

1. **Identificar las operaciones y su prioridad:**

   * Multiplicación (`*`)
   * Potencia (`**`)
   * División (`/`)
   * Suma (`+`)

   La potencia tiene mayor prioridad. Después, la multiplicación y la división tienen la misma prioridad y se resuelven de izquierda a derecha. Finalmente se realiza la suma.

2. **Realizar la potencia:**

   * `2 ** 3 = 8`

3. **Realizar la multiplicación:**

   * `4 * 8 = 32`

4. **Realizar la división:**

   * `32 / 8 = 4`

5. **Realizar la suma:**

   * `4 + 1 = 5`

**Resultado final:**

```python
5
```

**Comprobación en Python:**

```python
4 * 2 ** 3 / 8 + 1
```

Python muestra:

```python
5.0
```

Esto ocurre porque el operador `/` devuelve un resultado de tipo `float`.

---

## Conclusión

Los ejercicios permitieron comprobar la importancia de conocer la prioridad de los operadores matemáticos en Python. El orden general aplicado en estos ejercicios fue:

1. Paréntesis.
2. Potencias (`**`).
3. Multiplicaciones (`*`), divisiones (`/`) y módulos (`%`), de izquierda a derecha.
4. Sumas (`+`) y restas (`-`), de izquierda a derecha.

Las expresiones fueron resueltas primero de forma manual y posteriormente comprobadas mediante Python. Se pudo observar que el operador `/` produce resultados de tipo `float`, por lo que algunas respuestas aparecen con `.0` al ejecutarlas en Python, aunque matemáticamente representen un número entero.
