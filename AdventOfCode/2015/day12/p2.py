import json

def getSum(d: dict) -> int:
    if type(d) == int:
        return d

    sus = 0
    if type(d) == dict:
        for e in d:
            if d[e] == 'red':
                return 0
        
        for e in d:
            if d.get(e) != None:
                sus += getSum(d[e])
    elif type(d) == list:
        for e in d:
            if type(e) == int:
                sus += e
            elif type(e) == dict or type(e) == list:
                sus += getSum(e)
    return sus

print(getSum(json.loads(open('in').readline())))
