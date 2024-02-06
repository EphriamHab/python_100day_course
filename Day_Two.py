num_char = len(input("What is your name?"))
new_num_char = str(num_char)
print("Your name have "+ new_num_char +" characters.")

# challenge

two_digit_number = input("Type a two digit number?")

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
sum = first_digit + second_digit

print(sum)

# mathematical operation in python
# PEMDAS

# BMI challenge 

height =  float(input("enter your height in m: "))
weight = int(input("enter your weight in kg:  "))

BMI = weight/(height ** 2 )

print(int(BMI))

# chalenge of F string

age = input("what is your current age?")

age_remain_years = 90 - int(age)
age_remain_days = age_remain_years*365
age_remain_months = age_remain_years*12
age_remain_weeks = age_remain_years*52

print(f"You have {age_remain_days} days, {age_remain_weeks} weeks and {age_remain_months} months left.")


# Tip calculator 
print("Welcome to the tip calculator!!!")
bill = float(input("what was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay {final_amount} $")



