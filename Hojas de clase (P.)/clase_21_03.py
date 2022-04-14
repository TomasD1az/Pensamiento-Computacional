def contar_letras (cadena: str, letra: str) -> int:
    """Cuenta la cantidad de letras especificas en una cadena de argumentos
    
    Arguemtnos
    cadena (str) -- cadena sobre la que contar
    letra (str) -- letra que quiero contar
    """
    
    cuenta = 0
    for caracter in cadena:
        if caracter == letra:
            cuenta += 1
            
    return cuenta

def contar_elementos(lista: list, elemento) -> int:
    cuenta = 0
    for e in lista:
        if e == elemento:
            cuenta += 1
            
    return cuenta

# Mutabilidad

            