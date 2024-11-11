def fizzbuzz(multiplo_3: int, multiplo_5: int) -> int:
    if (isinstance(multiplo_3 and multiplo_5, int)):
        i: int 
        i = 1
        while i <= 100:
            if i % multiplo_3 == 0 and i % multiplo_5 == 0:
                print("fizzbuzz")
            elif i % multiplo_3 == 0:
                print("fizz")
            elif i % multiplo_5 == 0:
                print("buzz")
            else:
                print(i)
            i += 1
    else:
        print("Los parámetros deben ser enteros.")

def main() -> int:
    fizzbuzz(3, 5)
    return 0

if __name__ == "__main__":
    main()
