import random
from words import word_list
from hung import lives
import os
#Welcome
print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                    ''')

chosen_word = random.choice(word_list)

#FOR MAKING OF BLANK SPACES
result = []
for i in range(len(chosen_word)):
    result += "_"
print("   ".join(result))

#Life is initialized
life = 6

#Iteration Begins here
while life != 0:
    guess = input("\nGuess a letter: ").lower()
    os.system('cls')

    for i in range(len(chosen_word)):
        if guess in result:
            print("This letter is already chosen\n")
        elif chosen_word[i] == guess:
            result[i] = guess
        
    if guess not in chosen_word:
        life -= 1
        print(lives[life])
        print(f"\nWrong guess you have {life} life left.")
        if (life == 0):
            print("Game Over")
            print(f"Correct Answer was :: {chosen_word}")
            exit()
    print("   ".join(result))
    if (result == list(chosen_word)):
        print("\nYou Won")
