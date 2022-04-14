# def twice_as_old (dad_age, son_age):
#     return abs(dad_age - son_age * 2)

# print (twice_as_old(120, 10))


# def area_or_permieter(h: int, w: int):
#     if h == w:
#         return (h * w)
#     else:
#         return (2 * h + 2 * w)
    
# print (area_or_permieter(4, 5))



def dot_calculator (texto):

    contador_pri = 0
    contador_seg = 0
    op = None

    for character in text:
        
        if character == '.' and op is None:
            contador_pri += 1
        
        if character != '.' and character != ' ': 
            op = character
        
        if character == '.'  and op is not None:
            contador_seg += 1
        
        if op == '+':
            (contador_pri + contador_seg) * '.'
        elif op == '-':
            (contador_pri - contador_seg) * '.'
        elif op == '*':
            (contador_pri * contador_seg) * '.'
        elif op == '/':
            (contador_pri // contador_seg) * '.'
                
print (len (character))