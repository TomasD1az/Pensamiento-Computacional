def name ():
    mazo = list(range (1,41))
    return mazo
 
def card_missin ():
    for i in range(1, 41, 1):
        if i >= 1 and i <= 10:
            print (str(i) + " de oro")
        if i > 10 and i <= 20:
            print (str(i-10) + " de copa")
        if i > 20 and i <= 30:
            print (str(i-20) + " de basto")
        if i > 30 and i <= 40:
            print (str(i-30) + " de espada")

print(name())
# def remove_card ():
    