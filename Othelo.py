
class State:
    def __init__(self):
        self.Board[3][3] = 'H'
        self.Board[3][4] = 'C'
        self.Board[4][3] = 'C'
        self.Board[4][4] = 'H'
        self.Board[5][2] = 'H'

    Board = [['' for i in range(8)]for j in range(8)]

    def EvaluationFunction(self):
        CCount = 0
        HCount = 0

        for i in range(8):
            for j in range(8):
                if self.Board[i][j] == 'C':
                    CCount += 1
                if self.Board[i][j] == 'H':
                    HCount += 1

        if HCount + CCount == 64:
            return int('-inf')
        else:
            return HCount - CCount

    def SanityChecks(self, row, col, Turn):

        OpponentPiece = 'H' if Turn == 'C' else 'C'  # that sprite that is inbetween the turn's Piece

        if self.Board[row][col] != '':
            return False
        if (self.AllMoves(Start=col-1, x=row, y=col-1, XIncr=0, YIncr=-1, Step=-1, Range=0, Turn=Turn,
                          OpponentPiece=OpponentPiece)  # Left Horizontal
                or (self.AllMoves(Start=col+1, x=row, y=col+1, XIncr=0, YIncr=1, Step=1, Range=8, Turn=Turn,
                                  OpponentPiece=OpponentPiece))  # Right Horizontal
                or (self.AllMoves(Start=row-1, x=row-1, y=col, XIncr=-1, YIncr=0, Step=-1, Range=0, Turn=Turn,
                                  OpponentPiece=OpponentPiece))  # Up Vertical
                or (self.AllMoves(Start=row+1, x=row+1, y=col, XIncr=1, YIncr=0, Step=1, Range=8, Turn=Turn,
                                  OpponentPiece=OpponentPiece))  # Down Vertical
                or (self.AllMoves(Start=col + 1, x=row-1, y=col+1, XIncr=-1, YIncr=1, Step=1, Range=8, Turn=Turn,
                                  OpponentPiece=OpponentPiece))    # Top Right Diagonal
                or (self.AllMoves(Start=col + 1, x=row-1, y=col-1, XIncr=-1, YIncr=-1, Step=-1, Range=0, Turn=Turn,
                                  OpponentPiece=OpponentPiece))  # Top Left Diagonal
                or (self.AllMoves(Start=col + 1, x=row+1, y=col+1, XIncr=1, YIncr=1, Step=1, Range=8, Turn=Turn,
                                  OpponentPiece=OpponentPiece))  # Bottom Right Diagonal
                or (self.AllMoves(Start=col - 1, x=row+1, y=col-1, XIncr=1, YIncr=-1, Step=-1, Range=0, Turn=Turn,
                                  OpponentPiece=OpponentPiece))):  # Bottom Left Diagonal  # Down Vertical
            return True
        else:
            return False

    def AllMoves(self, Start, x, y, XIncr, YIncr, Step, Range, Turn, OpponentPiece):
        sandwich = False
        if (x > 7 or y > 7) or (x < 0 or y < 0):
            return False

        for i in range(Start, Range, Step):
            if (self.Board[x][y] == '') or (self.Board[x][y] == Turn and sandwich is False):
                return False
            if self.Board[x][y] == OpponentPiece and sandwich is False:
                sandwich = True
            if self.Board[x][y] == Turn and sandwich is True:
                return True

            x += XIncr
            y += YIncr

    def InEightMoves(self, SRow, SCol, Row, Col):
        return ((SRow != Row and SCol != Col) and ((SRow == Row and SCol != Col)
                or (SCol == Col and SRow != Row)
                or (abs(SRow-Row) == abs(SCol-Col))))


class Othelo:

    def __init__(self):
        self.turn = 'C'

    turn = 'C'  # H for Human, C for Computer
    InitialBoard = State()

    def MinMax(self):
        pass

    def ToggleTurn(self):
        self.turn = 'C' if self.turn == 'H' else 'H'

    def MakeMove(self, x, y):
        self.InitialBoard.Board[x][y] = self.turn

