#import random
import random

game_finished = False
#create a score variable
#set it equal to zero and add the values of each roll
player_1_score = 0
#create a variable to track number of rolls
rolls = 0

#tuple for dice values
dice_values = (1,2,3,4,5,6)

#three initial rolls
#print each value for player
#add values to score and increase roll number by 1
roll_1 = random.choice(dice_values)
print(roll_1)
player_1_score += roll_1
rolls += 1
print(f"Player 1 rolled a {roll_1}, for a total score of {player_1_score}.")

roll_2 = random.choice(dice_values)
print(roll_2)
player_1_score += roll_2
rolls += 1
print(f"Player 1 rolled a {roll_2}, for a total score of {player_1_score}.")

roll_3 = random.choice(dice_values)
print(roll_3)
player_1_score += roll_3
rolls += 1
print(f"Player 1 rolled a {roll_3}, for a total score of {player_1_score}.")


#create if statements to check if any of the roll values equal each other
#if the values do equal each other, player should have the option to reroll
while game_finished == False:
    if roll_1 == roll_2:
        reroll_3_Q = input("Do you want to reroll your 3rd die? Type 'yes' or 'no'")
        if reroll_3_Q == "yes":
            roll_3 = random.choice(dice_values)
            print(roll_3)
            rolls += 1
        elif reroll_3_Q == "no":
            game_finished = True
        else: 
            input("Do you want to reroll your 1st die? Type 'yes' or 'no'")
    elif roll_2 == roll_3:
        reroll_1_Q = input("Do you want to reroll your 1st die? Type 'yes' or 'no'\n")
        if reroll_1_Q == "yes":
            roll_1 = random.choice(dice_values)
            print(roll_1)
            rolls += 1
        elif reroll_1_Q == "no":
            game_finished = True
        else: 
            input("Do you want to reroll your 2nd die? Type 'yes' or 'no'")
    elif roll_1 == roll_3:
        reroll_2_Q = input("Do you want to reroll your 2nd die? Type 'yes' or 'no'")
        if reroll_2_Q == "yes":
            roll_2 = random.choice(dice_values)
            print(roll_2)
            rolls += 1
        elif reroll_2_Q == "no":
           game_finished = True
        else: 
            input("Do you want to reroll your 3rd die? Type 'yes' or 'no'")
    elif roll_1 == roll_2 and roll_2 == roll_3 and roll_3 == roll_1:
        player_1_score = 0
        game_finished = True
    else: 
        reroll_all = input("Would you like to reroll your dice?")
        if reroll_all == "yes":
            roll_4 = random.choice(dice_values)
            player_1_score += roll_1
            rolls += 1
            print(f"Player 1 rolled a {roll_4}, for a total score of {player_1_score}.")
            roll_5 = random.choice(dice_values)
            player_1_score += roll_1
            rolls += 1
            print(f"Player 1 rolled a {roll_5}, for a total score of {player_1_score}.")
            roll_6 = random.choice(dice_values)
            player_1_score += roll_1
            rolls += 1
            print(f"Player 1 rolled a {roll_6}, for a total score of {player_1_score}.")



if rolls >= 5:
    game_finished == True

Score = {"player_1_scores" : player_1_score}
                 
for player_1_score in Score["score"]:
    player_1_score.append(player_1_score)