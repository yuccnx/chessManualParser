#-*- coding: UTF-8 -*-

RANK_TOP = 3
RANK_BOTTOM = 12
RANK_LEFT = 3
RANK_RIGHT = 11

RANK_WIDTH = 16

SQUARE_SIZE = 256

PIECE_RED   = 0x08
PIECE_BLACK = 0x10
COLOR_MARK  = 0x18

PIECE_KING    = 0x01
PIECE_ADVISOR = 0x02
PIECE_BISHOP  = 0x03
PIECE_KNIGHT  = 0x04
PIECE_ROOK    = 0x05
PIECE_CANNON  = 0x06
PIECE_PAWN    = 0x07

'''
[
    0, 0, 0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 0, 0, 0,
    0, 0, 0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 0, 0, 0,
    0, 0, 0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 0, 0, 0,
    0, 0, 0, 21, 20, 19, 18, 17, 18, 19, 20, 21, 0, 0, 0, 0,
    0, 0, 0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 0, 0, 0,
    0, 0, 0, 0,  22, 0,  0,  0,  0,  0,  22, 0,  0, 0, 0, 0,
    0, 0, 0, 23, 0,  23, 0,  23, 0,  23, 0,  23, 0, 0, 0, 0,
    0, 0, 0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 0, 0, 0,
    0, 0, 0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 0, 0, 0,
    0, 0, 0, 15, 0,  15, 0,  15, 0,  15, 0,  15, 0, 0, 0, 0,
    0, 0, 0, 0,  14, 0,  0,  0,  0,  0,  14, 0,  0, 0, 0, 0,
    0, 0, 0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 0, 0, 0,
    0, 0, 0, 13, 12, 11, 10, 9,  10, 11, 12, 13, 0, 0, 0, 0,
    0, 0, 0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 0, 0, 0,
    0, 0, 0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 0, 0, 0,
    0, 0, 0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 0, 0, 0
 ]
'''

_initFen = "rnbakabnr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RNBAKABNR w - - 0 1"

# 转Y 坐标
def RANK_Y(sq):
    return sq >> 4

# 转x 坐标
def RANK_X(sq):
    return sq & 15

# 转数据棋盘坐标
def COORD_XY(x, y):
    return x + (y << 4)

def MOVE(squares, src, to):
    squares[to] = squares[src]
    squares[src] = 0

def CHAR_TO_PIECE(c):
    side = 0
    if ("A" <= c and c <= "Z"):
        side = PIECE_RED
    elif ("a" <= c and c <= "z"):
        side = PIECE_BLACK

    if c == "K" or c == "k":
        return PIECE_KING | side
    if c == "A" or c == "a":
        return PIECE_ADVISOR | side
    if c == "B" or c == "E" or c == "b" or c == "e":
        return PIECE_BISHOP | side
    if c == "H" or c == "N" or c == "h" or c == "n":
        return PIECE_KNIGHT | side
    if c == "R" or c == "r":
        return PIECE_ROOK | side
    if c == "C" or c == "c":
        return PIECE_CANNON | side
    if c == "P" or c =="p":
        return PIECE_PAWN | side

    return -1

def squaresFromFen(fen):
    squares = [ 0 for i in range(SQUARE_SIZE)]

    x = RANK_LEFT
    y = RANK_TOP

    for c in fen:
        if c == " ":
            break

        if c == "/":
            x = RANK_LEFT
            y += 1
        elif "1" <= c and c <= "9":
            x += int(c)
        elif (("A" <= c and c <= "Z") or ("a" <= c and c <= "z")):
            squares[COORD_XY(x, y)] = CHAR_TO_PIECE(c);
            x += 1

        if y > RANK_BOTTOM:
            break

    return squares

def squaresFromInitFen():
    return squaresFromFen(_initFen)

def posStrToPos(s):
    x = "abcdefghi".find(s[0])
    y = "9876543210".find(s[1])
    if x == -1 or y == -1:
        return 0

    return COORD_XY(x+RANK_LEFT, y+RANK_TOP)

def fenMoveStrToMove(s):
    src, dst = 0, 0
    if len(s) == 4:
        src = posStrToPos(s[:2])
        dst = posStrToPos(s[2:])

    return (src, dst)

def fensMoveStrToMoves(moveStr):
    return [fenMoveStrToMove(move) for  move in moveStr.split(" ")]