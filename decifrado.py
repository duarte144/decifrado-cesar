import  string

def cifrar_letra(letra: str, clave: int) -> str:
    ABC: str = string.ascii_uppercase
    idx_letra: int= ABC.index(letra)
    return ABC[idx_letra + clave  %26]
    

def main():
    print(cifrar_letra("S",3))
    print(cifrar_letra("I",3))
    print(cifrar_letra("T",3))
    print(cifrar_letra("E",3))
    print(cifrar_letra("M",3))
    print(cifrar_letra("A",3))
    
    
    
if__name__ ="__main__"
main()







