def ganancias_netas(volumen: float, precio_inicial: float, precio_final: float) -> float:
    a = precio_final * volumen
    b = precio_inicial * volumen
    c = a - b
    return ("Si vendo todos mis libros mi ganancia neta es de: " f"{c:.2f} $GRO")
    
print (ganancias_netas(12095.2, 0.86, 1.28))

def Cuanto_vender(volumen: float, precio_inicial: float, precio_final: float, libro_precio: float):
    deuda = libro_precio + precio_inicial * volumen
    cuanto_vender = deuda / precio_final
    return ("Tengo que vender " f"{cuanto_vender:.0f}" " items para poder pagar el libro y devolver la plataa prestada")

print (Cuanto_vender(12095.2, 0.86, 1.28, 2831.97))