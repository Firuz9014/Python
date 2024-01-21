import random
from replit import clear

### CARD DECK
cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]

### LOGO

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""



def game():
    print(logo)
    computer  = [random.choice(cards), random.choice(cards)]
    player  = [random.choice(cards), random.choice(cards)]
    print(f"Your cards: {player}")
    print(f"Computer's first cards: {computer[0]}")
    while(True):
        if sum(player) == 21:
            print(f"Your cards: {player}")
            print(f"Computer's cards: {computer}")
            return 'You won'
        elif sum(player) > 21:
            print(f"Your cards: {player}")
            print(f"Computer's cards: {computer}")
            return 'You lost'
        choice = input("Type \'y\' to get another card, type \'n\' to pass: ")
        if choice == 'n':
            print(f"Your cards: {player}")
            print(f"Computer's cards: {computer}")
            break
        player.append(random.choice(cards))
        print(f"Your cards: {player}")
        print(f"Computer's first cards: {computer[0]}")
    if sum(player) > sum(computer):
        return 'You won'
    elif sum(player) == sum(computer):
        return 'Draw'
    else:
        return 'You lost'
                                      


def main():
    choice = input('Do you want to play a game of Blackjack? Type \'y\' or \'n\': ')
    if choice == 'y':
        while(True):
            g = game()
            print(g)
            choicee = input('Do you want to play again? Type \'y\' or \'n\': ')
            if choicee == 'y':
                clear()
                continue
            elif choicee == 'n':
                break
            else:
                print('Invalid input!')
                break
    elif choice == 'n':
        print('Hope to see you back!')
        return 
    else:
        return main()
    
    print('Hope to see you back!')
    return  







main()
