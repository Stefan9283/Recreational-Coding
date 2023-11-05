

inp = [0,3,6]

occur = {}
for i in range(len(inp)):
	occur[inp[i]] = [i + 1, 1]

turns = 10

last = inp[len(inp) - 1]
mentioned_at = len(inp)

for turn in range(len(inp), turns + 1):
	if last in occur:
		diff = occur[last] - mentioned_at
		occur[diff] = 
		pass
	else:
		mentioned_at = occur[0]
		last = 0
		occur[0] = turn
		
	print(occur)