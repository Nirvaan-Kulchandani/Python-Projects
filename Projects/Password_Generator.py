
# Project	                     Libraries	                     Idea
# 1️⃣ Random Password Generator	  random, string	Generate strong passwords


import random
import string

def generate_password(min_length=9, max_length=12, use_special_chars=True):
    '''Generates a random password with given length and chaaracter set.'''

    if min_length < 8 or max_length > 15:
        raise ValueError("Password length must be between 8 and 15 characters.")
    
    if min_length > max_length:
        raise ValueError("Minimum length cannot be greater than maximum length.")
    
    # Characters that will beused in password generation

    characters = None
    if use_special_chars == 1:
        characters = string.ascii_letters + string.digits + string.punctuation
    elif use_special_chars == 0:
        characters = string.ascii_letters + string.digits
    else:
        raise Exception("Invalid input for special characters. Use 1 for yes and 0 for no.")
    
    pass_length = None
    if min_length == max_length:
        pass_length = min_length
    else:
        pass_length = random.randint(min_length, max_length)

    password = ''.join(random.choice(characters) for _ in range(pass_length))

    return password



if __name__ =="__main__":
    try:
        print("Welcome to random password genrator!")
        min_Length = int(input("Enter minimum length of password (8-15): "))
        max_Length = int(input("Enter maximum length of password (8-15): "))
        special_char = int(input("Do you want Special Characters in your password? (1 for Yes, 0 for No): "))

        password = generate_password(min_Length, max_Length, special_char)
        print(f"\nPassword generated:  {password}\n\n")
        print("Thank you for using this random password generator!")

    except Exception as e:
        print(f"Error While Generating Password: {e}")

    