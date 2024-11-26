This is the README for my Tuple-Out Dice game!

In this game, a single player will roll 3 dice and then have the option to reroll a single die if the two other dice are equal, or reroll all of them if none of the dice values are equal. On the off chance that all the dice roll the same value, then the player's score will be 0. The goal of the game is to see how high you can score within 6 or less rolls. 

Step 1:
When running this game in the terminal with 'python consolidation_1.py', the player will not need to worry about importing the random module or running the initializing functions/tuple. (Side note- I saved the dice values as a tuple since the values are unchanging.)

Step 2:
The game will automatically roll the player's first 3 dice. These values will be printed out and added to a dictionary. I decided on a dictionary to store the final values since the extra rolls are optional, and so it would be ideal to append them on.

Step 3:
Run through the while loop.
If all of the values are equal, then the player's score will be 0. If 2 of them are equal, then the player will have the option to reroll the remaining dice. If a player chooses not to reroll their dice, or should their rolls exceed 6, then the game will stop. If none of the values equal each other, then the player can reroll all of their dice.


A player's final score will be printed out so that the player can try and exceed this score on their next playthrough. 