"""
The solver works by first "creating" 
the board from a list of tuples in the
form (Column, Row, Value) with zero in 
the value meaning the space is empty. 
The board is contained within a dictionary
called spaces that contains the name of the
square in the form ColumnRow (e.g A1) with 
the key being mapped to a value that's an 
instance of the custom made class space,
with the attributes row, column, value, name,
impossible, and possible. The starter.py file
also creates the areas the board will work with
namely the columns, rows, and squares. 

The game begins...
"""

import classes
numbers_to_letters = {1:"A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"F", 7:"G", 8:"H", 9:"I"}


def start_game(board):
    areas, squares, spaces = {}, {}, {}
    def create_board(board):
        for space in board:
            column, row, value = space
            spacename = (column+str(row))
            spaces[spacename] = classes.space(spacename, column, row, value)
    
    def create_areas():
        for i in range(9):
            row_name = "Row" + str(i+1) 
            areas[row_name] = classes.area(row_name)
            column_name = "Column" + numbers_to_letters[i+1] 
            areas[column_name] = classes.area(column_name)
            square_name = "Square" + str(i+1)
            squares[square_name] = classes.square(square_name)
    

                
            
    create_board(board)
    create_areas()
    for square in squares.itervalues():
        square.set_columns_and_rows()

    return areas, squares, spaces

