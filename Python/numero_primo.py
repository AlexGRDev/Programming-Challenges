import argparse

def is_primo(n: int) -> bool:
    if n <= 1:
        return False
    
    if(isinstance(n, int)):
        i: int

        i = n
        while (i * i <= n):
            if (n % i == 0):
                return False
            i += 1
        return True
    else:
        return ""

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=int)
    args = parser.parse_args()
    
    n = args.n

    if is_primo(n):
        print(f"'{n}' es primo")
    else:
        print(f"'{n}' NO es primo.")
    
    return 0

if __name__ == "__main__":
    main()