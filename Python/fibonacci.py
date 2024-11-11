def fibonacci(a: int, b: int) -> int:
    if (isinstance(a and b, int)) or a < 0 or b < 0:
        i: int
        a: int
        b: int

        i = 0
        while i < 50:
            print(a)
            a, b = b, a + b
            i += 1
        return a
    else:
        return ""

def main() -> int:
    print(fibonacci(0, 1))
    return 0

if __name__ == "__main__":
    main()
