import random
# Hangman

word_list = ["advark","baboon","camel"]

computer_choice = random.choice(word_list)
# print(computer_choice)
display = []

for letter in range(len(computer_choice)):
    display += "_"
    
print(display)

guesses = 6

playing = True

while playing:

    user_guess = input("guess a letter: ").lower()
 
    for position in range(len(computer_choice)):
        letter = computer_choice[position]
        if letter == user_guess:
            display[position] = letter

    if user_guess not in computer_choice:
        print("Not in word")
        guesses -= 1
            
    print(display)
    if "_" not in display:
        print("You win")
        playing = False
    elif guesses == 0:
        print("You lose")
        playing = False

# if user_guess in computer_choice:
#     print("you got a word")