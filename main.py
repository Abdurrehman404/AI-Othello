from functools import partial
from tkinter import *
import Othelo as ot

game = ot.Othelo()

def click(x, y):
    print(x)
    print(y)
    try:
        if game.InitialBoard.SanityChecks(x, y, game.turn):
            game.MakeMove(x, y)
            obj = Grid.grid_slaves(x, y)
            obj = obj[0]
            obj.configure(background='#000000' if game.turn == 'H' else '#ffffff')
            print(game.InitialBoard.Board)
            game.ToggleTurn()

    except Exception as e:
        print(str(e))

def MakeCellAlive(event):
    print('Event fired')
    x = event.x_root - Grid.winfo_rootx()
    print(Grid.grid_size())


def MakeAGrid(Grid, X, Y):
    x = 0
    y = 0

    while x != X :
        while y != Y :
            Button(
            Grid,
            width = 7,
            height = 3,
            background = '#ffffff' if game.InitialBoard.Board[x][y] == 'C' else '#000000' if game.InitialBoard.Board[x][y] == 'H' else '#32d16f',
            command=partial(click, x, y),
            activebackground='#32d16f',
            borderwidth=0,
            ).grid(row = x, column = y, padx = 0.5, pady = 0.5)
            #btn.bind('<Button>', MakeCellAlive)

            y = y + 1
        x = x + 1
        y = 0

    Grid.mainloop()

if __name__ == '__main__':
    
    flag = [[0] * 8] * 8
    Grid = Tk()
    Grid.title('Othelo')
    Grid.geometry('458x435')
    Grid.config(bg='#073570')
    MakeAGrid(Grid, 8, 8)

    print(game.InitialBoard.Board)



