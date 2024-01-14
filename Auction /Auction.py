from replit import clear
import operator
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''




participants = {}

print(logo)
print('Welcome to the secret auction program.')

while(True):
    name = input("What is your name?: ")
    bid = int(input('What\'s your bid?: $'))
    participants[name] = bid
    choice = input('Are there any other bidders? Type \'yes\' or \'no\'.\n')
    if choice == 'yes':
        clear()
        continue
    elif choice == 'no':
        clear()
        break

winner = max(participants.items(), key=operator.itemgetter(1))[0]

print(f'The winner is {winner} with a bid of ${participants[winner]}')
