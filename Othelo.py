
class Othelo:

    def __init__(self):
        self.turn = 'C'

    turn = 'C'  # H for Human, C for Computer

    def MinMax(self):
        pass


class State:
    def __init__(self):
        pass

    Board = [['W' for i in range(8)]for j in range(8)]

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

    def SanityChecks(self, i, j, Turn):
        Piece = 'H' if Turn == 'C' else 'C'  # that sprite that is inbetween the turn's Piece


    def InEightMoves(self, SRow, SCol, Row, Col):
        return ((SRow != Row and SCol != Col) and ((SRow == Row and SCol != Col)
                or (SCol == Col and SRow != Row)
                or (abs(SRow-Row) == abs(SCol-Col))))

    def MakeMove(self):
        pass


