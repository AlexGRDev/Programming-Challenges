import argparse

CUADRADO: str = "CUADRADO"
RECTANGULO: str = "RECTANGULO"
TRIANGULO: str = "TRIANGULO"

def area_poligono(figure: str, a: float, b: float) -> float:
    if (figure not in [CUADRADO, RECTANGULO, TRIANGULO]):
        return (1)
    
    if not (isinstance(a, (float, int)) or (b is not None and not isinstance(b, (float, int)))):
        return print("Los valores de a y b deben ser números")
    
    if (figure == TRIANGULO):
        return (a * b) / 2
    elif (figure == RECTANGULO):
        return a * b
    elif (figure == CUADRADO):
        return a * a
    else:
        return (1)

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('figure', type=str)
    parser.add_argument('a', type=float)
    parser.add_argument('b', type=float)
    args = parser.parse_args()

    try:
        print("".join({args.figure.upper()}), area_poligono(args.figure.upper(), args.a, args.b))
    except ValueError as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()