import  string

def cifrar_letra(letra: str, clave: int) -> str:
    abs: str = string.ascii_uppercase
    idx_letra: int= abs.index(letra)
    return abs[idx_letra + clave  %26]


def main():
    print(cifrar_letra("C",5))
    print(cifrar_letra("D",5))
    print(cifrar_letra("E",5)) 
 
    
  
if__name__ ="__main__"
main()