from functools import partial
from tkinter import *
import Othelo as ot

def click(x, y):
    print(x)
    print(y)
    try:
       obj = Grid.grid_slaves(x, y)
       obj = obj[0]
       print(obj)
       obj.configure(background='#01ac6f')

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
            background='#03fc6f',
            command=partial(click,x,y)
            ).grid(row = x, column = y, padx = 2, pady = 2)
            #btn.bind('<Button>', MakeCellAlive)

            y = y + 1
        x = x + 1
        y = 0

    Grid.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    
    flag = [[0] * 8] * 8
    Grid = Tk()
    Grid.title('Othelo')
    Grid.geometry('505x480')
    Grid.config(bg='#073570')
    MakeAGrid(Grid, 8, 8)

    game1 = ot.Othelo()


