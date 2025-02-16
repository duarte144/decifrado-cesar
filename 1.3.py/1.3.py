import  string

def cifrar_letra(letra: str, clave: int) -> str:
    HOLA: str = string.ascii_uppercase
    idx_letra: int= HOLA.index(letra)
    return HOLA[idx_letra + clave  %26]


def main():
    print(cifrar_letra("H",3))
    print(cifrar_letra("O",3))
    print(cifrar_letra("L",3)) 
    print(cifrar_letra("A",3))  
    
  
if__name__ ="__main__"
main()

