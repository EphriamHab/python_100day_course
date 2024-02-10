# Guessing a number game
import random
print(""" _______           _______  _______  _______    _______  _______  _______  _______ 
(  ____ \|\     /|(  ____ \(  ____ \(  ____ \  (  ____ \(  ___  )(       )(  ____ \
| (    \/| )   ( || (    \/| (    \/| (    \/  | (    \/| (   ) || () () || (    \/
| |      | |   | || (__    | (_____ | (_____   | |      | (___) || || || || (__    
| | ____ | |   | ||  __)   (_____  )(_____  )  | | ____ |  ___  || |(_)| ||  __)   
| | \_  )| |   | || (            ) |      ) |  | | \_  )| (   ) || |   | || (      
| (___) || (___) || (____/\/\____) |/\____) |  | (___) || )   ( || )   ( || (____/\
(_______)(_______)(_______/\_______)\_______)  (_______)|/     \||/     \|(_______/""")


def play_game():
    guessed_number = random.randint(1,100)
    is_game_continue = True
    option = input("choose the difficultiy 'easy' or 'hard': " )
    if option == 'easy':
       count = 10
    elif option =='hard':
       count = 5 
    else:
        "please choose the correct level"
        return
    print(f"You have remaining {count} attempts to guess a number")

    while is_game_continue and count > 0:
        user_guess = int(input("Make a guess: "))
        if user_guess == guessed_number:
            print(f"You got it. The answer was {guessed_number}")
            is_game_continue = False
        elif user_guess < guessed_number:
            print("Too low.")
        else:
            print("Too high.")
               
        count -=1
        if count > 0 and is_game_continue:
            print("Guess again")
            print(f"You have {count} attempts remaining.")
    if count == 0:
       print("You lose the game.")

play_game()

