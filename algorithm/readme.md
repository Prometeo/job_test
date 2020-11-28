# Encontrar los dos primeros elementos que sumen "y"

En la primera solución se recorre el arreglo, se compara el número actual del arreglo con el resultado deseado de la suma, si el número es menor al resultado se calcula la diferencia, entonces ese numero, resultado de la diferencia es buscado dentro del arreglo, si no lo encuentra se realiza el mismo procedimiento con el siguiente número del arreglo.

En la Segunda solución se ordena el arreglo de menor a mayor usando el método quicksort, una vez ordenado el se aplica la primera solución sobre este arreglo resultante.

## Ventajas y Desventajas
1. Aplicando solo la primera solución puede ser rápido y conveniente para un arreglo pequeño, pero si el arreglo es muy grande no es un algoritmo conveniente.
2. La segunda solución puede ser mas eficiente aplicado a arreglos con una gran cantidad de elementos, pero el arreglo va a ser modificado, por lo tanto no se puede aplicar sobre arreglos que deban ser inmutables.
