import Tkinter, tkFont
from starter import numbers_to_letters
def make_board(board):
    for i in range(8):
        i = i+1
        line = board.create_line(i*50,100,i*50,600)
        line = board.create_line(0,(i*50)+100, 450,(i*50)+100)
    for i in range(2):
        i = i+1
        line = board.create_line(0,99+i*150, 450, 99+i*150)
        line = board.create_line(0,101+i*150, 450, 101+i*150) 
        line = board.create_line(-1+i*150, 100, -1+i*150, 550)
        line = board.create_line(1+i*150, 100, 1+i*150, 550)

"""
get_board uses the make_board function to open up the GUI, and 
links a text box with a name (it puts them in the dict
space_values). Then, it uses retrieve, which is called by the
button, and returns a list of tuples in the form (Column, Row, Value)
"""

def get_board():
    top = Tkinter.Tk()
    board = Tkinter.Canvas(top, width = 450, height = 550, bg = "white")
    top_line = board.create_line(0,100,450,100)
    font = tkFont.Font(size = 18)
    space_values = {}
    game_board = []

    make_board(board)

    for i in range(9):
        i = i+1
        for j in range(9):
            j = j+1
            name = numbers_to_letters[i]+str(j)
            space = Tkinter.Entry(top, width = 1, font = font)
            space.place(x = (i-1)*50+15, y = (j-1)*50+110)
            space_values[name] = space
            



    def retrieve():
        for name, value in space_values.iteritems():
            if value.get() == "":
                game_board.append((name[0], int(name[1]), 0))
            else:
                game_board.append((name[0], int(name[1]), int(value.get())))
        top.destroy()

    b = Tkinter.Button(board, text="Solve", command = retrieve)
    b.place(x = 195, y = 50)


    board.pack()
    top.mainloop()

    return game_board

def show_board(spaces):
    top = Tkinter.Tk()
    board = Tkinter.Canvas(top, width = 450, height = 550, bg = "white")
    top_line = board.create_line(0,100,450,100)
    font = tkFont.Font(size = 18)

    make_board(board)
    for i in range(9):
        i = i+1
        for j in range(9):
            j = j+1
            number = spaces[numbers_to_letters[i]+str(j)].value
            space = Tkinter.Label(top, text = number, font = font)

            space.place(x = (i-1)*50+15, y = (j-1)*50+110)
    board.pack()
    top.mainloop()

