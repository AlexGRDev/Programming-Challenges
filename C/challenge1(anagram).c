    #include <stdbool.h>
    #include <stdio.h>
    #include <string.h>

    bool anagram(char *str1, char *str2)
    {
        int counter[8] = {0};
        int i;
        int j;

        if (strlen(str1) != strlen(str2))
        {
            return false;
        }

        i = 0;
        while (str1[i] != '\0')
        {
            counter[(unsigned char)str1[i]]++;
            
            j = 0;
            while (j < 8)
            {
                counter[(unsigned char)str2[j]]++;
                if (counter[j] != 0)
                {
                    return false;
                }
                j++;
            }
            i++;
        }

        return true;
    }

    int main()
    {
        char *str1 = "roma";
        char *str2 = "amor";
        bool result;

        result = anagram(str1, str2);
        if (result)
        {
            printf(" %s and %s are anagrams\n", str1, str2);
        }
        else
        {
            printf("%s and %s are not anagrams\n", str1, str2);
        }

        return 0;
    }
