from replit import clear
Money = 0
Milk = 200
Coffee = 100
Water = 300


coffee_types = [
    {
        'Name': 'espresso', 
        'Water': 50,
        'Coffee': 18,
        'Milk':0,
        'Price':1.50
    },
    {
        'Name': 'latte', 
        'Water': 200,
        'Coffee': 24,
        'Milk': 150,
        'Price':2.5
    },
    {
        'Name': 'cappuccino', 
        'Water': 250,
        'Coffee': 24,
        'Milk': 100,
        'Price':3.00
    }
]

def report():
    print(f'Water: {Water}ml')
    print(f'Milk: {Milk}ml')
    print(f'Coffee: {Coffee}g')
    print(f'Money: ${Money}')




def receive_payment():
    quarter = float(input("How many quarters?: "))*25
    dime = float(input("How many dimes?: "))*10
    nickle = float(input("How many nickles?: "))*5
    penny = float(input("How many pennies?: "))
    Total = (quarter+dime+nickle+penny)/100
    return Total



def check_resources(name):
    found = False
    for cf in coffee_types:
        if cf['Name'] == name.lower():
            found = True
            if Milk - cf['Milk'] <= 0: ## Water > c['Water'] and Coffee > c['Coffee']:)
                 print('Sorry, there is no enough Milk')
                 return False
            if Water - cf['Water'] <= 0:
                 print('Sorry, there is no enough Water')
                 return False
            if Coffee - cf['Coffee'] <= 0:
                 print('Sorry, there is no enough Coffee')
                 return False
            return cf['Price']
    if found == False:
        print('Not found!')
        return False


def complete_transaction(name):
    for cf in coffee_types:
        if cf['Name'] == name.lower():
            global Milk
            global Water
            global Coffee
            Milk = Milk - cf['Milk']
            Water = Water - cf['Water']
            Coffee = Coffee - cf['Coffee']
            global Money
            Money = Money + cf['Price']
            print(f"Here is your {name}. Enjoy!")
    





def process():
    choice = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if choice == 'report':
        report()
        return process()
    else:
        coffee = check_resources(choice)
        if coffee == False:
            return process()
        else:
            payment = receive_payment()
            if coffee - payment == 0:
                complete_transaction(choice)
                return process()
            elif payment - coffee > 0:
                print(f"You paid {payment}. Here is your change {payment-coffee} for {choice}")
                complete_transaction(choice)
                return process()
            elif payment - coffee < 0:
                print(f"You paid {payment}. The price of the {choice} is {coffee}")
                return process()
                




process()


