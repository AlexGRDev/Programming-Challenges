/*
    * Escribe un programa que muestre por consola (con un print) los
    * números de 1 a 100 (ambos incluidos y con un salto de línea entre
    * cada impresión), sustituyendo los siguientes:
    * - Múltiplos de 3 por la palabra "fizz".
    * - Múltiplos de 5 por la palabra "buzz".
    * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
*/

#include <stdio.h>

int fizzbuzz(int *num) 
{
    if (*num % 3 == 0 && *num % 5 == 0) 
    {
        printf("fizzbuzz\n");
    } else if (*num % 3 == 0)
    {
        printf("fizz\n");
    } else if (*num % 5 == 0)
    {
        printf("buzz\n");
    } return printf("%d\n", *num);
}

int main() 
{
    int i;
    int *ptrI = &i;


    i = 1;
    while (*ptrI <= 100) 
    {
        fizzbuzz(&i);
        (*ptrI)++;
    } return 0;
}
