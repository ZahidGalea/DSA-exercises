Te explico la técnica de Sliding Window (Ventana Deslizante), que es muy útil para problemas que involucran subarreglos
o subcadenas contiguos.

La idea básica es mantener una "ventana" que se desliza sobre los datos, donde la ventana representa el subconjunto
actual que estamos considerando.

Hay dos tipos principales:

1. Ventana de Tamaño Fijo:

```python
def ventanaFija(arr, k):
    n = len(arr)
    # Procesar primera ventana
    ventana = arr[0:k]
    resultado = [sum(ventana)]

    # Deslizar ventana
    for i in range(k, n):
        # Añadir nuevo elemento y quitar el primero
        ventana = ventana[1:] + [arr[i]]
        resultado.append(sum(ventana))

    return resultado
```

2. Ventana de Tamaño Variable:

```python
def ventanaVariable(arr, target):
    inicio = 0
    suma_actual = 0
    min_longitud = float('inf')

    for fin in range(len(arr)):
        suma_actual += arr[fin]

        # Contraer ventana mientras cumplamos condición
        while suma_actual >= target:
            min_longitud = min(min_longitud, fin - inicio + 1)
            suma_actual -= arr[inicio]
            inicio += 1

    return min_longitud
```

Patrón general para problemas de ventana deslizante:

```
inicio = 0
for fin in range(len(array)):
    # 1. Expandir: añadir elemento en posición 'fin'
    
    # 2. Contraer: mientras la ventana viole condición
    while ventana_necesita_contraerse:
        # remover elemento en posición 'inicio'
        inicio += 1
    
    # 3. Actualizar resultado si es necesario
```

Casos comunes donde se usa:

- Encontrar el subarreglo más largo/corto que cumple una condición
- Calcular máximos/mínimos en subarreglos de tamaño k
- Encontrar todas las subcadenas que contienen ciertos caracteres
- Problemas de límite o suma máxima en subarreglos

Tips para entrevistas:

1. Identifica si necesitas ventana fija o variable
2. Piensa en las condiciones para expandir y contraer
3. Ten cuidado con los índices al actualizar la ventana
4. Considera casos edge: array vacío, k = 0, etc.

¿Te gustaría ver algún ejemplo específico de un problema que use sliding window?