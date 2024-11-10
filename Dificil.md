## Ejercicio 00

**sucesion de fibonachi**

**Deriecotir de entrega**: `ex00/`

**Archivo a entregar**: `fibonachi.c`

**Funciones autorizadas**: `write`

- Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0
    - La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.

**Prototipo de la función**:
```c
void    fibonachi(void);
```

## Ejemplo de salida:
```
0, 1, 1, 2, 3, 5, 8, 13...
```

## Ejercicio: 01

**Calcular el aspect ratio de una imagen a partir de una URL**

**Directorio de entrega**: `ex01/`

**Archivo a entregar**: `aspect_ratio.c`

**Funciones autorizadas**: `write`

- Crea un programa que se encargue de calcular el aspect ratio de una imagen a partir de una URL.
    - Url de ejemplo:
      `https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png`
    - Por "ratio" hacemos referencia a los valores como "16:9" de una imagen de 1920x1080px.

**Prototipo de la función**:
```c
void calcular_aspect_ratio(char *url);
