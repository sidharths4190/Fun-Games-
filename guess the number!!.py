# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


import random
import simplegui

secret_number = -1
num_range = 100
# helper function to start and restart the game
def new_game():
    global secret_number
    secret_number = random.randrange(0, num_range)
    
def range100():
    global num_range
    num_range = 100
    new_game()
                                    
                                  
def range1000():
    global num_range
    num_range = 1000
    new_game()
    
    
def input_guess(guess):
    global secret_number
    guess_number = int(guess)
    
    if guess_number < secret_number :
        print "guess is less than the number "
        return 
    
    elif guess_number > secret_number :
        print "guess is greater than the secret number "
        return 

    elif guess_number == secret_number :
        print "correct guess"
        new_game()                          
                                    

    
# create frame
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_button("0-100",range100,100)                                    
frame.add_button("0-1000",range1000,100) 
frame.add_input("Enter your guess",input_guess, 200)                                     

# register event handlers for control elements and start frame


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
