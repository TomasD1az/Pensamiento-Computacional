def sq_list(lista: list) -> list:
    lista_2 = lista
    for i in range (len(lista_2)):
        lista_2[i] = lista[i] ** 2
    return lista_2

print (sq_list(1, 4, 5))

def generar_lista (n: int) -> list:
    return list(range(n))


def minimax (secuencia):
    return min (secuencia), max (secuencia)


def desemp ():
    meses = (("enero", 31), ("febrero", 28), ("diciembre", 31))
    for mes, dias in meses:
        print (mes, "Tiene", dias, "dias.")
        
        
def desemp_2 ():
    preg = (("Cuantos estudiantes hay en IA?", (50, 100, 150, 200)),
             ("Cuantos estudiantes hay en el UBA?", (1000, 2000, 3000)))
    for pregunta, opciones in preg:
        print (pregunta)
        # for i in range (len(opciones)):
        #     print (f"{i + 1}. {opciones[i]}")
        for i, opcion in enumerate(opciones, 1):
            print (f"{i}. {opcion}")
            
# Tabla ASki -> tabla que muestra el valor de las letras
# se usa el comando 'ord'(x) para ver cual es el valor de esa letra