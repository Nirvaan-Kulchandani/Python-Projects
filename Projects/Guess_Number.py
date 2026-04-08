import random

while True:
    
    rand_num = random.randint(1, 100)

    nums_guessed = []

    print('Hey Dear user, You have entered the Game Gf Guessing! (GOG), where u have to guess a no. between 1 - 100')
    print("Let's Start!...\n\n")

    while True:
        user_inp = int(input("Guess the number: "))
        nums_guessed.append(user_inp)

        if user_inp == 0:
            break

        if user_inp == rand_num:
            print(f"U Win!!!, u guessed the number in {len(nums_guessed)} tries!")
            print('☺☻☺ Thank You!, for playing our game ☺☻☺')
            break
        
        elif user_inp < rand_num:
            print('Wrong GueSS!,  hint: (guess a bit higher number!)\n')
        
        else:
            print('Wrong GueSS!,  hint: (guess a bit lower number!)\n')


    again_ask = input('\n\nWould u like to again play the game(Y/n): ')
    
    if (again_ask.lower() in ['n', 'no']):
        print('Ok! Bye!!')
        break
