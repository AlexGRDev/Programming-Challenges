/*
    * Escribe un programa que imprima los 50 primeros números de la sucesión
    * de Fibonacci empezando en 0.
    * - La serie Fibonacci se compone por una sucesión de números en
    *   la que el siguiente siempre es la suma de los dos anteriores.
    *   0, 1, 1, 2, 3, 5, 8, 13...
 */

#include <stdio.h>
#include <stdint.h>

int fibonacci(int *num) 
{
    static int memo[51] = {0};

    if (*num == 0) 
    {
        return 0;
    } 
    else if (*num == 1) 
    {
        return 1;
    } 
    else if (memo[*num] != 0) 
    {
        return memo[*num];
    } 
    else 
    {
        int n1 = *num - 1;
        int n2 = *num - 2;

        memo[*num] = fibonacci(&n1) + fibonacci(&n2);
        return memo[*num];
    }
}

int main() 
{
    int i = 0;
    int *ptrI = &i;

    printf("Primeros 50 números de Fibonacci:\n");

    while (*ptrI <= 50) 
    {
        printf("fibonacci(%d) %d\n", *ptrI, fibonacci(&i));
        (*ptrI)++;
    }
    return 0;
}