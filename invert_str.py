def inver(cadena: str) -> str:
    invert_str: str 
    i: int
    
    invert_str = ""
    i = 0 
    while(i < len(cadena)):
        invert_str = cadena[i] + invert_str
        i += 1
    return(invert_str)        



def main() -> int:
    cadena: str
    cadena = input("Enter a string: ")
    print(inver(cadena)) 


if __name__ == "__main__":
    main()