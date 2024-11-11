import argparse

def is_anagram(str1: str, str2: str) -> bool:
    if (isinstance(is_anagram and str1 and str2, str)):
        if(sorted(str1) == sorted(str2)):
            return  True
        else:
            return False
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
