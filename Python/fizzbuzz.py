def fizzbuzz(multiplo_3: int, multiplo_5: int) -> int:
    if not (isinstance(multiplo_3, int) and isinstance(multiplo_5, int)):
        return (-1)
    
    numero: int 
    numero = 1
    while (numero <= 100):
        if (numero % multiplo_3 == 0 and numero % multiplo_5 == 0):
            print("fizzbuzz")
        elif (numero % multiplo_3 == 0):
            print("fizz")
        elif (numero % multiplo_5 == 0):
            print("buzz")
        else:
            print(numero)
        numero += 1
    return (0)

def main() -> None:
    fizzbuzz(3, 5)

if __name__ == "__main__":
    main()
