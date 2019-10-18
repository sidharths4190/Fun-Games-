

import simplegui
import random

# Insert your solution for RPSLS here


def name_to_number(name) :
   
    if name == "rock" :
        return 0
    
    elif name == "spock" :
        return 1
    elif name == "paper" :
        return 2
    elif name == "lizard" :
        return 3
    elif name == "scissors" :
        return 4
    


def number_to_name(number):
    if number == 0 :
        return "rock"
    elif number == 1 :
        return "spock"
    elif number == 2 :
        return "paper"
    elif number == 3 :
        return "lizard"
    elif number == 4 :
        return "scissors"
    

def rpsls(player_choice): 
    a = name_to_number(player_choice)
    b = random.randrange(0,5)
    
    
    if a-b == 1 or a-b == -3 or a-b == 2 or a-b == 4:
        print "computer chooses" + " " + number_to_name(b)
        print "user chooses " + player_choice  
        print "player wins"
        print " "
   
        
        
      
          
    elif a-b == 0 :
        print "computer chose" + " " + number_to_name(b)
        print "user chose " + player_choice 
        print "tie match"
        print " "
       
    else :
        print "computer chose" + " " + number_to_name(b)
        print "user chose " + player_choice 
        print "computer wins"
        print " "
     
     
    
# handler for input field
def Rock():
    
    rpsls("rock")
    
def Paper():
    rpsls("paper")
    
def Scissors():
    rpsls("scissors")
    
def Lizard():
    rpsls("lizard")
    
def Spock():
    rpsls("spock")
    

    
   
    

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_button("ROCK",Rock,100)
frame.add_button("PAPER",Paper,100)
frame.add_button("SCISSORS",Scissors,100)
frame.add_button("LIZARD",Lizard,100)
frame.add_button("SPOCK",Spock,100)





# Start the frame animation
frame.start()
