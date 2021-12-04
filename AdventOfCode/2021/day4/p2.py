from typing import List

def isBingo(board: List[List[int]]):
    for row in board:
        if row.count(None) == 0:
            return True

    for i in range(0, 5):
        NoneFound = 0
        for j in range(0, 5):
            if board[j][i] == None:
                NoneFound = 1
                break
        if NoneFound == 0:
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

def prettyPrint(board: List[List[int]], complete: List[List[int]]):
    for i in range(0, 5):
        print(board[i], complete[i])

file1 = open('in', 'r')
Lines = file1.readlines()

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

lastPicked = None
bingo = None

wasBingo = [None] * len(bingoBoards)

for pick in order:
    foundBingo = False
    bingoCounter = 0
    boardID = 0
    for board, empty_board in zip(bingoBoards, emptyBoards):
        coords = getElemPosition(board, pick)
        if coords == None:
            if isBingo(empty_board):
                bingoCounter += 1
            boardID += 1
            continue
        i, j = coords
        empty_board[i][j] = pick
        if isBingo(empty_board):
            foundBingo = True
            lastPicked = pick
            bingoCounter += 1
            if wasBingo[boardID] == None:
                bingo = empty_board, board
            wasBingo[boardID] = True
            if bingoCounter == len(bingoBoards):
                break
        boardID += 1
    if bingoCounter == len(bingoBoards):
        break

print(getNotYetChosenSum(bingo[0], bingo[1]) * lastPicked)
