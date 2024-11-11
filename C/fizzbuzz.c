#include <unistd.h>

void print_number(int i) 
{
    if (i > 9)
    {
        print_number(i / 10);
    }
    char c = '0' + i % 10;
    write(1, &c, 1);
}

void fizzbuzz(void)
{
    int i;

    i = 1;
    while (i <= 100)
    {
        if(i % 3 == 0 && i % 5 == 0)
        {
            write(1, "fizzbuzz\n", 10);
        }
        else if(i % 3 == 0)
        {
            write(1, "fizz\n", 6);
        }
        else if(i % 5 == 0)
        {
            write(1, "buzz\n", 6);
        }
        else
        {
            print_number(i);
            write(1, "\n", 1);
        }
        i++;
    }
    
}

int  main(void)
{
    fizzbuzz();
    return(0);
}