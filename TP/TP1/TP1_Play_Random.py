import random
from time import sleep
from TP1_Def_Print_Score import print_score
from TP1_Def_Player_Inputs import player_inputs
from TP1_Def_Select_valid_mode import select_valid_mode
from TP1_Def_Select_valid_player import select_valid_player
from TP1_Def_Win_conditions import win_conditions


def Simulation_mode ():
    
    """
    This is the simulation mode function. It is responsable for counting the 
    points in a random way by selecting (randomly) who won the point using a
    'randrange' and selecting a value to each player (0 to player1 and 
    1 to player2). And by calling some previously-defined functions, it 
    transforms this into an output that prints a scoreboard until the while
    that contains all of this functions stops (someone has won)
    
    Args:
        No argumetns used on this function
            
    Returns:
        This function will return the scoreboard, which includes the 
        points of each player. This process will be repeated for a game.
    """
    
    Player_won = False
    score_p1 = 0
    score_p2 = 0
    Player1, Player2 = player_inputs()
    Player2 = select_valid_player(Player1, Player2)
    
    mode = input("would you like to see the complete simultation or just the result?: ")
    mode = mode.lower()
    mode = select_valid_mode(mode, "complete", "just result")
    
    while Player_won == False:        
        Random_number = random.randrange(2)
        Player3 = 2
    
        if mode == "complete":
                score_p1, score_p2 = print_score(Player1, Player2, score_p1, score_p2, Player3, Random_number)
                sleep(2)
                Player_won = win_conditions(score_p1, score_p2, Player1, Player2, Player_won)
                
        elif mode == "just result":
                score_p1, score_p2 = print_score(Player1, Player2, score_p1, score_p2, Player3, Random_number)
                Player_won = win_conditions(score_p1, score_p2, Player1, Player2, Player_won)