# Prefix Sum

El prefix sum es una técnica que nos permite calcular la suma de cualquier rango en un array de manera eficiente, con
complejidad O(1) después del preprocesamiento.

Te lo explico paso a paso:

1) Primero, creamos un nuevo array donde cada posición contiene la suma de todos los elementos anteriores incluyendo el
   actual.

Por ejemplo:

```python
# Array original
arr = [3, 1, 4, 2, 5]
# Prefix sum
prefix = [3, 4, 8, 10, 15]
# Donde prefix[i] = arr[0] + arr[1] + ... + arr[i]
```

Aquí está el pseudo código para construir el prefix sum:

```
función construirPrefixSum(arr):
    n = longitud(arr)
    prefix = nuevo array de tamaño n
    prefix[0] = arr[0]
    
    para i desde 1 hasta n-1:
        prefix[i] = prefix[i-1] + arr[i]
    
    retornar prefix
```

La belleza del prefix sum es que podemos encontrar la suma de cualquier rango [L,R] en O(1) usando:

```
sumaRango(L, R) = prefix[R] - prefix[L-1]  # si L > 0
sumaRango(0, R) = prefix[R]  # si L = 0
```

Este concepto es fundamental para resolver problemas más complejos, como:

- Encontrar subarrays con suma específica
- Calcular promedios móviles
- Problemas de ventana deslizante

¿Te gustaría que te muestre un problema específico donde se aplica este concepto? O ¿tienes alguna duda sobre cómo
funciona?

Un consejo para las entrevistas: asegúrate de manejar bien los casos edge, como arrays vacíos o cuando L = 0 en las
consultas de rango.