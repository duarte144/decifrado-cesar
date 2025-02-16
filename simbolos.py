import string  # ---> se importa para obvtener mayusculas, minusculas y dijitos 

def cifrar_letra(letra: str, clave: int, abs: str) -> str: # --->  Letra en mayúscula a cifrar # ---> clave Número de posiciones a desplazar en el alfabeto
    if letra in abs:  # ---> Conjunto de caracteres que se usarán en el cifrado
        idx = abs.index(letra) # ---> aqui tendra en cuenta el indice en el cual va a caer la letra o posicion 
        return abs[(idx + clave) % len(abs)]  # ---> aqui obtendra el caracter y no ser lo contrario retornara 
    return letra 

def cifrar_mensaje(mensaje: str, clave: int):
    abs = string.ascii_uppercase + string.ascii_lowercase + string.digits +  "" # ---> aqui obtendra todos los caracteres necesarios para cifrar el mensaje 
    
    for letra in mensaje:
        print(cifrar_letra(letra, clave, abs), end="")  
    print()  

def main():
    mensaje_original = "¡Hola Mundo! 124"
    clave = 3
    cifrar_mensaje(mensaje_original, clave)  

if __name__ == "__main__":
    main()
