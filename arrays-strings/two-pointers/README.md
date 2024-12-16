Te explico la técnica de dos punteros (Two Pointers), que es muy útil para problemas que involucran búsqueda de pares o
manipulación de arrays/strings.

Hay varios patrones comunes de dos punteros:

1. Punteros desde extremos opuestos:

```python
def dosExtremos(arr):
    izq = 0
    der = len(arr) - 1

    while izq < der:
        # Procesar arr[izq] y arr[der]
        if condicion:
            izq += 1
        else:
            der -= 1
```

2. Punteros con diferente velocidad (rápido y lento):

```python
def dosVelocidades(arr):
    lento = 0
    rapido = 0

    while rapido < len(arr):
        if condicion:
            # Procesar usando lento
            lento += 1
        rapido += 1
```

3. Punteros en paralelo:

```python
def dosPunterosPalalelos(arr1, arr2):
    p1 = 0
    p2 = 0

    while p1 < len(arr1) and p2 < len(arr2):
        # Comparar arr1[p1] y arr2[p2]
        if condicion:
            p1 += 1
        else:
            p2 += 1
```

Problemas típicos donde se usa:

1. Encontrar pares que suman un valor objetivo (en array ordenado)

```python
def encontrarParSuma(arr, objetivo):
    izq = 0
    der = len(arr) - 1

    while izq < der:
        suma = arr[izq] + arr[der]
        if suma == objetivo:
            return [izq, der]
        elif suma < objetivo:
            izq += 1
        else:
            der -= 1

    return []
```

2. Detectar ciclos en una linked list:

```python
def detectarCiclo(head):
    lento = rapido = head

    while rapido and rapido.next:
        lento = lento.next
        rapido = rapido.next.next
        if lento == rapido:
            return True

    return False
```

Tips para entrevistas:

1. Identifica el patrón adecuado para tu problema
2. Cuida las condiciones de parada del while
3. Maneja casos edge: arrays vacíos, un solo elemento
4. Verifica que los punteros no se crucen cuando no deben
5. En arrays ordenados, dos punteros suele ser más eficiente que otras soluciones

Usos comunes:

- Encontrar pares/tripletas en arrays ordenados
- Eliminar duplicados
- Palingromos
- Merge de arrays ordenados
- Detectar ciclos
- Encontrar el elemento del medio

¿Te gustaría ver algún problema específico usando dos punteros?