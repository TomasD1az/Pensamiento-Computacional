from TP2_submenu import menu_play

def menu () -> int:
    fin=0
    while not fin:
        print("\t\t ** Welcome to the Hangmans Game **")
        print ("""
                Please select one option:
                
                1. Play
                2. See words list
                3. Rules
                4. Quit
                """)
    
        option = int(input("> "))
    
        if option == 1:
            fin = menu_play()
        elif option == 2:
            ## see_words()
            pass
        elif option == 3:
            ## see_rules()
            pass
        elif option == 4:
            pass
        
































    # try:
    #     option = int(input ("> "))
    # except SyntaxError:
    #     print('value entered is not an integer')
    # if 1 <= option <= 4:
    #     raise ValueError('Invalid expression, enter a 1 to 4 value')
    # return option