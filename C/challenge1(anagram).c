#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

bool anagram(char *str1, char *str2)
{
    
}

int main()
{
    char *str1;
    char *str2;
    bool result;

    str1 = "roma";
    str2 = "roma";

    result = anagram(str1, str2);
    if (result == true)
    {
        printf("%s and %s are anagrams\n", str1, str2);
    }
    else
    {
        printf("%s and %s are not anagrams\n", str1, str2);
    }
    
    return 0;
}
