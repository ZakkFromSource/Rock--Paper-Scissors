import random

valid = [1, 2, 3]
beats = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
moves = {1: 'rock', 2: 'paper', 3: 'scissors'}
p1 = None
com = None


def validentry(p1) :
    if p1 in valid :
        print('Good Luck!')
        comp_rps()
        return True
    else:
        print("Invalid Input, try again.\n ---")
        

def p1_input() :
    while True:
        try:
            p1 = int(input("""
               Rock, Paper, Scissors!
      
        Enter '1' to select ROCK
        Enter '2' to select PAPER
        Enter '3' to select SCISSORS
        > """))
            if validentry(p1):
                return p1
                
        except:
            print("Please enter a valid number (1, 2, or 3).\n---")

def comp_rps():
    return random.randrange(1,4)

def win_chk ():
    p1_hand = moves[p1]
    com_hand = moves[com]
    print('Player:', p1_hand)
    print('Computer:', com_hand)
    
    if beats[p1_hand] == com_hand :
        print("You win! Congratulations!")
    elif beats[com_hand] == p1_hand :
        print("You lose! Computer wins!")
    else:
        print("Draw!")    

p1 = p1_input()
com = comp_rps()
#print(p1, com)
win_chk()



