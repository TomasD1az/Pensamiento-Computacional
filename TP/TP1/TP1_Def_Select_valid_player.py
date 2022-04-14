def select_valid_player (Player1, Player2):
    
    """
    Similar to 'select_valid_score', this function denies the possibility of
    having the same input on both player's name. Until the new input for 
    PLayer 2 is different from Player1, you cannot continue.
    
    Args:
        Player1(str): Name of the first player.
        Player2(str): Name of the second player.
    
    Returns:
        When the new value of Player2 is different from Player1, that new 
        value will be assigned to Player 2 in the executable file.
    """
    
    while Player1 == Player2:
        print("")
        print ("Not valid player (#ERROR 54369)")
        Player2 = input ("Select a valid player: ")
        print ("Please wait a second...")
    return Player2