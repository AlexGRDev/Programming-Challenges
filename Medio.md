## Ejrecicio: 00

**es un anagrama**

**Deriecotir de entrega**: `ex00/`

**Archivo a entregar**: `anagrama.c`

**Funciones autorizadas**: `ninugna`

- Escribe una funcion que reciba dos palabras (str) y retorne verdadero o falso (bool) segun sean o no anagramas.
    - Un Anagrama consiste en formar una palabra reordenando TODAS as letras de otra palabra inicial.
    - NO hace falta comprobar que ambas palabras existan.
    - Dos palabras exactamente iguales no son anagrama.

**Prototipo de la función**:
```c
bool    anagrama(char *str1, char *str2);
```

## Ejemplo de salida:
```
a.out "amor" "roma"
true

a.out "pez" "mundo"
false
```

## Ejercicio: 01

**es un número primo**

**Deriecotir de entrega**: `ex01/`

**Archivo a entregar**: `es_primo`

**Funciones autorizadas**: `write`

- Escribe un programa que se encargue de comprobar si un número es o no primo.
    - Hecho esto, imprime los números primos entre 1 y 100.

**Prototipo de la función**:
```c
int es_primo(int num);
```

## Ejemplo de salida:
```
2, 3, 5, 7, 11, 13, 17, 19...
```

## Ejercicio: 02

**Calcular el área de un polígono**

**Directorio de entrega**: `ex02/`

**Archivo a entregar**: `area_poligono.c`

**Funciones autorizadas**: `write`

- Escribe un programa que se encargue de calcular y retornar el área de un polígono.
    - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
    - La función recibirá por parámetro solo UN polígono a la vez.
    - Imprime el cálculo del área de un polígono de cada tipo.

**Prototipo de la función**:
```c
void calcular_area(int tipo, float a, float b);
```

## Ejemplo de salida:
```
a.out "triangulo" 5,10
a.out "cuadrado" 4,0
a.out "rectangulo" 6,8  

El área del triángulo es: 25.00
El área del cuadrado es: 16.00
El área del rectángulo es: 48.00
```