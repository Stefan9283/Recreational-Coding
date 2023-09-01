
from CircularDoublyLinkedList import CircularDoublyLinkedList


players_count, last_marble = [int(tok) for idx, tok in enumerate(open('in').read().split()) if idx in [0, 6] ]
last_marble *= 100
players = [0 for _ in range(players_count + 1)]

circle = CircularDoublyLinkedList()
circle.add(0)
player_idx = 1
for marble in range(1, last_marble+1):
    if marble % 23 != 0:
        circle.shift(1)
        circle.add(marble)
        circle.shift(1)
    else:
        circle.shift(-7)
        players[player_idx] += circle.get() + marble
        circle.remove()
    
    player_idx += 1
    if player_idx > players_count:
        player_idx = 1
    # print(marble, circle)
    # print(marble)
            
print(max(players))