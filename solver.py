import starter, GUI

board = GUI.get_board()
areas, squares, spaces = starter.start_game(board)

"""
Lower Square and Area take in a space and all the areas, and tell the areas that they've been filled with 
something with a value so they no longer need that value and the value is now impossible for them.

They also let the spaces with values know that everything else is impossible for them.
"""
    
def lower_area(space, areas):
    for area in areas.itervalues():
        if space.value != 0:
            for i in range(9):
                i = i+1
                if i != space.value:
                    space.make_impossible(i)
            if space.row == area.name[-1] or space.column == area.name[-1]:
                area.make_impossible(space.value)
                
def lower_square(space, squares):
    for square in squares.itervalues():
        if space.value != 0:
            for i in range(9):
                i = i+1
                if i != space.value:
                    space.make_impossible(i)
            if space.column in square.columns and space.row in square.rows:
                    square.make_impossible(space.value)

"""
lower_space takes in the dictionaries that make up the boards
and matches each space.impossible with the area it is in's 
area.impossible(also does it for squares). Also updates the 
space.possible with the same information. 

Finally, it checks if every number but a certain number is 
impossible for a space. If that's the case, it sets the certian 
number as the number in the space.
"""
                
def lower_space(spaces, areas, squares):
    for space in spaces.itervalues():
        if space.value == 0:
            for area in areas.itervalues():
                if space.row == area.name[-1]: #If the area is a row
                    for value in area.impossible: # for values that are already in the area
                        space.make_impossible(value)
                if space.column == area.name[-1]: # If the area is a column
                    for value in area.impossible:
                        space.make_impossible(value)
            for square in squares.itervalues():
                if space.row in square.rows and space.column in square.columns: # if the space is in that square
                    for value in square.impossible:
                        space.make_impossible(value)
        if len(space.impossible) == 8:
            for i in range(9):
                i = i+1
                if i not in space.impossible:
                    space.value = i
                    space.possible = i

# find_brother_spacesn finds and returns the brother columns and rows for whatever space
# brother columns/rows are the columns and rows that are in the same big square as whichever square. 
# Column B and C and Row 2 and 3 for A1
def find_brother_spaces(space):
    brother_rows = []
    brother_columns = []
    for square in squares.itervalues():
        if space.row in square.rows and space.column in square.columns:
            brother_rows = square.rows[:]
            brother_columns = square.columns[:]
            brother_rows.remove(space.row)
            brother_columns.remove(space.column)
    return brother_rows, brother_columns
#This function see's if all the other 8 spots in a brother column/row are full
def get_rid_of_impossibles(bros, space):
    for num in range(9):
        num = num+1
        count = 0
        for bro in bros:
            if num in bro.impossible:
                count = count + 1
            if count == 8:
                space.value = num   

def rows_and_coloums(space, squares, areas):
    square_bros = []
    column_bros = []
    row_bros = []
    brother_rows, brother_columns = find_brother_spaces(space)
    for other_space in spaces.itervalues():
        if other_space.row == space.row and other_space.column != space.column:
            row_bros.append(other_space)
        if other_space.column == space.column and other_space.row != space.row:
            column_bros.append(other_space)
        if (other_space.row in brother_rows and other_space.column == space.column) or (other_space.column in brother_columns and other_space.row == space.row) or (other_space.row in brother_rows and other_space.column in brother_columns):
            square_bros.append(other_space)

    get_rid_of_impossibles(square_bros, space)
    get_rid_of_impossibles(row_bros, space)
    get_rid_of_impossibles(column_bros, space)
    

def solve(spaces, areas, squares):
    for space in spaces.itervalues():
        lower_area(space, areas)
    for space in spaces.itervalues():
        lower_square(space, squares)
    lower_space(spaces, areas, squares)
    for space in spaces.itervalues():
        rows_and_coloums(space, squares, areas)
    for space in spaces.itervalues():
        if type(space.possible) == list and len(space.possible) == 1:
                space.value = int(space.possible[0])



lastdone = 0
first_time = True

while True:
    solve(spaces, areas, squares)
    done = 0
    for space in spaces.itervalues():
        if space.value != 0:
            done = done + 1
    
    if done == lastdone: #If nothing changed, meaning the game is either solved or the program cannot solve it
        if first_time:  #But it has to go through the same thing twice.
            first_time = False
        else:
            break
    else: 
        lastdone = done
        first_time = True

GUI.show_board(spaces)
