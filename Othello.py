import copy
import time

class State:

    def __init__(self, state=None):
        if state is None:
            self.Board[3][3] = 'C'
            self.Board[3][4] = 'H'
            self.Board[4][3] = 'H'
            self.Board[4][4] = 'C'
        #     self.Board[0][7] = 'H'
        #     self.Board[1][7] = 'C'
        #     self.Board[2][7] = 'C'
        #     self.Board[3][7] = 'C'
        #     self.Board[4][7] = 'C'
        #     self.Board[5][7] = 'C'
        #     self.Board[6][7] = 'C'

        else:
            self.Board = copy.deepcopy(State.Board)


    Board = [['' for i in range(8)]for j in range(8)]

    def EvaluationFunction(self):  # If Human is winning then it will return Negative Value
        CCount = 0
        HCount = 0

        for i in range(8):
            for j in range(8):
                if self.SanityChecks(i, j, 'H'):
                    HCount += 1
                if self.SanityChecks(i, j, 'C'):
                    CCount += 1
                if self.Board[i][j] == 'C':
                    CCount += 1
                if self.Board[i][j] == 'H':
                    HCount += 1

        if HCount + CCount == 64:
            return float('-inf')
        else:
            return CCount - HCount  # ComputerCount - HumanCount

    def SanityChecks(self, row, col, Turn):

        OpponentPiece = 'H' if Turn == 'C' else 'C'  # that sprite that is inbetween the turn's Piece

        if self.Board[row][col] != '':
            return False
        if (self.AllMoves(Start=col-1, x=row, y=col-1, XIncr=0, YIncr=-1, Step=-1, Range=-1, Turn=Turn,
                          OpponentPiece=OpponentPiece)  # Left Horizontal
                or (self.AllMoves(Start=col+1, x=row, y=col+1, XIncr=0, YIncr=1, Step=1, Range=8, Turn=Turn,
                                  OpponentPiece=OpponentPiece))  # Right Horizontal
                or (self.AllMoves(Start=row-1, x=row-1, y=col, XIncr=-1, YIncr=0, Step=-1, Range=-1, Turn=Turn,
                                  OpponentPiece=OpponentPiece))  # Up Vertical
                or (self.AllMoves(Start=row+1, x=row+1, y=col, XIncr=1, YIncr=0, Step=1, Range=8, Turn=Turn,
                                  OpponentPiece=OpponentPiece))  # Down Vertical
                or (self.AllMoves(Start=col + 1, x=row-1, y=col+1, XIncr=-1, YIncr=1, Step=1, Range=8, Turn=Turn,
                                  OpponentPiece=OpponentPiece))    # Top Right Diagonal
                or (self.AllMoves(Start=col + 1, x=row-1, y=col-1, XIncr=-1, YIncr=-1, Step=-1, Range=-1, Turn=Turn,
                                  OpponentPiece=OpponentPiece))  # Top Left Diagonal
                or (self.AllMoves(Start=col + 1, x=row+1, y=col+1, XIncr=1, YIncr=1, Step=1, Range=8, Turn=Turn,
                                  OpponentPiece=OpponentPiece))  # Bottom Right Diagonal
                or (self.AllMoves(Start=col - 1, x=row+1, y=col-1, XIncr=1, YIncr=-1, Step=-1, Range=-1, Turn=Turn,
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

    def FlipCells(self, row, col, Turn):
        OpponentPiece = 'H' if Turn == 'C' else 'C'  # that sprite that is inbetween the turn's Piece

        self.__FlipMoves(Start=col - 1, x=row, y=col - 1, XIncr=0, YIncr=-1, Step=-1, Range=-1, Turn=Turn,
                      OpponentPiece=OpponentPiece)  # Left Horizontal
        self.__FlipMoves(Start=col + 1, x=row, y=col + 1, XIncr=0, YIncr=1, Step=1, Range=8, Turn=Turn,
                      OpponentPiece=OpponentPiece)  # Right Horizontal
        self.__FlipMoves(Start=row - 1, x=row - 1, y=col, XIncr=-1, YIncr=0, Step=-1, Range=-1, Turn=Turn,
                      OpponentPiece=OpponentPiece)  # Up Vertical
        self.__FlipMoves(Start=row + 1, x=row + 1, y=col, XIncr=1, YIncr=0, Step=1, Range=8, Turn=Turn,
                      OpponentPiece=OpponentPiece)  # Down Vertical
        self.__FlipMoves(Start=col + 1, x=row - 1, y=col + 1, XIncr=-1, YIncr=1, Step=1, Range=8, Turn=Turn,
                      OpponentPiece=OpponentPiece)  # Top Right Diagonal
        self.__FlipMoves(Start=col + 1, x=row - 1, y=col - 1, XIncr=-1, YIncr=-1, Step=-1, Range=-1, Turn=Turn,
                      OpponentPiece=OpponentPiece)  # Top Left Diagonal
        self.__FlipMoves(Start=col + 1, x=row + 1, y=col + 1, XIncr=1, YIncr=1, Step=1, Range=8, Turn=Turn,
                      OpponentPiece=OpponentPiece)  # Bottom Right Diagonal
        self.__FlipMoves(Start=col - 1, x=row + 1, y=col - 1, XIncr=1, YIncr=-1, Step=-1, Range=-1, Turn=Turn,
                      OpponentPiece=OpponentPiece)  # Bottom Left Diagonal  # Down Vertical


    def __FlipMoves(self, Start, x, y, XIncr, YIncr, Step, Range, Turn, OpponentPiece):
        sandwich = False
        if (x > 7 or y > 7) or (x < 0 or y < 0):
            return False
        TempX = x
        TempY = y

        for i in range(Start, Range, Step):
            if (self.Board[x][y] == '') or (self.Board[x][y] == Turn and sandwich is False):
                return False
            if self.Board[x][y] == OpponentPiece and sandwich is False:
                sandwich = True  # something fishy
            if self.Board[x][y] == Turn and sandwich is True:
                for j in range(Start, Range, Step):
                    if x == TempX and y == TempY:
                        return True
                    self.Board[TempX][TempY] = Turn
                    TempX += XIncr
                    TempY += YIncr

                return True

            x += XIncr
            y += YIncr


    def InEightMoves(self, SRow, SCol, Row, Col):
        return ((SRow != Row and SCol != Col) and ((SRow == Row and SCol != Col)
                or (SCol == Col and SRow != Row)
                or (abs(SRow-Row) == abs(SCol-Col))))

    def PrintState(self):
        for i in range(0, 8):
            print(self.Board[i])

        print('-------------------------------')

class Othello:

    def __init__(self):
        self.Turn = 'H'

    Difficulty = 3
    Turn = 'H'  # H for Human, C for Computer
    InitialBoard = State()
    InLoop = True

    def MinMax(self, SomeState, Depth, IsMaxLevel):

        if Depth == self.Difficulty:
            return SomeState.EvaluationFunction(), -1, -1
        else:
            if IsMaxLevel:
                Max = float('-inf')
                MaxX = 0
                MaxY = 0
                for i in range(8):  # Computer Piece Index
                    for j in range(8):
                        if SomeState.SanityChecks(i, j, 'C'):
                            newState = State(copy.deepcopy(State))
                            newState.Board[i][j] = 'C'
                            #print('Before Flipping in MIN MAX Max Level')
                            #newState.PrintState()
                            newState.FlipCells(i, j, 'C')
                            #print('After Flipping in MIN MAX Max Level')
                            #newState.PrintState()
                            #print(Depth)
                            res, resX, resY = self.MinMax(State(copy.deepcopy(newState)), Depth + 1, not IsMaxLevel)

                            if res > Max:
                                Max = res
                                MaxX = i
                                MaxY = j

                return Max, MaxX, MaxY

            else:
                Min = float('inf')
                MinY = -1
                MinX = -1
                for i in range(8):
                    for j in range(8):
                        if SomeState.SanityChecks(i, j, 'H'):
                            newState = State(copy.deepcopy(State))
                            newState.Board[i][j] = 'H'
                            #print('Before Flipping in MIN MAX Min Level')
                            #newState.PrintState()
                            newState.FlipCells(i, j, 'H')
                            #print('After Flipping in MIN MAX Min Level')
                            #newState.PrintState()
                            #print(Depth)
                            res, resX, resY = self.MinMax(State(copy.deepcopy(newState)), Depth + 1, not IsMaxLevel)

                            if res > Min:
                                Min = res
                                MinX = i
                                MinY = j

                return Min, MinX, MinY

    def ComputerTurn(self):
        self.InLoop = self.CheckStale(self.InitialBoard, 'C')
        maxval, x, y = self.MinMax(self.InitialBoard, 0, True)
        print('Turn Taken By Computer')
        print(x)
        print(y)

        if self.InitialBoard.SanityChecks(x, y, self.Turn):
            self.MakeMove(x, y)
            self.InitialBoard.FlipCells(x, y, Turn=self.Turn)
            self.InLoop = self.CheckStale(self.InitialBoard, 'C')
            return True
        else:

            return False

    def CheckStale(self, state, Turn):
        for i in range(8):
            for j in range(8):
                if state.SanityChecks(i, j, Turn):
                    return True

        print('Game Jammed, No Move Left for')
        print('Computer' if Turn is 'C' else 'Human')

        return False

    def ToggleTurn(self):
        self.Turn = 'C' if self.Turn == 'H' else 'H'

    def MakeMove(self, x, y):
        self.InitialBoard.Board[x][y] = self.Turn

    def GetCount(self, Piece):
        count = 0
        for i in range(8):
            for j in range(8):
                if self.InitialBoard.Board[i][j] == Piece:
                    count += 1

        return count
