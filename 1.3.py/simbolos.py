import string

def cifrar_letra(letra: str, clave: int, abs: str) -> str:
    if letra in abs:
        idx = abs.index(letra)
        return abs[(idx + clave) % len(abs)]
    return letra 

def cifrar_mensaje(mensaje: str, clave: int):
    abs = string.ascii_uppercase + string.ascii_lowercase + string.digits +  " "
    
    for letra in mensaje:
        print(cifrar_letra(letra, clave, abs), end="")  
    print()  

def main():
    mensaje_original = "¡Hola Mundo! 123"
    clave = 3
    cifrar_mensaje(mensaje_original, clave)  

if __name__ == "__main__":
    main()
