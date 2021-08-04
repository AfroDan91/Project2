import random

###### machine2 - generates enemys stats ######
def enemy_gen():
    names = ["Jack the ripper","Angry Dave", "Crazy Pat"]
    enemy_name = random.choice(names)
    attack = random.randint(1, 10)
    defence = random.randint(1, 10)
    estats = [enemy_name, attack, defence]

    return estats


###### machine3 - generates players stats ######
def player_gen():
    names = ["Steve the King", "Evan Almighty", "Thor"]
    player_name = random.choice(names)
    attack = random.randint(1, 10)
    defence = random.randint(1, 10)
    pstats = [player_name, attack, defence]

    return pstats



enemy_stats = enemy_gen()
player_stats = player_gen()



###### machine4 - checks to see who won ######
def who_won(p, e):
    
    if p[1] + p[2] >= e[1] + e[2]:
        winner = p[0]
    elif e[1] + e[2] > p[1] + p[2]:
        winner = e[0]
    else:
        winner = "... no one! It was a draw. Play again if you want to see who the real winner is"
    
    victor = f"The winner is {winner}!"

    return victor
    




###### machine1 - makes displays information ######

enemy_gen()  # generates an enemy name, attack and defence
player_gen() # generates a player name, attack and defence
who_won_the_battle = (who_won(player_stats, enemy_stats))

print(who_won_the_battle)

