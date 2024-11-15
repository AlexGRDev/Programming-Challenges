def fibonacci(a: int, b: int) -> int:
    if not (isinstance(a, int) and isinstance(b, int)):
        return (-1)

    counter = 0
    while counter <= 50:
        print(a)
        a, b = b, a + b
        counter += 1
    return (a)

def main() -> int:
    print(fibonacci(0, 1))
    return (0)

if __name__ == "__main__":
    main()