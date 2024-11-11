
import argparse

def is_anagram(str1: str, str2: str) -> bool:
    if (len(str1) != len(str2)):
        return False

    if (isinstance(str1 and str2, str)):
        i: int
        count1: str
        count2: str

        count1: str = {}
        count2: str = {}

        i = 0
        while(i < len(str1)):
            count1[str1] = count1.get(str1[i], 0) + 1
            count2[str2] = count2.get(str2[i], 0) + 1
            i += 1
        return True
    else:
        return ""

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('str1', type=str)
    parser.add_argument('str2', type=str)
    args = parser.parse_args()
    
    if not (args.str1.isalpha() and args.str2.isalpha()):
        print("Por favor, introduce solo letras en ambos argumentos.")
        return 1

    str1 = args.str1
    str2 = args.str2

    if is_anagram(str1, str2):
        print(f"'{str1}' y '{str2}' son anagramas.")
    else:
        print(f"'{str1}' y '{str2}' NO son anagramas.")
    
    return 0

if __name__ == "__main__":
    main()
