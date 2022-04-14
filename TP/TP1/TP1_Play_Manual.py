from TP1_Def_Print_Score import print_score
from TP1_Def_Player_Inputs import player_inputs
from TP1_Def_Select_valid_mode import select_valid_mode
from TP1_Def_Select_valid_player import select_valid_player
from TP1_Def_Win_conditions import win_conditions

def Manual_mode():

    """
    This is the simulation mode function. It is responsable for counting the 
    points in a manual way by making the user insert who won the point and
    assign a value to each player ("Player1" to player1 and "Player2" 
    to player2). And by calling some previously-defined functions, it 
    transforms this into an output that prints a scoreboard until the while
    that contains all of this functions stops (someone has won)
    
    Args:
        No argumetns used on this function
            
    Returns:
        This function will return the scoreboard, which includes the 
        points of each player. This process will be repeated for a game.
    """

    score_p1 = 0
    score_p2 = 0 
    Player_won = False

    Player1, Player2 = player_inputs()
    Player2 = select_valid_player(Player1, Player2)
    
    while Player_won == False:
        
        point_winner = input ("Who won this point?: ")
        point_winner = select_valid_mode (point_winner, Player1, Player2)
        score_p1, score_p2 = print_score(Player1, Player2, score_p1, score_p2, point_winner, None)        
        Player_won = win_conditions(score_p1, score_p2, Player1, Player2, Player_won)