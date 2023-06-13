'''
This code checks if there is any winning category. A check is made against each winning category starting from Highest ranking
category. If a winning category is found the winning combination is returned or else a 'False' is returned.
'''
from cards import Deck
from cards import Card
from functools import reduce
from collections import Counter

def is_consecutive(list, count): 
    ''' Function checks if there is a certain number of consecutive cards'''
    consecutive_count = 0
    for i in range(len(list) - 1):
        if list[i] + 1 == list[i+1]:
            consecutive_count += 1
            if consecutive_count == count-1:
                return True
        else:
            consecutive_count = 0
    return False

def find_consecutive_values(list, count): 
    ''' Function finds consecutive cards if any and returns it'''
    for i in range(len(list) - count + 1):
        if all(list[i+j] == list[i+j+1] - 1 for j in range(count - 1)):
            return list[i:i+count]
    return []

def repeating_items(list, count): 
    ''' Function checks if there are pairs and checks for the number of pairs found'''
    repeating=[]
    dictionary = {}
    
    for item in list:
        if item not in dictionary:
            dictionary[item] = 1
        else:
            dictionary[item] += 1
    
    for key, value in dictionary.items():
        if value == count:
            repeating.append(key)
    
    return repeating


#----------------------------------------------------------------------------------------

def one_pair(community,p):
    ''' Function checks if one pair category is being fulfilled. If yes the winning combination is returned
    else a 'False' is returned. '''
    winning_combo=[]
    p_values=[] #stores ranks of cards   
    p_com= reduce(lambda x, y: x + y, [community,p])
    for i in p_com:
        p_values.append((i.get_value()))
    repeating_elements=repeating_items(p_values,2)

    if len(repeating_elements) == 1:
        for j in p_com:
            if j.get_value()==repeating_elements[0]:
                winning_combo.append(i)
    else:
        return False  
    
    return winning_combo

def two_pair(community,p):
    ''' Function checks if two pair category is being fulfilled. If yes the winning combination is returned
    else a 'False' is returned. '''
    winning_combo=[]
    p_values=[] #stores ranks of cards
    p_com= reduce(lambda x, y: x + y, [community,p])
    for i in p_com:
        p_values.append((i.get_value()))
    repeating_elements=repeating_items(p_values,2)

    if len(repeating_elements) == 2:
        for x in range(2):
            for j in p_com:
                if j.get_value()==repeating_elements[x-1]:
                     winning_combo.append(j)
    else:
        return False  
    
    return winning_combo

def three_of_a_kind(community,p):
    ''' Function checks if three of a kind category is being fulfilled. If yes the winning combination is returned
    else a 'False' is returned. '''
    winning_combo=[]
    p_values=[] #stores ranks of cards
    p_com= reduce(lambda x, y: x + y, [community,p])
    for i in p_com:
        p_values.append((i.get_value()))

    repeating_elements = repeating_items(p_values,3)
    
    if len(repeating_elements)>0:
         for j in p_com:
            if j.get_value()==repeating_elements[0]:
                winning_combo.append(j)     

    if len(winning_combo) ==3:
        return winning_combo
    else:
        return False
    

def straight(community,p):
    ''' Function checks if straight category is being fulfilled. If yes the winning combination is returned
    else a 'False' is returned. '''
    p_values=[] #stores ranks of cards    
    win=[]
    winning_combo=[]
    p_com= reduce(lambda x, y: x + y, [community,p])
    for i in p_com:
        p_values.append((i.get_value()))
    sorted_p=sorted(list(set((p_values)))) #removes duplicate values and then sorts
    result=is_consecutive(sorted_p,5) #checks if has 5 consecutive values
    if result == True:
        combo=find_consecutive_values(sorted_p,5)
        for j in combo:
         win.append(p_values.index(j))  

        for h in win:
            winning_combo.append(p_com[h])    
    
    if len(winning_combo)>0:
        return winning_combo
    else:
        return False

def flush(community,p):
    ''' Function checks if flush category is being fulfilled. If yes the winning combination is returned
    else a 'False' is returned. '''
    p_values=[] #stores ranks of cards
    p_com= reduce(lambda x, y: x + y, [community,p])
    
    for i in p_com:
        p_values.append((i.get_suit()))
    repeat_suit=repeating_items(p_values,5)
    
    if len(repeat_suit)>0:
        winning_combo=[]
        for j in p_com:
            if j.get_suit()==repeat_suit[0]:
                winning_combo.append(j)
        return winning_combo
    else:
        return False

def full_house(community,p):
    ''' Function checks if full house category is being fulfilled. If yes the winning combination is returned
    else a 'False' is returned. '''
    is_three_of_kind=three_of_a_kind(community,p)
    is_one_pair=one_pair(community,p)    
    if is_three_of_kind and is_one_pair:
        winning_combo=reduce(lambda x, y: x + y, [is_three_of_kind,is_one_pair])
        return winning_combo
    else:
        return False

def four_of_a_kind(community,p):
    ''' Function checks if four of a kind category is being fulfilled. If yes the winning combination is returned
    else a 'False' is returned. '''
    winning_combo=[]
    p_values=[] #stores ranks of cards
    p_com= reduce(lambda x, y: x + y, [community,p])
    for i in p_com:
        p_values.append((i.get_value()))

    repeating_elements = repeating_items(p_values,4)
    
    if len(repeating_elements)>0:
         for j in p_com:
            if j.get_value()==repeating_elements[0]:
                winning_combo.append(j)     

    if len(winning_combo) ==4:
        return winning_combo
    else:
        return False
    
def straight_flush(community,p):
    ''' Function checks if straight flush category is being fulfilled. If yes the winning combination is returned
    else a 'False' is returned. '''
    straight_combo=[]
    winning_combo=[]
    is_straight=straight(community,p)
    is_flush=flush(community,p)
    if is_straight and is_flush:
        straight_combo=straight(is_flush,p)
        winning_combo=straight_combo
    if len(winning_combo)>0:
        return winning_combo
    else:
        return False
    
# --------------------------------------------------------------------------------------------------------
def check(community,p):
    ''' Function checks if any one of the categories is being filled. Order of checking starts with highest ranking and
     search terminates as soon as first category is fulfilled. '''
    if straight_flush(community,p):
        return ("Straight Flush",straight_flush(community,p))
    elif four_of_a_kind(community,p):
        return ("Four of a Kind",four_of_a_kind(community,p))
    elif full_house(community,p):
         return ("Full house",full_house(community,p))
    elif flush(community,p):
        return ("Flush",flush(community,p))
    elif straight(community,p):
        return ("Straight",straight(community,p))
    elif three_of_a_kind(community,p):
        return ("Three of a kind",three_of_a_kind(community,p))
    elif two_pair(community,p):
        return ("Two Pair",two_pair(community,p))
    elif one_pair(community,p):
        return("One Pair",one_pair(community,p))
    else:
        return ("Nothing", False)

'''
Testing the code:
Testing phase 1: creating cards
----
c1=Card()
c2=Card()
c3=Card()
c4=Card()
c5=Card()
c6=Card()
c7=Card()
c8=Card()
c9=Card()
c1.set_rank(8)
c1.set_suit(1)

c2.set_rank(8)
c2.set_suit(2)

c3.set_rank(8)
c3.set_suit(4)

c4.set_rank(9)
c4.set_suit(4)

c5.set_rank(12)
c5.set_suit(4)

c6.set_rank(11)
c6.set_suit(4)

c7.set_rank(10)
c7.set_suit(4)
-----

Testing phase 2: Manually assigning cards to check if category checks function as intended


community=[c1,c2,c3,c4,c5]
p1=[c6,c7]
'''




