# Day five challenge

studnet_heights = input("Input a list of student heights ").split()
for n in range(0, len(studnet_heights)):
   studnet_heights[n] = int(studnet_heights[n]) 
print(studnet_heights)

# print the average of student height
sum_height = 0
total_students = 0
for student_height in studnet_heights:
    sum_height += student_height
    total_students += 1 
average_heiight = sum_height/total_students
print(round(average_heiight))

# Maximum of student scores with for loops

studnet_scores = input("Input a list of student scores ").split()
for n in range(0, len(studnet_scores)):
   studnet_scores[n] = int(studnet_scores[n]) 
print(studnet_scores)

current_max = studnet_scores[0]

for score in studnet_scores:
    if score > current_max:
        current_max = score
print(f"The maximum score is {current_max}")

# The sum of even numbers
total = 0
for number in range(2,101,2):
    total += number
print(total)

# fizz buzz
for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


# password generator
import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
           'p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L',
           'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','*','(',')','+']

print('Welcome to password Generator')
nr_letters = int(input("How many letters would you like in your password? \n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

# easy level
password =""
for char in range(1, nr_letters+1):
    password += random.choice(letters)
for char in range(1, nr_numbers+1):
    password += random.choice(numbers)
for char in range(1, nr_symbols+1):
    password += random.choice(symbols)

print(password)
    
#   Hard level
password_list = []
for char in range(1, nr_letters+1):
    password_list += random.choice(letters)
for char in range(1, nr_numbers+1):
    password_list += random.choice(numbers)
for char in range(1, nr_symbols+1):
    password_list += random.choice(symbols)

random.shuffle(password_list)
# print(password_list)

password = ""

for char in password_list:
    password +=char

print(f"Your password is: {password}")