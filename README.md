# Poker-CLI-Game
Texas Hold'em Poker inspired Game using CLI.

Objectives of this project is to create a simplified Texas Hold'em Poker game using CLI. 
The rules and procedure of the game are as follows:
1. This is a two player Game
2. Program will deal two cards to both players and then five community cards which players share to make their hands. A poker hand is the best five cards from the community cards plus the player's cards. 
3. Goal is to find the category of each player's hand and determine the winner based on the rank of the category.

Categories in order from lowest to highest are: 1 pair, 2 pair, 3 of a kind, flush, Straight, Full house, 4 of a kind, Straight Flush.

To note:
a. Win is based solely of the rank of the category and not player's hand value.
b. If both players have hands in same category then it is a tie. 
c. In this game the Card class ranks Ace as the lowest card in a suit.

Files:
i. Cards.py defines Card and Deck classes.
ii. cardsDemo.py illustrates how to use Card and Deck classes.
iii. main.py is responsible for the main function where player's cards and community cards are displayed. It calls the function from categorycheck.py to find each player's respective winning category. Based on the rank of the categories, one player is deemed winner and the winning combination is outputted.
iv. categorycheck.py lists all the categories and functions to check if a player has a winning category and returns respective winning combinations.

