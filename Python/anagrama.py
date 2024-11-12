import argparse

def is_anagram(str1: str, str2: str) -> bool:
    if not (str1.isalpha() and str2.isalpha()):
        return (False)
    
    elif (len(str1) != len(str2)):
        return (False)
        
    freq_str1: dict = {}
    freq_str2: dict = {}
        
    i: int = 0
    while (i < len(str1)):
        freq_str1[str1[i]] = freq_str1.get(str1[i], 0) + 1
        freq_str2[str2[i]] = freq_str2.get(str2[i], 0) + 1
        i += 1
    return  (freq_str1 == freq_str2)

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('str1', type=str)
    parser.add_argument('str2', type=str)
    args = parser.parse_args()

    str1 = args.str1
    str2 = args.str2
    
    if (isinstance(str1, (int, float)) and isinstance(str2, (int, float))):
        return(1)
    elif (isinstance(str1, str) and isinstance(str2, str)):
        if (is_anagram(str1, str2)):
            print(f"'{str1}' y '{str2}' son anagramas.")
        else:
            print(f"'{str1}' y '{str2}' NO son anagramas.")
    return(0)

if __name__ == "__main__":
    main()