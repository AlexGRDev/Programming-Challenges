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

int fizzbuzz(int multiplo_3, int multiplo_5)
{
    int i;

    i = 1;
    while (i <= 100)
    {
        if (i % multiplo_3 == 0 && i % multiplo_5 == 0)
        {
            write(1, "fizzbuzz\n", 10);
        }
        else if (i % multiplo_3 == 0)
        {
            write(1, "fizz\n", 6);
        }
        else if (i % multiplo_5 == 0)
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

    return i;
}

int main(void)
{
    fizzbuzz(3, 5);
    return 0;
}
