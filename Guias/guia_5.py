"""
Guia de ejercicios n°5 - Secuencia
"""

"""Cadenas

1. ★☆☆ Corrija este código para que imprima la longitud de un string:
print(length("Esto es un texto")) (Hecho)"""

# print (len("Esto es un texto"))

"""
2. ★☆☆ Escribir una función que cuente la cantidad de letras A que se encuentran en una palabra. Complete
el siguiente código:
    def count_A(the_string: str) -> int:
     # complete me
"""
# def count_A(the_string: str) -> int:
#     lista = list [the_string]
#     print (lista()) 
    
# count_A("hola")


# # slucion alvaro:
    
# def count_A(word: str) -> int:
#     count = 0
#     for letter in word:
#         if letter() == 'a'
#     return 

"""
3. ★☆☆ Escriba una función count(s, character) que cuente cuántas veces aparece el carácter
character en la cadena s. Complete el siguiente código:
    def count(s: str, character: str) -> int:
     # complete me
"""


"""
5. ★☆☆ Una dirección IP (IPv4) es una cuarteto de números entre 0 y 255 (inclusive) separados por ".", y es la
dirección única de cada dispositivo conectado a una red, como la dirección postal de una casa en una
ciudad. Escribir una función que dada una dirección IPv4 válida, devuelva una versión modificada de esa
dirección IP, a esta versión modificada la llamaremos "IP con colmillos". Una dirección IP con colmillos
reemplaza cada punto "." de la dirección IP original con "[.]" (Hecho).
"""
# def poner_corchete (IP: str) -> list[str]:
#     for i in IP:
#         if i == ".":
#             i = "[.]"
#         print(i)

# poner_corchete("225.100.50.0")
     
# # solucion_alvaro:
# def good_way(ip):
#     ip = ip.replace('.', '[.]')
#     return ip

# def not_so_good(ip):
#     result = ""
#     for letter in ip:
#         if letter == '.':
#             result += '[.]'
#         else:
#             result == letter
#     return result

# def main ():
#     ip = "225.100.50.0"
#     # ip = good_way(ip)
#     ip = not_so_good(ip)
#     print (ip)

# if __name__ == '__main__':
#     main()

"""
6. ★★☆ Algunos tipos de piedras son joyas, y todas las joyas son piedras. Vamos a representar cada piedra
con un carácter, por ejemplo la "a", por lo que una cadena de caracteres representa un conjunto de piedras,
por ejemplo "aaAb" es un conjunto de piedras. Dada una cadena de caracteres que representa los tipos de
piedras que son joyas, y otra cadena de caracteres que representa las piedras que tienes, quieres saber
cuántas joyas tienes, es decir, cuántas de las piedras que tienes son también joyas. (Hecho)
"""

# def contar_joyas(piedras: str, joyas: list[str]) -> int:
#     contador = 0
#     for i in joyas:
#         for j in piedras:
#             if j == i:
#                 contador += 1
#     print (contador) 

# def main ():
#     joyas = "a"
#     piedras = "AAaaBBbb"
#     joyas = contar_joyas(piedras, joyas)

# if __name__ == '__main__':
#     main()

"""
10. 
"""
# print (ord("a"))
# print(chr(97))

def codigo_cesar (codigo_encrip: str, codigo_desen: str) -> str:
    codigo_desen = list(codigo_desen)
    lista_encriptada_ascii = {}
    
    for i in codigo_desen:
        lista_encriptada_ascii.append(ord(i)+3)
        print (lista_encriptada_ascii)
    pass
        
codigo_cesar("me pica el culo", "tyuop")