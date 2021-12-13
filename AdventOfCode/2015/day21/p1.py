import itertools
import functools
import math

Weapons = {   #Cost  Damage  Armor
    "Dagger":        [8,     4,       0],
    "Shortsword":   [10,     5,       0],
    "Warhammer":    [25,     6,       0],
    "Longsword":    [40,     7,       0],
    "Greataxe":     [74,     8,       0],
}
Armor = {      #Cost  Damage  Armor
    "Leather":      [13,     0,       1],
    "Chainmail":    [31,     0,       2],
    "Splintmail":   [53,     0,       3],
    "Bandedmail":   [75,     0,       4],
    "Platemail":   [102,     0,       5],
}

Rings = {   #Cost  Damage  Armor
    1:[ 25,     1,       0],
    2:[ 50,     2,       0],
    3:[100,     3,       0],
    4:[ 20,     0,       1],
    5:[ 40,     0,       2],
    6:[ 80,     0,       3],
}

Enemy = {
    "Hit Points": 109,
    "Damage": 8,
    "Armor": 2
}
# Enemy = {
#     "Hit Points": 12,
#     "Damage": 7,
#     "Armor": 2
# }
Player = {
    "Hit Points": 8,
    "Damage": 5,
    "Armor": 5
}


def doesPlayerWin(Enemy: dict, Player: dict) -> bool:
    enemy = dict(Enemy)
    player = dict(Player)
    playerTurn = True
    while enemy['Hit Points'] > 0 and player['Hit Points'] > 0:
        if playerTurn:
            damage = max(1, player['Damage'] - enemy['Armor'])
            enemy['Hit Points'] -= damage
        else:
            damage = max(1, enemy['Damage'] - player['Armor'])
            player['Hit Points'] -= damage
        # print(enemy, player)
        playerTurn = not playerTurn
        
    return player['Hit Points'] > 0

# print(play(Enemy, Player))



weapons = list(itertools.combinations(Weapons, 1))
armor = list(itertools.combinations(Armor, 1)) + list(itertools.combinations(Armor, 0))
rings = list(itertools.combinations(Rings, 2)) + list(itertools.combinations(Rings, 1)) + list(itertools.combinations(Rings, 0))

minGold = math.inf

for w in weapons:
    for a in armor:
        for r in rings:
            loadout = [Weapons[name] for name in w] + [Armor[name] for name in a] + [Rings[name] for name in r]
            stats = functools.reduce(lambda a, b: [a[0] + b[0], a[1] + b[1], a[2] + b[2]], loadout, [0, 0, 0])
            Player = {
                "Hit Points": 100,
                "Damage": stats[1],
                "Armor": stats[2]
            }
            if doesPlayerWin(Enemy, Player):
                minGold = min(minGold, stats[0])
            
print(minGold)
