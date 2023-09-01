
players_count, last_marble = [int(tok) for idx, tok in enumerate(open('in').read().split()) if idx in [0, 6] ]
players = [0 for _ in range(players_count + 1)]
circle = [ 0 ]
curr_idx = 0
player_idx = 1

for marble in range(1, last_marble+1):
    if marble % 23 != 0:
        next_idx = (curr_idx + 2) % circle.__len__()
        circle.insert(next_idx, marble)
        curr_idx = next_idx
    else:
        curr_idx = (curr_idx - 7 + circle.__len__()) % circle.__len__()
        players[player_idx] += circle.pop(curr_idx) + marble
        
    # print(f'[{player_idx}] {" ".join(list(map(str, circle[:curr_idx])))} ({circle[curr_idx]}) {" ".join(list(map(str, circle[curr_idx + 1:])))}')

    player_idx += 1
    if player_idx > players_count:
        player_idx = 1



print(players)
print(max(players))