name = input ("Bienvenido, ingrese su nombre:")
millas = input (name + ", ingrese sus millas:")

def convert_millas_km (km) -> float:
    km = millas * 1.60
    return km

print ("Señor/a" + name + ", usted tiene" + km + "kilometros")