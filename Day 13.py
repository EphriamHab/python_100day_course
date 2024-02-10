
# debugging


number = int(input("Which nuber do you want to check: "))

# the error is the use of assignment operator in the if clause
# we use eaulity operater to get boolean value
if number % 2 == 0:
    print("Even number")
else:
    print("Odd numbers")