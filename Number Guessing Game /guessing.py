from replit import clear
import random

HARD = 5
EASY = 10


logo = '''
__          ________ _      _____ ____  __  __ ______   _______ ____    _______ _    _ ______    _____ _    _ ______  _____ _____ _____ _   _  _____    _____          __  __ ______ 
\ \        / /  ____| |    / ____/ __ \|  \/  |  ____| |__   __/ __ \  |__   __| |  | |  ____|  / ____| |  | |  ____|/ ____/ ____|_   _| \ | |/ ____|  / ____|   /\   |  \/  |  ____|
 \ \  /\  / /| |__  | |   | |   | |  | | \  / | |__       | | | |  | |    | |  | |__| | |__    | |  __| |  | | |__  | (___| (___   | | |  \| | |  __  | |  __   /  \  | \  / | |__   
  \ \/  \/ / |  __| | |   | |   | |  | | |\/| |  __|      | | | |  | |    | |  |  __  |  __|   | | |_ | |  | |  __|  \___ \\___ \  | | | . ` | | |_ | | | |_ | / /\ \ | |\/| |  __|  
   \  /\  /  | |____| |___| |___| |__| | |  | | |____     | | | |__| |    | |  | |  | | |____  | |__| | |__| | |____ ____) |___) |_| |_| |\  | |__| | | |__| |/ ____ \| |  | | |____ 
    \/  \/   |______|______\_____\____/|_|  |_|______|    |_|  \____/     |_|  |_|  |_|______|  \_____|\____/|______|_____/_____/|_____|_| \_|\_____|  \_____/_/    \_\_|  |_|______|
                                                                                                                                                                                     
                                                                                                                                                                                     

'''



def guessing_game():
    print(logo)
    number = random.randint(1,100)
    print("I am thinking of a number between 1 and 100.")
    difficulty_level = input("Choose difficulty. Type \'easy\' or \'hard\': ")
    if difficulty_level == 'easy':
        life = EASY
    elif difficulty_level == 'hard':
        life = HARD
    else:
        print('Invalid Input!')
    while(life != 0):
        print(f"You have {life} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > number:
            print('Too High.')
            life -= 1
        elif guess < number:
            print('Too Low.')
            life -= 1
        elif guess == number:
            print(f'You won. The number is {number}')
            return
        if life != 0:
            print('Guess again.')
        elif life == 0:
            print(f"You lost. The number is {number}")




guessing_game()
