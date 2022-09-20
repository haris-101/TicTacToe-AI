import random
import math

# Constants
AI = 'X'
HUMAN = 'O'

scores = {'X': 10, 'O': -10, 'T': 0}

def winDetected(board):
    winningPosX = ["XXXEEEEEE", "EEEXXXEEE", "EEEEEEXXX", "XEEXEEXEE", "EXEEXEEXE", "EEXEEXEEX", "XEEEXEEEX", "EEXEXEXEE"]
    winningPosO = ["OOOEEEEEE", "EEEOOOEEE", "EEEEEEOOO", "OEEOEEOEE", "EOEEOEEOE", "EEOEEOEEO", "OEEEOEEEO", "EEOEOEOEE"]
    emptyCount = 0
    for x in board:
        if x == "E":
            emptyCount += 1

    if board[0:3] == 'XXX' or board[3:6] == 'XXX' or board[6:9] == 'XXX':
        return 'X'
    elif board[0:3] == 'OOO' or board[3:6] == 'OOO' or board[6:9] == 'OOO':
        return 'O'
    elif board[0] == board[3] and board[3] == board[6]:
        return board[0]
    elif board[1] == board[4] and board[4] == board[7]:
        return board[1]
    elif board[2] == board[5] and board[5] == board[8]:
        return board[2]
    elif board[0] == board[4] and board[4] == board[8]:
        return board[0]
    elif board[2] == board[4] and board[4] == board[6]:
        return board[2]
    elif emptyCount == 0:
        return "T"
    else:
        return None


def present(board):
    newBrd = ""
    for x in board:
        if x != 'E':
            newBrd += x
        else:
            newBrd += " "

    print(newBrd[0] + " | " + newBrd[1] + " | " + newBrd[2])
    print("---------")
    print(newBrd[3] + " | " + newBrd[4] + " | " + newBrd[5])
    print("---------")
    print(newBrd[6] + " | " + newBrd[7] + " | " + newBrd[8])
    print('\n')



def bestMove(board):
    bestScore = -math.inf
    bestPos = None
    for x in range(len(board)):
        if board[x:x+1] == 'E':
            board = board[:x] + AI + board[x+1:]
            score = minimax(board, 0, False)
            board = board[:x] + 'E' + board[x+1:]
            if score > bestScore:
                bestScore = score
                bestPos = x
    if bestPos != None:
        board = board[:bestPos] + AI + board[bestPos+1:]
    return board






def minimax(board, depth, isMaximizing):
    result = winDetected(board)
    if result == "X" or result == "O" or result == "T":
        return scores[result]
    if isMaximizing == True:
        bestScore = -math.inf
        for x in range(len(board)):
            if board[x:x+1] == 'E':
                board = board[:x] + AI + board[x+1:]
                score = minimax(board, depth + 1, False)
                board = board[:x] + 'E' + board[x+1:]
                bestScore = max(score, bestScore)

        return bestScore
    else:
        bestScore = math.inf
        for x in range(len(board)):
            if board[x:x+1] == 'E':
                board = board[:x] + HUMAN + board[x+1:]
                score = minimax(board, depth + 1, True)
                board = board[:x] + 'E' + board[x + 1:]
                bestScore = min(score, bestScore)
        return bestScore


def gameplay():
    board = 'EEEEEEEEE'
    while winDetected(board) != "X" and winDetected(board) != "O" and winDetected(board) != "T":
        present(board)
        userInput = int(input("Where would you like to play?: "))
        board = board[:userInput - 1] + HUMAN + board[userInput:]
        board = bestMove(board)
    present(board)
    if winDetected(board) != 'T':
        print(winDetected(board), " Won!")
    else:
        print('TIE!')

gameplay()