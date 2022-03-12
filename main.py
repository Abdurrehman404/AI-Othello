from tkinter import *

def MakeCellAlive(List,Grid,x,y):
    List[x][y] = 1

def MakeAGrid(List,Grid,X,Y):
    x=0
    y=0

    while ( x != X ):
        while( y != Y ):
            Button(
            Grid,
            width = 7,
            height = 3,
            activebackground ='#03fc6f',
            background='#03fc6f',
            command = MakeCellAlive(List,Grid,x,y)
            ).grid( row = x, column = y , padx = 2 , pady = 2 )
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
    MakeAGrid(flag, Grid, 8, 8)
