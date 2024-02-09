
def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return formated_f_name+" "+formated_l_name


f_name = input("First Name: ")
l_name = input("Last Name: ")

formated_name = format_name(f_name,l_name)
print(formated_name)


# Calculator

def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

operations = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}
def calculator():
    num1 = float(input("What is the first number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("what is the next number?: "))

        calculation_function = operations[operation_symbol]

        answer = calculation_function (num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ") =='y':
            num1 = answer
        else:
            should_continue = False
            calculator()
            
            
calculator()