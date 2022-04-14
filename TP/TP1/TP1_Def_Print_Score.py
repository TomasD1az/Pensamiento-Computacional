def print_score (Player1, Player2, score_p1, score_p2, point_winner, Random_number):

        """
        This functions' main property is to set up a counter that keeps 
        increasing wherever the inputs of who won are inserted manually
        or randomly, this score is mapped with an already defined list 
        that gives you the correct values of a tennis counter when being 
        printed. The secondary properties are that it sets back to 40/40
        when the one who had advantage lost the point; and, it sets the
        value of the points to game if the player has won the game.
        
        Args:
            Random_number(int): generates a number between o and 1.
            point_winner(str): input where the user decides who won the point
            Player1(str): the value assigned to 1° players' name.
            Player2(str): the value assigned to 2° players' name. 
            score_p1(int): Score of the first player.
            score_p2(int): Score of the second player.
        Returns:
            This function will continously return a value from the list
            (into strings) that will be printed into the scorebord until 
            the while stops.
        """

        list_points = ["0", "15", "30", "40", "ad", 'game']    
        print ("________________________________")    
        print ("**Grand Slam Tennis Anotator **")
        print ("")    
        
        if point_winner == Player1 or Random_number == 0:
            score_p1 += 1
            print("")
            print("Who scored? First PLayer")
        elif point_winner == Player2 or Random_number == 1:
            score_p2 += 1
            print("")
            print("Who scored? Second PLayer")
            
        if score_p1 == 4 and score_p2 == 4:
            score_p1 = 3 
            score_p2 = 3
        elif score_p1 == 4 and score_p2 <= 2:
            score_p1 = 5
        elif score_p2 == 4 and score_p1 <= 2:
            score_p2 = 5
            
        print ("Score:") 
        print (f"{Player1:} {list_points[score_p1]} pts")
        print (f"{Player2:} {list_points[score_p2]} pts")
        return score_p1, score_p2