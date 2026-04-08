
import random 

choices = 1, 2, 3
user_choice = int(input("Enter Choice in snake, water gun(1, 2, 3): "))
comp_choice = random.choice(choices)

dic = {1:"Snake", 2:"Water", 3:"Gun"}

print(f"\nYour Choice => {dic[user_choice]}\nCompute's choice => {dic[comp_choice]}")

win = (
    (1, 2),
    (2, 3),
    (3, 1)
)
lose = (
    (1, 3),
    (2, 1),
    (3, 2)
)

if (user_choice, comp_choice) in win:
    print("You Win!!!")
    
elif (user_choice, comp_choice) in lose:
    print("You Lose!!")

else:
    print("It's a Tie!")