import  string   # ---> aqui importaremos String para obtener el alfabeto en mayusculas

def cifrar_letra(letra: str, clave: int) -> str: # --->  Letra en mayúscula a cifrar # ---> clave Número de posiciones a desplazar en el alfabeto
    abs: str = string.ascii_uppercase  # ---> Aqui convierte el alfabeto o las letras en mayusculas
    idx_letra: int= abs.index(letra)
    return abs[idx_letra + clave  %26]


def main():  # ---> Función principal que prueba el cifrado con las letras "C", "D" y "E" usando un desplazamiento de 5
    print(cifrar_letra("C",5))
    print(cifrar_letra("D",5))
    print(cifrar_letra("E",5)) 
 
    
  
if__name__ ="__main__"
main()