from time import sleep

def menu_play():
    print("Entering Play...")
    sleep(2)
    print ("""
            Please select one option:
            
            1. Human Hangman
            2. Computer Hangman
            3. Go back
            """)
            
    option = int(input("> "))
    
    if option == 1:
        # llama a la funcion de jugar manual
        pass
    if option == 2:
        # llama a la funcion de jugar automatico
        pass
    if option == 3:
        return 0