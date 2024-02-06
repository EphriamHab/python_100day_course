# Hangman game
import random
word_list = ["ardvark","baboon","camel"]


chosen_word = random.choice(word_list)
# Testig code
print(f"Psst, the solution is {chosen_word}.")
lives = 6
display = []
for letter in chosen_word:
  display += "_"

end_of_game = False
while not end_of_game:
   guess = input("Guess a letter: ").lower()
   
   for x in range(0, len(chosen_word)):
     if guess == chosen_word[x]:
       display[x]= guess
   if guess not in chosen_word:
      lives -= 1
      if lives ==0:
         end_of_game = True
         print("You lose.")
         
   print(display)
   if "_" not in display:
      end_of_game = True
      print("You Won")
  
# for char in chosen_word:
#    if guess == char:
#       print("Right")
#    else:
#       print("Wrong")
      
