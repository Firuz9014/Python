import random

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

def word_list():
    word = []
    with open('Hangman/wordlist.txt', 'r') as words:
        for row in words:
            word.append(row.strip())
        
    return word
print(logo)
# Word Database
words = word_list()

#Choose a random word from the list
chosen_word = random.choice(words)


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
life = len(stages)-1
#Result
game_result = False
result = []
used_letter = []
for letter in chosen_word:
    result.append('_')

print('\n')

# Start the loop
while '_' in result:
    print(result)
    print('\n')
    #Guess a letter
    choice = input("Guess a letter: ").lower()
    if choice == chosen_word:
        game_result = True
        print('Wow, you guessed the word.')
        print(chosen_word)
        break
    # Checking if user already used that letter
    if choice in used_letter:
        print(f'You already used {choice}, why would you use it again?\n')
        continue
    print('\n')
    found = False
    #Checking if letter in our word
    for index,letter in enumerate(chosen_word):
        # if letter inside the word change found = true and append to result
        if letter == choice:
            result[index] = choice
            found = True
    #if letter was found
    if found == True:
        print(f'You guessed {choice}')
        #if there is no letter left to guess
        if '_' not in result:
            game_result = True
            break
    #if not found
    else:
        print(f'You guessed {choice}, that is not in the word. You lost a life.(')
        print(stages[life])
        print('\n')
        #checking if there is no life left
        if life == 0:
            game_result = False
            break
        life = life - 1
    used_letter.append(choice)


if game_result == True:
    print('\n\n\n\nYou won.')
else:
    print('\n\n\n\nYou lost.')