from functools import partial
from tkinter import *
import Othello as ot

game = ot.Othelo()

def click(x, y):
    print(x)
    print(y)
    try:
        if game.InitialBoard.SanityChecks(x, y, game.Turn):
            game.MakeMove(x, y)
            game.PrintState()
            game.FlipCells(x, y)
            UpdateBoard()
            game.PrintState()
            BlackCount.configure(text=game.GetCount('H'))
            WhiteCount.configure(text=game.GetCount('C'))
            game.ToggleTurn()
            TurnLabel.configure(text='Computer(White)' if game.Turn == 'C' else 'Human(Black)',
                                background='#ffffff' if game.Turn == 'C' else '#000000')
            TurnLabel.update()

    except Exception as e:
        print(str(e))

def UpdateBoard():
    for i in range(8):
        for j in range(8):
            obj = Grid.grid_slaves(i, j)
            obj = obj[0]
            obj.configure(background='#000000' if game.InitialBoard.Board[i][j] == 'H' else (
                '#ffffff' if game.InitialBoard.Board[i][j] == 'C' else '#32d16f'))

def MakeCellAlive(event):
    print('Event fired')
    x = event.x_root - Grid.winfo_rootx()
    print(Grid.grid_size())


def MakeAGrid(Grid, X, Y):
    x = 0
    y = 0

    while x != X:
        while y != Y:
            Button(
            Grid,
            width=7,
            height=3,
            background='#ffffff' if game.InitialBoard.Board[x][y] == 'C' else '#000000' if game.InitialBoard.Board[x][y] == 'H' else '#32d16f',
            command=partial(click, x, y),
            activebackground='#32d16f',
            borderwidth=0,
            ).grid(row=x, column=y, padx=0.5, pady=0.5)

            y = y + 1
        x = x + 1
        y = 0

    Grid.mainloop()

if __name__ == '__main__':
    
    flag = [[0] * 8] * 8
    Grid = Tk()

    TurnLabel = Label(
        Grid,
        width=15,
        height=2,
        background='#ffffff' if game.Turn == 'C' else '#000000',
        activebackground='#32d16f',
        borderwidth=0,
        foreground='#af1254',
        text='Computer(White)' if game.Turn == 'C' else 'Human(Black)',
        font=10,
    )
    TurnLabel.grid(row=8, column=0, padx=0, pady=10, rowspan=3, columnspan=3)

    BlackCount = Label(
        Grid,
        width=5,
        height=2,
        background='#ffffff' if game.Turn == 'C' else '#000000',
        activebackground='#32d16f',
        borderwidth=0,
        foreground='#af1254',
        text=game.GetCount('H'),
        font=10,
    )
    BlackCount.grid(row=8, column=4, padx=0, pady=10, rowspan=3, columnspan=3)

    WhiteCount = Label(
        Grid,
        width=5,
        height=2,
        background='#ffffff',
        borderwidth=0,
        foreground='#af1254',
        text=game.GetCount('H'),
        font=10,
    )
    WhiteCount.grid(row=8, column=5, padx=0, pady=10, rowspan=3, columnspan=3)


    Grid.title('Othello')
    Grid.geometry('458x490')
    Grid.config(bg='#073570')
    MakeAGrid(Grid, 8, 8)

    print(game.InitialBoard.Board)



