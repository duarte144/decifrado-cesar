import  string # ---> aqui importaremos String para obtener el alfabeto en mayusculas


def cifrar_letra(letra: str, clave: int) -> str: # ---> letra a cifrar # ---> clave va hacer el numero en el cual se posicionara 
    ABC: str = string.ascii_uppercase # ---> aqui es donde nos transforma o nos reconoce el aflabeto en mayuscula 
    idx_letra: int= ABC.index(letra) 
    return ABC[idx_letra + clave  %26] # ---> mantiene un orden al pasar de posicion 
    

def main(): # ---> Función principal que prueba el cifrado con las letras "S", "I" "S" "T" "E" "M" "A" usando un desplazamiento de 3
    print(cifrar_letra("S",3))
    print(cifrar_letra("I",3))
    print(cifrar_letra("T",3))
    print(cifrar_letra("E",3))
    print(cifrar_letra("M",3))
    print(cifrar_letra("A",3))
    
    
    
if__name__ ="__main__"
main()







