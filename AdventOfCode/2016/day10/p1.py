
class Bot:
    def __init__(self, id) -> None:
        self.vals: list[int] = []
        self.id: int = id
    def addValue(self, val) -> None:
        self.vals.append(val)
        if self.vals.__len__() > 2:
            raise Exception()
        self.vals.sort()
    def getMin(self) -> int:
        val = self.vals[0]
        self.vals = self.vals[1:]
        return val
    def getMax(self) -> int:
        val = self.vals[-1]
        self.vals = self.vals[:-1]
        return val
    def valuesCount(self) -> int:
        return len(self.vals)
    def __str__(self) -> str:
        return "(bot " + str(self.id) + ' ' + str(self.vals) + ")"

def doOp(id, f, *args):
    if bots.get(id) == None:
            bots[id] = Bot(id)
    if len(args):
        return f(bots[id], args[0])
    else:
        return f(bots[id])

def report():
    for bot in bots:
        print(bots[bot])
    print('out', output)        
    print() 
    

bots: dict[Bot] = {}
output: dict[int] = {}

assign = [line for line in open('in').readlines() if line.startswith('value')]
give =  [line for line in open('in').readlines() if line.startswith('bot')]
lines = assign + give

rules = {} # botID -> ((type, lowID), (type, highID))


for line in lines:
    toks = line.strip('\t').split()
    if toks[0] == 'bot':
        rules[int(toks[1])] = ({'type': toks[5], 'ID': int(toks[6])}, {'type': toks[-2], 'ID': int(toks[-1])})
    else:
        doOp(int(toks[-1]), Bot.addValue, int(toks[1]))

report()

while True:
    for bot in bots:
        if doOp(bot, Bot.valuesCount) == 2:
            minVal = doOp(bot, Bot.getMin)
            maxVal = doOp(bot, Bot.getMax)
            lowID = rules[bot][0]['ID']
            lowtype = rules[bot][0]['type']
            highID = rules[bot][1]['ID']
            hightype = rules[bot][1]['type']
            
            if [minVal, maxVal] == [17, 61]:
                print('part1', bot)
            
            if lowtype == 'bot': doOp(lowID, Bot.addValue, minVal)
            else: output[lowID] = minVal
            if hightype == 'bot': doOp(highID, Bot.addValue, maxVal)
            else: output[highID] = maxVal
            break
    onBots = 0
    for bot in bots:
        onBots += doOp(bot, Bot.valuesCount)
    if onBots == 0:
        break

print('part2', output[0] * output[1] * output[2])
    






























# for i in range(len(assign)):
#     tok = instr[i].strip('\n').split()
#     print('ass', tok)
#     if tok[0] == 'value':
#         value = int(tok[1])
#         botID = int(tok[-1])
#         doOp(botID, Bot.addValue, value)
# report()
# for i in range(len(assign), len(assign) + len(give)):
#     tok = instr[i].strip('\n').split()
#     if tok[0] == 'bot':
#         srcID = int(tok[1])
#         if doOp(srcID, Bot.valuesCount) != 2: 
#             continue
#         minVal = doOp(srcID, Bot.getMin)
#         maxVal = doOp(srcID, Bot.getMax)
#         if 61 == maxVal and 17 == minVal:
#             print(srcID)
#         lowID = int(tok[6])
#         highID = int(tok[11])
#         if tok[5] == 'bot': doOp(lowID, Bot.addValue, minVal)
#         else: output[lowID] = minVal
#         if tok[10] == 'bot': doOp(highID, Bot.addValue, maxVal)
#         else: output[highID] = maxVal
#     # report()

