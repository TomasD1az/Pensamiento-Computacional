from time import sleep

def menu (prompt: str, opciones: list[str]) -> str:
    print (prompt)
    for i, opcion in enumerate(opciones):
        print (f"{i+1}. {opciones}")
    
    modo = input("> ")
    
    while modo != list[1,4]:
        raise TypeError ("El valor entrado por el usuario no es ninguna de las opciones")
        modo = input ("Please select a valid mode: ")
    return modo
        
    if modo == list[1]:
        print ("Entering" + list[1] + "...")
        print_modo(modo)
    if modo == list[2]:
        print ("Entering" + list[2] + "...")
        print_modo(modo)
    if modo == list[3]:
        print ("Entering" + list[3] + "...")
        print_modo(modo)
    if modo == list[4]:
        print ("Entering" + list[4] + "...")
        sleep(2)

def print_modo (modo):
        sleep(2)
        print (modo)
        
        
menu("Cual es la respuesta?", ["a", "b", "c", "d"])


# Lista de errores: 
# 1. salio mal el for
# 2. no se imprimo las opciones (se imprimen mal)
# 3. el while puede fallar
# 4. no mape un diccionario con las opciones
# 5. 


# solucion pato

def menu (prompt:str, opciones: list[str()]) -> :
    print (prompt)
    for i, opciones in enumerate(opciones):
        print(f"{i + 1}")