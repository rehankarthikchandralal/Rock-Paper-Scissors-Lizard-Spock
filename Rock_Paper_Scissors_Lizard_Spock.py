import random

class RPSLS():
    """
    Rock-paper-scissors-lizard-Spock is a more complex version of the classic hand game 
    where players choose one of five options: rock, paper, scissors, lizard, or Spock.
    Instead of each option having only one weakness and one strength,
    each option beats two other options and loses to two other options.
    """
    

def name_to_number(name):
    """
    Given string name, returns integer 0, 1, 2, 3, or 4 
    The key idea of this function is to equate the strings
    "rock", "paper", "scissors", "lizard", "Spock" to numbers
    as follows:

    0 - rock
    1 - Spock
    2 - paper
    3 - lizard
    4 - scissors
    """
    if(name == "rock"):
        return 0
    elif(name =="Spock"):
        return 1
    elif(name == "paper"):
        return 2
    elif(name == "lizard"):
        return 3
    elif(name == "scissors"):
        return 4
    else:
        print("ERROR:The input is INVALID")  
        return None


def number_to_name(number):
    """
    Given integer number (0, 1, 2, 3, or 4) is converted to 
    corresponding name 
    """
    if(number == 0):
        return "rock"
    elif(number == 1):
        return "Spock"
    elif(number == 2):
        return "paper"
    elif(number == 3):
        return "lizard"
    elif(number == 4):
        return "scissors"
    else:
        print("ERROR:The input is INVALID")  
        return None

def rpsls(player_choice):
    """
    Given string player_choice, play a game of RPSLS 
    and print results to console
    """
    
    print() 
    
    print("The player's choice is",player_choice)


    player_number=name_to_number(player_choice)
    print("The player's number is",player_number)


    comp_number=random.randrange(5)
    print("The computer's number is",comp_number)

    # convert comp_number to comp_choice using the function number_to_name()
    
    # print out message for computer's choice

    # compute difference of player_number and comp_number modulo five

    # use if/elif/else to determine winner and print winner message
    
    
     

# test your code
rpsls("rock")
# rpsls("Spock")
# rpsls("paper")
# rpsls("lizard")
# rpsls("scissors")

# always remember to check your completed program against the grading rubric

#print(name_to_number("spock"))
#print(number_to_name(5))