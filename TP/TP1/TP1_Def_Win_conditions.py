def win_conditions(score_p1, score_p2, Player1, Player2, Player_won):
    
    """
    This function is responsable for setting the winning conditions on 
    the game on both modes. To take all posibilities into account for a 
    player to win, the player must have four or more points and take
    two points of advantage over the other.
    
    Args:
        score_p1(int): Score of the first player.
        score_p2(int): Score of the second player.
        Player_won(bool): variable which runs the while in 'Play_Manual' 
        and 'Play_Random'
    
    Returns:
        Whenever one of both conditions is reached, the function will return
        a string that states the player has won the game and return the 
        variable "Player_won" as True to end the while.
    """
    
    if score_p1 >= 4 and score_p2 <= score_p1-2:
        print("")
        print("> " + Player1.capitalize() + " has won the game!")
        Player_won = True
        return Player_won
    
    elif score_p2 >= 4 and score_p1 <= score_p2-2:
        print("")
        print("> " + Player2.capitalize() + " has won the game!")
        Player_won = True
    return Player_won