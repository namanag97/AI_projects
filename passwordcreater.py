import random
import string

def generate_password(min_length, numbers=True, Special_character=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
   
    characters = letters
    if numbers: 
     characters += digits
    if Special_character:
        characters += special

    pwd =""
    meets_criteria = False
    has_number=False
    has_special=False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char
        print(pwd)
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            mmets_criteria = has_number
        if Special_character:
            meets_criteria = meets_criteria and has_special 

    return pwd

      
min_length = int(input('min_length'))
has_number = input("do you want to have numbers y/n?").lower() == 'y'
has_special = input("do you want to have special characters y/n?").lower() == 'y'

pwd = generate_password(min_length,has_number,has_special)
print("password",pwd)


    

