from time import sleep
from TP1_Play_Manual import Manual_mode
from TP1_Play_Random import Simulation_mode
from TP1_Def_Select_valid_mode import select_valid_mode

def Play_Manual ():
    
    """
    This function is responsable for importing the manual mode and letting
    the user know that the manual mode will be debugged.
    
    Args:
        Manual_mode: Runs the function Manual_mode.
    
    Returns:
        This funtion returns the "Manual_Mode()" from the "TP1_Play_Manual"
        file.
    """
    
    print ("Entering Manual Mode")    
    sleep (2.5)
    Manual_mode()
    
    
def Play_Simulation ():
    
    """
    This function is responsable for importing the simulation mode and letting
    the user know that the simulation mode will be debugged.
    
    Args:
        Simulation_mode: Runs the function Simulation_mode.
    
    Returns:
        This funtion returns the "Simulation_mode()" from the 
        "TP1_Play_Random" file.
    """
    
    print ("Entering Simulation Mode")    
    sleep (2.5)
    Simulation_mode()
    

def main():
    
    """
    This function is the main function, where the first debugging of the
    program should be. However, this function is only capable of giving
    a welcome to the user and responding what mode the user wants to play 
    (cannot write a non-pre-defined mode). From now on, all functions will
    be imported from different files.
    
    Args:
        No argumetns used on this function.

    Returns:
        This funtion returns the "Manual_Mode()" from the "TP1_Play_Manual"
        file, or the "Simulation_mode()" from the "TP1_Play_Random" file
        depending on which mode the user decides to play.
    """
    
    print ("** Welcome to Grand Slam Tenis Annotator **")
    print ("")
    sleep (3)
    print ("PLease select your method: \n1. Manual Mode: \n2. Simulation Mode:")
    mode = input ("> ")
    mode = mode.lower()
    
    print ("Please wait a second...")
    sleep (3)
    
    mode = select_valid_mode (mode, "manual mode", "simulation mode")
    
    if mode == "manual mode":
        print ("")
        Play_Manual()
    elif mode == "simulation mode":
        print ("")
        Play_Simulation()


if __name__ == "__main__":
    main ()