import argparse

def is_anagram(str1: str, str2: str) -> bool:
    if not (isinstance(str1, str) and isinstance(str2, str)):
        print("Error: Los parámetros deben ser str.")
        return False
    
    if (len(str1) != len(str2)):
        return False
    
    freq_str1: dict
    freq_str2: dict
    
    freq_str1 = {}
    freq_str2 = {}
    if not(isinstance(freq_str1, dict) and isinstance(freq_str2, dict)):
        return False
        
    i: int = 0
    while (i < len(str1)):
        freq_str1[str1[i]] = freq_str1.get(str1[i], 0) + 1
        freq_str2[str2[i]] = freq_str2.get(str2[i], 0) + 1
        i += 1
    return  (freq_str1 == freq_str2)

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('str1', type=str)
    parser.add_argument('str2', type=str)
    args = parser.parse_args()

    if not (args.str1.isalpha() and args.str2.isalpha()):
        print("Por favor, introduce solo letras en ambos argumentos.")

    str1 = args.str1
    str2 = args.str2

    if (is_anagram(str1, str2)):
        print(f"'{str1}' y '{str2}' son anagramas.")
    else:
        print(f"'{str1}' y '{str2}' NO son anagramas.")

if __name__ == "__main__":
    main()
