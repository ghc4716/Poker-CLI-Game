import cards 
import categorycheck
''' The game functions as follows:
    1) Create a Deck and Shuffle it and deals all the cards to players and community cards
    2) A function is called from categorycheck.py to check if either players have a winning category
    3) A check is made to see who has the higher winning category rank. If both have same cateogry or neither have any winning categories
    then the round ends in a draw.
    4) Players then have an option to see another hand or to terminate the game. 
    Note: The game automatically terminates when there is less than 9 cards left in the deck.
    
'''

#category ranking starting from lowest to highest rank
category=["Nothing","One Pair","Two Pair","Three of a kind","Flush","Straight","Full house","Four of a Kind","Straight Flush"]


#importing Deck class and shuffling the deck
deck=cards.Deck()
deck.shuffle()

def hand():
    #dealing cards to each player and dealing community cards
    player1=[]
    player2=[]
    community_cards=[]
    for i in range(2):
        player1.append(deck.deal())
    for i in range(2):
        player2.append(deck.deal())
    for i in range(5):
        community_cards.append(deck.deal())

    #Print community cards and player cards
    print("Community cards: ", community_cards)
    print("Player 1 cards: ", player1)
    print("Player 2 cards: ", player2)

    #check individually for each player, store highest category
    #compare categories between players to see who wins

    category_1=categorycheck.check(community_cards,player1)
    category_2=categorycheck.check(community_cards,player2)
    category_rank_1=category_1[0]
    category_rank_2=category_2[0]

    if category.index(category_rank_1)>category.index(category_rank_2):
        print("Player 1 wins")
        print("The winning category is: ", category_1[0])
        print("The winning combination is:",category_1[1])
    elif category.index(category_rank_1)<category.index(category_rank_2):
        print("Player 2 wins")
        print("The winning category is: ", category_2[0])
        print("The winning combination is:", category_2[1])
    elif category.index(category_rank_1) == category.index(category_rank_2):
        if category.index(category_rank_1)==0:
            print("It is a draw. No one wins")
        else:
            print("It is a draw")
            print("The winning category is: ", category_1[0])
            print("The combinations are:", category_1[1],category_2[1])
    else:
        print("No one wins")

    print(deck.cards_count())

#asks player if they want to play another as long as cards in deck are greater than 9
hand()
answers=["Yes","yes","y","Y"] 
prompt="Y"
while deck.cards_count() > 9 and prompt in answers:
    prompt=input("Do you want to play another hand? Y/N: ")
    if prompt in answers:
         hand()
    else:
         break
