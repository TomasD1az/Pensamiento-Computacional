month = int(input ("Que numero de mes quisieras elegir?: "))

if 1 <= month <= 3:
    print ("This month is part of the 1st quarter")
elif 4 <= month <= 6:
    print ("This month is part of the 2nd quarter")
elif 7 <= month <= 9:
    print ("This month is part of the 3rd quarter")
elif 10 <= month <= 12:
    print ("This month is part of the 4th quarter")