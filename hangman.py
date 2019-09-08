

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
    
    while wrong < len(stages) - 1:
        print("\n")
    
        message = "Guess a letter: " 
        character = input(message) 
    
        if character in letters:
            cind = letters \
                   .index(character)
            
            board[cind] = character
            
            letters[cind] = '$'
    
        else:
            wrong += 1
    
        print((" ".join(board)))
    
        e = wrong + 1
   
        print("\n".join(stages[0: e]))
    
        if "__" not in board:
            
            print("You win!")
            
            print(" ".join(board))
            
            win = True
            break
      
    if not win:
        print("\n"
              .join(stages[0: \
              wrong]))
        
        print("You lose! It was {}.".format(word))
                               
hangman("soccer")
                               
                               
                               
                               
                               
                               
        
          
  