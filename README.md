This is the README for my Tuple-Out Dice game!

Step 1:
Import the random module to use random.choice

Step 2:
Run through the player's initial score and roll count (both 0) in order to add to them later on. You should also run through the dice values, saved as a tuple, since these values are unchanging.

Step 3:
The game will automatically roll the player's first 3 dice. These values will be printed out and added to a dictionary. I decided on a dictionary to store the final values since the extra rolls are optional, and so it would be ideal to append them on.

Step 4:
Run through the while loop.
If all of the values are equal, then the player's score will be 0. If 2 of them are equal, then the player will have the option to reroll the remaining dice. If a player chooses not to reroll their dice, or should their rolls exceed 6, then the while loop will break. If none of the values equal each other, then the player can reroll all of their dice.

A player's final score will be printed out so that the player can try and exceed this score on their next playthrough. 