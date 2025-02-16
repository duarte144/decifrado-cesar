import  string  # ---> aqui importaremos String para obtener el alfabeto en mayusculas

def cifrar_letra(letra: str, clave: int) -> str: # ---> letra a cifrar # ---> clave va hacer el numero en el cual se posicionara 
    HOLA: str = string.ascii_uppercase # ---> aqui es donde nos transforma o nos reconoce el aflabeto en mayuscula 
    idx_letra: int= HOLA.index(letra) 
    return HOLA[idx_letra + clave  %26]


def main():  # ---> Función principal que prueba el cifrado con las letras "H", "O" "L" "A" usando un desplazamiento de 3
    print(cifrar_letra("H",3))
    print(cifrar_letra("O",3))
    print(cifrar_letra("L",3)) 
    print(cifrar_letra("A",3))  
    

if__name__ ="__main__"
main()

