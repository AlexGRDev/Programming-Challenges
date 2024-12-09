/*
    * Escribe un programa que se encargue de comprobar si un número es o no primo.
    * Hecho esto, imprime los números primos entre 1 y 100.
*/

#include <stdio.h>
#include <stdbool.h>

bool es_primo(int *n)
{
    if (*n <= 1) return false;

    int i;
    
    i = 2;
    while (i <= *n / 2)
    {
        if (*n % i == 0) return false;
        i++;
    } return true;
}

int main()
{
    int i;
    int *ptrI = &i;

    *ptrI = 1;
    while (*ptrI <= 100)
    {
        if (es_primo(&i))
        {
            printf("%d\n", *ptrI);
        } (*ptrI)++;
    } return 0;
}

    
