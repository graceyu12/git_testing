#import random
import random

#create a score variable
#set it equal to zero and add the values of each roll
player_1_score = 0

#tuple for dice values
dice_values = (1,2,3,4,5,6)

#three initial rolls
#print each value for player
roll_1 = random.choice(dice_values)
player_1_score += roll_1
print(f"Player 1 rolled a {roll_1}, for a total score of {player_1_score}.")

roll_2 = random.choice(dice_values)
player_1_score += roll_2
print(f"Player 1 rolled a {roll_2}, for a total score of {player_1_score}.")


roll_3 = random.choice(dice_values)
player_1_score += roll_3
print(f"Player 1 rolled a {roll_3}, for a total score of {player_1_score}.")

#player_1_score = roll_1 + roll_2 + roll_3
#print(player_1_score)


#create if statements to check if any of the roll values equal each other
#if the values do equal each other, player should have the option to reroll
if roll_1 == roll_2:
    reroll_3_Q = input("Do you want to reroll your 3rd die? Type 'yes' or 'no'")
    if reroll_3_Q == "yes":
         roll_3 = (random.randint(1,6)) 
         print(roll_3)
    elif reroll_3_Q == "no":
        pass
    else: input("Do you want to reroll your 3rd die? Type 'yes' or 'no'")
elif roll_2 == roll_3:
    reroll_1_Q = input("Do you want to reroll your 1st die? Type 'yes' or 'no'\n")
    if reroll_1_Q == "yes":
        roll_1 = (random.randint(1,6)) 
        print(roll_1)
    elif reroll_1_Q == "no":
        pass
    else: input("Do you want to reroll your 3rd die? Type 'yes' or 'no'")
elif roll_1 == roll_3:
    reroll_2_Q = input("Do you want to reroll your 2nd die? Type 'yes' or 'no'")
    if reroll_2_Q == "yes":
        roll_2 = (random.randint(1,6)) 
        print(roll_2)
    elif reroll_2_Q == "no":
        pass
    else: input("Do you want to reroll your 3rd die? Type 'yes' or 'no'")
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

Score = {"player_1_scores" : player_1_score}
                 
for player_1_score in Score["score"]:
    player_1_score.append(player_1_score)