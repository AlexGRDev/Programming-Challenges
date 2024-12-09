/*
    * Escribe una función que reciba dos palabras (String) y retorne
    * verdadero o falso (Bool) según sean o no anagramas.
    * - Un Anagrama consiste en formar una palabra reordenando TODAS
    *   las letras de otra palabra inicial.
    * - NO hace falta comprobar que ambas palabras existan.
    * - Dos palabras exactamente iguales no son anagrama.
 */


#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool anagram(char *word1, char *word2)
{
    if (strcmp(word1, word2) == 0)
    {
        return false;
    } if (strlen(word1) != strlen(word2))
    {
        return false;
    }

    int char_counter[256];
    int i;

    i = 0;
    while (i < 256)
    {
        char_counter[i] = 0;

        if (word1[i] != '\0')
        {
            char_counter[(unsigned char)(word1[i])]++;
        } 
        
        int j;
        
        j = 0;
        while (j < i)
        {
            if (char_counter[j] != 0)
            {
                char_counter[(unsigned char)(word2[j])]++;
            } j++;
        } i++;
    } return true;
}

int main() 
{
    char word1[] = "pera";
    char word2[] = "perra";

    if (anagram(word1, word2))
    {
        printf("Las palabras son anagramas\n");
    } else
    {
        printf("Las palabras no son anagramas\n");
    } return 0;
}
