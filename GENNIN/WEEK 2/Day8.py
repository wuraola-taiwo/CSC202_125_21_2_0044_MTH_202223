# paint area calculator
import math

test_h = int(input("Height of wall: "))
test_w = int(input("width of wall: "))
coverage = 5

def paint_calc(height, width, cover):
        number_o_cans = (height * width) / cover
        print(f"You need {math.ceil(number_o_cans)} cans of paint to cover the wall")

paint_calc(height = test_h, width= test_w, cover = coverage)

#prime number checker

n = int(input("Check this number: "))

def prime_checker(number):
    is_prime = True
    for i in range(2, number - 1):
        if number % i == 0:
            is_prime = False
    if is_prime == True:
        print("Its a prime number")
    else:
        print("Its not a prime number")
        
prime_checker(number = n)

# caesar cypher

def caesar(option, message, move):
    cypher_message = ""
    if option == "decrypt":
        move *= -1
    for i in message:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = position + move
            cypher_message += alphabet[new_position]
        else:
            message += cypher_message
        
    print(f"The {option}d text is {cypher_message}")
    


playing = True

while playing:
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    direction = input("Type 'encode' to encrypt, type 'decode' tp decrypt: ").lower()
    text = input("Type your message here: ").lower()
    shift = int(input("Enter Shift amount: "))
    shift = shift % 25


    # def encrypt(message, move):
    #     crypt_message = ""
    #     for i in message:
    #         position = alphabet.index(i)
    #         new_position = position + move
    #         crypt_text = alphabet[new_position]
    #         crypt_message += crypt_text
    #     print(f"The cypher message is {crypt_message}")
    # # encrypt(message=text, move=shift)

    # def decrypt(message, move):
    #     plain_message = ""
    #     for i in message:
    #         position = alphabet.index(i)
    #         new_position = position - move
    #         crypt_text = alphabet[new_position]
    #         plain_message += crypt_text
    #     print(f"The cypher message is {plain_message}")
    # # decrypt(message=text, move=shift)

    # if direction == "encode":

    #     encrypt(message=text, move=shift)

    # elif direction == "decode":

    #     decrypt(message=text, move=shift)

    # else:
    #     print("Enter a valid option")

    

            
    caesar(option=direction, message=text, move=shift)
    play = input("Do you want to go again Y/N: ").lower()
    if play != "y":
        playing = False