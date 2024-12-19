import json
with open('calculator_message.json', 'r') as file:
    MESSAGE = json.load(file)
def prompt(message):
    print(f"=> {message}")
def is_valid_value(value):
    try:
        float(value)
    except ValueError:
        return False
    return True
def messages(message, lang = 'en'):
    return MESSAGE[lang][message]
def calculator():
    flag1 = 0
    print("What is your language? en or vn")
    language = input()

    while flag1 == 0:
        prompt(messages('first number',language))
        num1 = input()
        if is_valid_value(num1):
            flag1 = 1
        else:
            print(prompt(messages('invalid number',language)))
    flag2 = 0
    while flag2 == 0:
        prompt(messages('second number',language))
        num2 = input()
        if is_valid_value(num2):
            flag2 = 1
        else:
            print("Invalid input. Please input an integer: ")
    print("""Please chooose operation: 
    1 for add 
    2 for subtract 
    3 for multiply
    4 for divide.""")
    operation = input()
    while operation not in ['1','2','3','4']:
        print("invalid choice. Please choose agian: ")
        operation = input()
    match operation:
        case '1': print(f"{num1} + {num2} = {float(num1) + float(num2)}")
        case '2': print(f"{num1} - {num2} = {float(num1) - float(num2)}")
        case '3': print(f"{num1} * {num2} = {float(num1) * float(num2)}")
        case '4': print(f"{num1} / {num2} = {float(num1) // float(num2)}")
calculator()
again = ['y', 'Y']
one_more = 1
while one_more == 1:
    decision = input("""Would you like doing another operation? 
                    y or Y for yes
                    n or N for no""")
    if decision in again:
        calculator()
    else:
            one_more = 0    
    


