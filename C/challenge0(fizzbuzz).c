#include <stdio.h>

void fizzbuzz()
{
    int i;
    int *ptrI = &i;

    i = 1;

    while (*ptrI <= 100)
    {
        if (*ptrI % 3 == 0 & *ptrI % 5 == 0)
        {
            printf("fizzbuzz\n");
        }
        else if (*ptrI % 3 == 0)
        {
            printf("fizz\n");
        }
        else if (*ptrI % 5 == 0)
        {
            printf("buzz\n");
        }
        else
        {
            printf("%d", *ptrI);
        }
        (*ptrI)++;
    }
    
}

int main()
{
    fizzbuzz();
    return(0);
}