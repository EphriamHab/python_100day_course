# simple function
def greet():
    print("Hello")
    print("How do you do")
    print("Isn't the weather nice today")

greet()

# Function that allows for input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")

greet_with_name("Ephrem")

# Function with more than 1 input
import math
def greet_with(name,location):
    print(f"Hello {name}")
    print(f"what is it in {location}")
    
greet_with("Ephrem","Nowhere")

def paint_calc(height, width, cover):
    area = height * width
    number_of_cans = math.ceil(area/cover)
    print(f"You need {number_of_cans} cans of paint.")

# test_case

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)

# prime number checker
def prime_checker(number):
    count = 0
    for x in range(1,number+1):
        if number % x ==0:
            count += 1
    if count > 2:
        print("Composite")
    elif count == 2:
        print("prime")
    else:
        print("Neither")


n = int(input("Check this number: "))
prime_checker(number = n)

# caser cipher

alphabet = ['a','b','c','d','e','f','g','h','i','j'
            'k','l','m','n','o','p','q','r','s','t',
            'u','v','x','y','z','a','b','c','d','e','f','g','h','i','j'
            'k','l','m','n','o','p','q','r','s','t',
            'u','v','x','y','z']



# combine the to function as one function

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    for letter in start_text:
        if letter in alphabet:
          position = alphabet.index(letter)
          if cipher_direction =='decode':
            shift_amount *= -1
          new_postion = position + shift_amount
          new_letter = alphabet[new_postion]
          end_text += new_letter
        else:
            end_text += letter
    print(f"The {cipher_direction}d text is: {end_text}")
should_continue = True
while should_continue:
    
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message: \n").lower()
  shift = int(input("Type the shift number: \n"))

  shift = shift % 25
  caesar(start_text = text, shift_amount=shift, cipher_direction= direction)
  result = input("Type yes if you continue or no to end: ")
  if  result  == "no":
     should_continue = False 
     print("Good Bye")
def encrypt(plain_text, shift_amount):
   cipher_text = ""
   for  letter in plain_text:
       position = alphabet.index(letter)
       new_postion = position + shift_amount
       new_letter = alphabet[new_postion]
       cipher_text += new_letter
   print(f"The encoded text is: {cipher_text}")



def decrypt(cipher_text, shift_amount):
   plain_text = ""
   for  letter in cipher_text:
       position = alphabet.index(letter)
       new_postion = position - shift_amount
       new_letter = alphabet[new_postion]
       plain_text += new_letter
   print(f"The decoded text is: {plain_text}")


if direction =="encode":
   encrypt(plain_text= text, shift_amount= shift)
elif direction =="decode":
   decrypt(cipher_text= text, shift_amount= shift)
else:
    prit("Wrong choose please enter encode or decode") 