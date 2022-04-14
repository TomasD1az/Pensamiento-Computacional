def select_valid_mode (mode, first_condition, second_condition):

    """
    The purpose of this function is to deny every entry possible that does 
    not fit in with the two modes possibles. Until the new input for 
    mode is equal to one of the two possible modes, you cannot continue.
    
    Args:
        mode(str): Input of which mode the user wants to play.
        first_condition(str): the first pre-established mode to play.
        second_condition(str): the second pre-established mode to play. 
            
    Returns:
        When the new value of mode is equal to any condition, that new 
        value will be assigned to mode in the executable file.
    """
    
    while mode != first_condition and mode != second_condition or first_condition == second_condition:
        print("")
        print ("Not valid mode (#ERROR 54278)")
        mode = input ("Select a valid value: ")
        mode = mode.lower ()
        print ("Please wait a second...")
    return mode