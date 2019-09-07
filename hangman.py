

def hangman(word):
    wrong = 0 #keeps track of incorrect guesses
    stages = ["",
              "_________        ",
              "|                ",
              "|        |       ",
              "|        0       ",
              "|       /|\      ",
              "|       / \      ",
              "|                "
               ]
    #stages draws the hangman
    
    letters = list(word) #contains each letter in the variable word and keeps track of which letters are left to guess
    
    board = ["__"] * len(word) #keeps track of the hints
    win = False #keeps track of if the players has won the game
    
    print("Welcome to Hangman")