from time import perf_counter, sleep

def usd_to_cny(dollars) -> float:
    return dollars * 6.75

def usd_to_ars(dollars) -> float:
    return dollars * 200
    
def usd_to_chf(dollars) -> float:
    return dollars * 0.94


dollars =  float(input ("Inrgese USD: "))
cny = usd_to_cny(dollars)
ars = usd_to_ars(dollars)
chf = usd_to_chf(dollars)

response = input ("Ingrese monedas (acronimos):")

if response == "ARS":
        sleep (3)
        print("")
        print (f"{ars:.2f} ARS")
elif response == "CNY":
        sleep (3)
        print("")
        print (f"{cny:.2f} CNY")
elif response == "CHF":
    sleep (3)
    print("")
    print (f"{chf:.2f} CHF")
else :
    sleep (3)
    print("")
    print ("Error 404, destruyendo la computadora en...")


# if __name__ == '__main__':
#     main()    
#  el main se usa para 