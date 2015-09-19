import Tkinter
from starter import numbers_to_letters
# Creates the GUI for the board before the game

root = Tkinter.Tk()

canvas = Tkinter.Canvas(root, width = 550, height = 550)
canvas.grid()

for i in range(9):
    for j in range(9):
        column = j+1
        v = Tkinter.StringVar()
        name = numbers_to_letters[column] + str(i+1) 
        print name
        name = Tkinter.Entry(canvas, width =4 , textvariable = v)
        name.grid(row = i, column = j)

root.mainloop()
