import argparse

CUADRADO: str = "CUADRADO"
RECTANGULO: str = "RECTANGULO"
TRIANGULO: str = "TRIANGULO"

def area_poligono(figure: str, a: float, b: float) -> float:
    if not(figure in [CUADRADO, RECTANGULO, TRIANGULO]):
        return (1)
    
    elif not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return (1)
    
    elif (figure == TRIANGULO):
        return (a * b) / 2
    elif (figure == RECTANGULO):
        return a * b
    elif (figure == CUADRADO):
        return a * a
    return (0)

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('figure', type=str)
    parser.add_argument('a', type=float)
    parser.add_argument('b', type=float)
    args = parser.parse_args()
    
    area = area_poligono(args.figure.upper(), args.a, args.b)
   
    if not (isinstance(args.figure.upper(), str) and isinstance(args.a, float) and isinstance(args.b, float)):
        return(1)
    elif (area == 1):
        print(f'Error en los parámetros proporcionados.')
        return(1)
    elif (area != 0): 
        print(f'La área de {args.figure} es {round(area, 2)}')
    else:
        print(f'Error al calcular el área.')
    return(0)

if __name__ == "__main__":
    main()