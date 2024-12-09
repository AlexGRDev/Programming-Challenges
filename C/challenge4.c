/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */

#include <stdio.h>

int calcPoligon(char *pligon, int *a, int *b) 
{
    int area = 0;

    if (*pligon == 'T')
    {
        area = (a[0] * b[0]) / 2;
    } else if (*pligon == 'C')
    {
        area = a[0] * a[0];
    } else if (*pligon == 'R') 
    {
        area = a[0] * b[0];
    } else 
    {
        printf("Polígono no soportado\n");
    } return area;
}

int main()
{
    int a[3];
    int b[3];
    int area[3];
    char poligon[3];

    a[0] = 5;
    a[1] = 5;
    a[2] = 5;
    b[0] = 4;
    b[1] = 6;
    b[2] = 8;
    poligon[0] = 'T';
    poligon[1] = 'C';
    poligon[2] = 'R';

    int i;
    i = 0;
    while (i < 3)
    {
        area[i] = calcPoligon(poligon + i, a, b);
        printf("El área del %c es: %d\n", poligon[i], area[i]);
        i++;
    } return 0;
}
    
