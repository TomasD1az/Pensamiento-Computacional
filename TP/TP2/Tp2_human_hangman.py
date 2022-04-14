def human_hangman ():
    #word = eleccion_palabra()
    word = list(input("ingrese la palabra: "))
    list_guiones=[]
    
    for i in range(len(word)):
        list_guiones.append('_')
    
    letra = input('Ingrese la letra: ')
    
    while list_guiones != word:
        for j, character in enumerate(word):
            if character == letra:
                list_guiones[j]=letra
            
        print(" ".join(list_guiones))

    print ("Game has ended")

human_hangman()
    
    