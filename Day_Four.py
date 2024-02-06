import random

test_seed = int(input("Create a seed number"))
random.seed(test_seed)

toss_value = random.randint(0, 1)
if toss_value == 1:
    print("Heads")
else:
    print("Tails")

# Who is paying the bill
 
namesAsCSV = input("Give me everybody's names, seperated by a comm.")
names = namesAsCSV.split(', ')

assign_rand = random.randint(0, len(names)-1)

print(f"{names[assign_rand]} should pay the bill.")

row1 = [" "," "," "]
row2 = [" "," "," "]
row3 = [" "," "," "]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row1}")

position = input("Where do you want to put the treasure?")

y = int(position[0])-1
x = int(position[1])-1



map[x][y] = "X"
for row in map:
    print(row)


# Day Four final project

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images = [rock, Paper, Scissors]
user_choice = int(input("Waht is your choose? 0 for Rock. 1 for Paper, or 2 for Scissors\n"))
print(game_images[user_choice])

computer_choice = random.randint(0,2)
print("computer choice")
print(game_images[computer_choice])

if user_choice < 0 or user_choice > 2:
    print("You put invalid number, you lose")
elif user_choice == 0 and computer_choice == 2:
    print("You win")
elif user_choice == 2 and computer_choice == 0:
    print("You lose")
elif user_choice > computer_choice:
    print("You win")
elif computer_choice > user_choice:
    print("You lose")
elif computer_choice == user_choice:
    print("You draw")