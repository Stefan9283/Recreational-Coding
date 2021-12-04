from typing import List

file1 = open('in', 'r')
Lines = file1.readlines()

def isBingo(board: List[List[int]]):
    for row in board:
        if row.count(None) == 0:
            return True

    for i in range(0, 5):
        NoneFound = 0
        for j in range(0, 5):
            if board[j][i] == None:
                NoneFound += 1
                break
        if NoneFound == 0:
            print("col", i)
            return True
    return False

def getElemPosition(board: List[List[int]], target: int) -> List[int]:
    for i in range(0, 5):
        for j in range(0, 5):
            if board[i][j] == target:
                return i, j

def getNotYetChosenSum(board: List[List[int]], complete: List[List[int]]) -> int:
    s = 0
    for i in range(0, 5):
        for j in range(0, 5):
            if board[i][j] == None:
                s += complete[i][j]
    return s
order = []
for num in Lines[0].split(','):
    order.append(int(num))

bingoBoardsCount = (len(Lines) - 1) // 6

bingoBoards = []

for i in range(0, bingoBoardsCount):
    board = []
    for row in range(0,5):
        rowList = []
        for num in Lines[i * 6 + 1 + row + 1].split():
            rowList.append(int(num))
        board.append(rowList)
    bingoBoards.append(board)

emptyBoards = []
for board in bingoBoards:
    empty_board = []
    for i in range(0, 5):
        empty_board.append([None, None, None, None, None])
    emptyBoards.append(empty_board)

pickCount = 0
lastPicked = None
bingo = None

for pick in order:
    lastPicked = pick
    foundBingo = False
    for board, empty_board in zip(bingoBoards, emptyBoards):
        print(board, empty_board, pick)
        coords = getElemPosition(board, pick)
        if coords == None:
            continue
        i, j = coords
        empty_board[i][j] = pick
        if isBingo(empty_board):
            foundBingo = True
            bingo = empty_board, board
    if foundBingo == True:
        break
    pick += 1

