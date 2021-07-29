import random

# plc1 = 0
# plc2 = 0
# hoc1 = 0
# hoc2 = 0



# def deal_player():

#     pcard1 = all_cards.pop(all_cards.index(random.choice(all_cards)))

#     pcard2 = all_cards.pop(all_cards.index(random.choice(all_cards)))

#     deal_house(all_cards)

#     print(f"You draw; {pcard1}, {pcard2}")

#     global plc1 
#     plc1 = pcard1
#     global plc2
#     plc2 = pcard2


# def deal_house(cards):
#     hcard1 = all_cards.pop(all_cards.index(random.choice(all_cards)))

#     hcard2 = all_cards.pop(all_cards.index(random.choice(all_cards)))

#     print(f"The house draws; {hcard1}, {hcard2}")
#     global hoc1
#     hoc1 = hcard1
#     global hoc2 
#     hoc2 = hcard2

# def who_won(pc1, pc2, hc1, hc2):
#     print(pc1, pc2, hc1, hc2,)
#     for i in range(11):
#         if str(i) in str(pc1):
#             pc1v = i

#     if 'J' in str(pc1):
#         pc1v = 10
#     elif 'Q' in str(pc1):
#         pcv1 = 10
#     elif 'K' in str(pc1):
#         pcv1 = 10
#     else:
#         pc1v = 1

#     for i in range(11):
#         if str(i) in str(pc2):
#             pc2v = i
#         elif 'J' in str(pc2):
#             pc2v = 10
#         elif 'Q' in str(pc2):
#             pc2v = 10
#         elif 'K' in str(pc2):
#             pc2v = 10
#         else:
#             pc2v = 1

#     for i in range(11):
#         if str(i) in str(hc1):
#             hc1v = i
#         elif 'J' in str(hc1):
#             hc1v = 10
#         elif 'Q' in str(hc1):
#             hc1v = 10
#         elif 'K' in str(hc1):
#             hc1v = 10
#         else:
#             hc1v = 1

#     for i in range(11):
#         if str(i) in str(hc2):
#             hc2v = i
#         elif 'J' in str(hc2):
#             hc2v = 10
#         elif 'Q' in str(hc2):
#             hc2v = 10
#         elif 'K' in str(hc2):
#             hc2v = 10
#         else:
#             hc2v = 1

#     player_total = pc1v + pc2v

#     house_total = hc1v + hc2v
    
#     print(f" the house draws {house_total}")
#     print(f" you draw {player_total}")
    



# all_cards = ['AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 
#     'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 
#     'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 
#     'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC']

# deal_player()

# print(plc1)

# who_won(plc1, plc2, hoc1, hoc2)


# print(all_cards)

###########################################################################################

#make a function that draws and returns 1 card from a list or dictionary of cards and removes it from the list. 



#sets gobal variables
plc1 = 0
plc2 = 0
hoc1 = 0
hoc2 = 0



def deal_player(): # this function draws cards for the player

    pcard1 = random.choice(list(all_cards.keys()))
    pcard1v = all_cards[pcard1]
    print(pcard1v)
    #del all_cards[pcard1]
   

    pcard2 = random.choice(list(all_cards.keys()))
    del all_cards[pcard2]
    
    deal_house(all_cards)

    print(f"You draw; {pcard1}, {pcard2}")
    print(all_cards)




def deal_house(cards):
    print(cards)
    hcard1 = random.choice(list(all_cards.keys()))

    hcard2 = random.choice(list(all_cards.keys()))



def who_won(pc1, pc2, hc1, hc2):
    print("hello")





all_cards = {'AH':1, '2H':2, '3H':3, '4H':4, '5H':5, '6H':6, '7H':7, '8H':8, '9H':9, '10H':10, 'JH':10, 'QH':10, 'KH':10, 
    'AD':1, '2D':2, '3D':3, '4D':4, '5D':5, '6D':6, '7D':7, '8D':8, '9D':9, '10D':10, 'JD':10, 'QD':10, 'KD':10, 
    'AS':1, '2S':2, '3S':3, '4S':4, '5S':5, '6S':6, '7S':7, '8S':8, '9S':9, '10S':10, 'JS':10, 'QS':10, 'KS':10, 
    'AC':1, '2C':2, '3C':3, '4C':4, '5C':5, '6C':6, '7C':7, '8C':8, '9C':9, '10C':10, 'JC':10, 'QC':10, 'KC':10,}

deal_player()

who_won(plc1, plc2, hoc1, hoc2)
