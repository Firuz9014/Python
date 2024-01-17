from replit import clear


symbols = ['/','+','*','-']
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""



def add(num1, num2):
    '''
        Take arguments num1 and num2 and return its sum
    '''
    return num1+num2


def divide(num1,num2):
    '''
        Take arguments num1 and num2 and return its divison
    '''
    return num1/num2


def susbtract(num1,num2):
    '''
        Take arguments num1 and num2 and return its substraction
    '''
    return num1-num2


def multiply(num1,num2):
    '''
        Take arguments num1 and num2 and return its multiplication
    '''
    return num1*num2



def calc(num1, num2, symb):
    if symb == '/':
        return divide(num1,num2)
    elif symb == '*':
        return multiply(num1,num2)
    elif symb == '-':
        return susbtract(num1,num2)
    elif symb == '+':
        return add(num1,num2)



def main():
    print(logo)
    num1 = int(input("What's your first number?: "))
    symb = ''
    while(True):
        while(True):
                operations = '''
                +
                /
                -
                *
                '''
                print(operations)
                symb = input("Choose an operation: ")
                if symb in symbols:
                    break
                else:
                    print('Invalid input! Please, try again!')
        num2 = int(input("What's your second number?: "))
        result = calc(num1,num2,symb)
        print(f'{num1}{symb}{num2}={result}')
        choice = input(f"Type \'y\' to continue with {result}, or type \'n\' to start a new calcuation: ")
        if choice == 'n':
            clear()
            return main()
        elif choice == 'y':
            num1 = result
            continue
        else:
            print('Invalid input!')
            return 






main()


