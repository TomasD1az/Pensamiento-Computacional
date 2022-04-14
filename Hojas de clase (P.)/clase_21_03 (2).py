class Contador(object):

  def __init__(self, inicial=0):
    self.numero = inicial

  def siguiente(self):
    self.numero += 1
    return self.numero

cuenta = Contador()

for i in range(5):
   print(cuenta.siguiente())

for i in range (TP1_Solucion_Inicial):
    print("Hola")