# Dice-Game
This is a simple program designed to mimic the app Bank! on the Apple App store. I do not claim to have invented this app or game. The rights to the actual game are owned by ThunderHive Games LLC. This code repository is to mimic the gameplay.  See README file for game explanation.
1. Players choose the number of rounds they want to play (10, 15, or 20)
2. They specify number of players.
3. During each round, players roll two dice and input the amount the dice add up to (2-12)
4. During the first 3 rounds, if a 7 is rolled, 70 points are added to the round total. All other totals remain the same.
5. After 3 round, if a 7 is rolled, the total goes to 0 and the round ends. If a double is rolled (two 2's, two 1's, etc.) the score doubles.
6. At any point during the game, a player may bank or save the round total points to their overall points. They are ineligible to continue rolling for that round.
7. The game ends when all the rounds are played and whoever ends with the most points wins!

Some notes about the code:
This is a simple python program using object-oriented programming. Player classes are created and used throughout the game. Other methods are used like Bank() and playGame(). This is a work in progress so not all funtionality is there.
   
