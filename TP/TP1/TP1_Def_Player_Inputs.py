def player_inputs():

    """
    This function generates two inputs that will store the value of which
    will be the names of both players in the game. 
    
    Args:
        Player1(str): the value assigned to 1° players' name.
        Player2(str): the value assigned to 2° players' name. 
            
    Returns:
        This function will return both inputs value into strings that will
        be printed into the scorebord later on.
    """

    print ("")
    print ("Running the program...\nDo not turn off the computer")
    Player1 = input("Insert name of 1° player: ")
    Player2 = input ("Insert name on 2° player: ")
    return Player1, Player2