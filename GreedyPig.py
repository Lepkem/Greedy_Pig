#jordanguerrero 
# 
# Definition of program 
# Imports 
# Globals 
#   - Capitals are used for constant values
# Classes
# Methods / functions
# Main 

import random

#constant value of players that can participate
MIN_PLAYERS = 2
MAX_PLAYERS = 6

# strategy 1, 2 or 3. strategy 
# basic is 0 and default, advanced is 1 
DEFAULT_GAME_TYPE = 0

#using gametype input as an index for the value of winning points
WINNING_POINTS = [50,100]

#using gametype input as an index for game type in interpellated message
GAME_TYPELIST = ["beginners", "advanced"]

#This is a list of instances of the class Player
list_of_players = []

#this is a default variable for the number of players to make it flexible
num_players = MIN_PLAYERS 

#this variable makes the game type changable and the default a default
game_type = DEFAULT_GAME_TYPE

#
class Player:
    def __init__(self, PlayerName):
        self.name = PlayerName
        self.score = 0
    # Class functions to help out
    def Save_score(self, score):
        self.score += score
    def Show_Score(self):
        print(f"{self.name}'s current score is:{self.score}")

# class Relationship:
#     # init -- happens only once when u create the class 
#     def __init__(self):
#         print("we met")
#     def MakeLove():
#         print("making love)")
#     def BreakUp():
#         print("breakingu")

# this function contains a die with 6 surfaces
def throwdie():
    throwvalue = (random.randint(1,6))
    return throwvalue

# this function is responsible for every turn of the selected player
def playerturn(active_player:Player):
    turn_score = 0
    
    print()
    print('---------------------------------------------------------')
    print(f"Hello {active_player.name} your safe die will be rolled")
    print('---------------------------------------------------------')
    print("")
    #throwing '1' will grant you no points, even in the safe throw
    turn_score = throwdie()
    print(f'You just rolled {turn_score}')
    print('')
    if turn_score == 1:
        turn_score = 0

    choice = '.'
    # this part of the code does the logical and visual part in the turn
    while choice != "p":        
        print("press any key to roll again and p for pass (your current score will be saved)")
        choice = input('>>')
        if choice == 'p':
        #this part of the code saves points
            active_player.Save_score(turn_score)
            if endgame() == True:
                YouWon()
                return
        else:
            newScore = throwdie()
            print(f'You just scored {newScore} points!')
            print("")
            if newScore == 1:
                print(r'¯\_(⊙︿⊙)_/¯  ¯\_(⊙︿⊙)_/¯  ¯\_(⊙︿⊙)_/¯  ¯\_(⊙︿⊙)_/¯  ¯\_(⊙︿⊙)_/¯  ¯\_(⊙︿⊙)_/¯')
                print("Your turn points are lost - next player will now play :P ")
                print("")
                active_player.Show_Score()
                print("")
                return
            else:
                turn_score += newScore
                print(f'Your unsafe score is now {turn_score}. Want to go again~~~?')
                print("")


# tries to convert input to int or returns none
def safe_cast_int(val, default=None):
    try:
        return int(val)
    except (ValueError, TypeError):
        return default

#this function asks for input and if none given, default is used for the game type
def getgametype():
    print("For the beginner game, input 0 (default) ; for the advanced game, input 1") 
    user_input = safe_cast_int(input("> "))
    # the default value of the game type is used 
    if user_input == None:
        return
    # this checks if the user input is valid, if not, a loop is implemented
    if user_input != 1 and user_input != 0:
        print('error, please provide correct input')
        getgametype()
    else:
        global game_type 
        game_type = user_input

#this function asks for input and if none given, default is used for the amount of players
def getplayeramount():
    print(f"Choose an amount of players with a minimum of {MIN_PLAYERS} (default) and a maximum of {MAX_PLAYERS}")
    user_input = safe_cast_int(input("> "))
    # the default value of the player amount is used 
    if user_input == None:
        return
    # this checks if the user input is valid, if not, a loop is implemented
    if user_input > MAX_PLAYERS or user_input < MIN_PLAYERS:
        print('error, please provide correct input')
        getplayeramount()
    else:
        global num_players 
        num_players = user_input  

#this will ask the user to write their names, print a message and append the list of players
def getplayername(playernumber):
    print(f"Hello player {playernumber}, please write your name.")
    # new instance of the player class. The name attribute comes from the input
    newplayer = Player(input(">"))
    #
    print(f"Player {playernumber}, your name is now {newplayer.name}.")
    #global is used to modify the list of players within the function scope
    global list_of_players
    list_of_players.append(newplayer)

#It returns boolean value wether or not someone complies with the values 
def endgame():
    #https://stackoverflow.com/questions/7125467/find-object-in-list-that-has-attribute-equal-to-some-value-that-meets-any-condi
    #next((x for x in list_of_players if x.score >= WINNING_POINTS[game_type]), None)

    return any(x for x in list_of_players if x.score >= WINNING_POINTS[game_type] )



#http://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=Greedy%20Pig
def logo():
    print("")
    print("")
    print(" ██████╗ ██████╗ ███████╗███████╗██████╗ ██╗   ██╗    ██████╗ ██╗ ██████╗ ")
    print("██╔════╝ ██╔══██╗██╔════╝██╔════╝██╔══██╗╚██╗ ██╔╝    ██╔══██╗██║██╔════╝ ")
    print("██║  ███╗██████╔╝█████╗  █████╗  ██║  ██║ ╚████╔╝     ██████╔╝██║██║  ███╗")
    print("██║   ██║██╔══██╗██╔══╝  ██╔══╝  ██║  ██║  ╚██╔╝      ██╔═══╝ ██║██║   ██║")
    print("╚██████╔╝██║  ██║███████╗███████╗██████╔╝   ██║       ██║     ██║╚██████╔╝")
    print(" ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚═════╝    ╚═╝       ╚═╝     ╚═╝ ╚═════╝ ")
    print("")
    print("By Jordan Guerrero, Jasper Jumulet and Gerben Put")
    print("")

def YouWon():
    print("██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗ ██████╗ ███╗   ██╗██╗")
    print("╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██╔═══██╗████╗  ██║██║")
    print(" ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║   ██║██╔██╗ ██║██║")
    print("  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║   ██║██║╚██╗██║╚═╝")
    print("   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝╚██████╔╝██║ ╚████║██")

def DisplayAllPlayersScore():
    for player in list_of_players:
        # function that takes one player from players list through the index.
        player.Show_Score()

        
def main():

    logo()
    getgametype()
    getplayeramount()



    print(f"The game type is {GAME_TYPELIST[game_type]} and the current number of players is {num_players}")
    
    # this will ask the user to write their names for the number of players
    for i in range(num_players):
        getplayername(i+1)

    
    print("starting the game ;)")
    print('')

    while endgame() == False:
        for active_player in list_of_players:
            # function that takes one player from players list through the index.
            if endgame() == False:
                DisplayAllPlayersScore()
                playerturn(active_player)


if __name__ == '__main__':
    main()






