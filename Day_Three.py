
# Leap year challenge

year = int(input("Enter the year to check leap year or not?"))

if year % 4 != 0:
    print(f"{year} is not leap year")
elif year % 100 == 0 and year %  400 !=0:
    print(f"{year} is not leap year")
else:
    print(f"{year} is leap year")
    
    
# an other solution

if year % 4 ==0:
  if year % 100 == 0:
    if year % 400 == 0:
        print("Leap Year")
    else:
        print("Not Leap Year")
  else:
      print("Leap year")
else:
    print("Not Leap Year")

# Love Calculator
print("Welcome to love calculator!!!")

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name1_as_lower = name1.lower()
name2_as_lower = name2.lower()
combined_string = name1_as_lower + name2_as_lower

t = combined_string.count("t")
r = combined_string.count("r")
u = combined_string.count("u")
e = combined_string.count("e")

l = combined_string.count("l")
o = combined_string.count("o")
v = combined_string.count("v")
e = combined_string.count("e")

sum_true = t+r+u+e
sum_love = l+o+v+e

calculate_value = str(sum_true) + str(sum_love)

print(calculate_value)

calculate_value_as_num = int(calculate_value)

if calculate_value_as_num < 10 or calculate_value_as_num > 90:
    print(f"Your score is {calculate_value_as_num}, You go together like coke and mentos.")

elif calculate_value_as_num >= 40 and calculate_value_as_num <= 50:
    print(f"Your score is {calculate_value_as_num}, You are alright together.")
else:
    print(f"Your score is {calculate_value_as_num}.")
    
# Treasure island
print('''
      *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
      ''')

print("Welcome to Tresure Island")
print("Your mission is to find the tresure.")
choice1 = input('You\'re at crossroad, where do you want to go? Type "left" or "right"')

if choice1 == 'right':
    print("Game over")
elif choice1 == 'left':
    choice2 = input("Do you want to swim or wait. type 'swim' or 'right'")
    if choice2 == 'swim':
        print('Game Over')
    elif choice2 == 'wait':
        choice3 = input("which door? type 'red' or 'blue' or 'yellow'")
        if  choice3 == 'yellow':
            print("you win the game!!!")
        else:
            print("Game over")
        
