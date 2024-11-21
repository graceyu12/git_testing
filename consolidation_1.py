#after each roll, display score
import random

fixed = False

roll_1 = (random.randint(1,6)) 
print(roll_1)

roll_2 = (random.randint(1,6)) 
print(roll_2)

roll_3 = (random.randint(1,6)) 
print(roll_3)

player_1_score = roll_1 + roll_2 + roll_3

if roll_1 == roll_2:
    reroll_3rd = input("Do you want to reroll your 3rd die? Type 'yes' or 'no'")
    if reroll_3rd == "yes":
         roll_3 = (random.randint(1,6)) 
         print(roll_3)
elif roll_2 == roll_3:
    reroll_1st = input("Do you want to reroll your 1st die? Type 'yes' or 'no'")
    if reroll_1st == "yes":
        roll_1 = (random.randint(1,6)) 
        print(roll_1)
elif roll_1 == roll_3:
    reroll_2nd = input("Do you want to reroll your 2nd die? Type 'yes' or 'no'")
    if reroll_2nd == "yes":
        roll_2 = (random.randint(1,6)) 
        print(roll_2)
elif roll_1 == roll_2 == roll_3:
    number = player_1_score
    result = player_1_score + 0
    print(f"Player 1's Score is now {player_1_score}. Switching to Player 2's turn")
else: 
    print(f"Player 1's score is {roll_1} + {roll_2} + {roll_3}")
    roll_1 = (random.randint(1,6)) 
    print(roll_1)

    roll_2 = (random.randint(1,6)) 
    print(roll_2)

    roll_3 = (random.randint(1,6)) 
    print(roll_3)

player_1_score = roll_1 + roll_2 + roll_3
print(f"Player 1's Score is now {player_1_score}")

#if roll_1 == roll_2 == roll_3:
    #fixed == True
    #print("It's now player 2's turn")

