"""
So these classes represent spaces(the small squares), areas
(the rows and columns) and squares( the 3x3 squares). Squares
is a subclass of area.

Each space has possible values, and impossible values, which are updated
with the function make_impossible.
The space.names are string like "A1" and "G4"

Areas have things they need and things that are impossibe (what they already
have).
area.names are strings like "ColumnD" and "Row2"

Squares are made by making the intersection of 3 rows and 3 columns.
square.names are strings like "Square1" and "Square9" going from left to right, up and down.
"""
class space:
    def __init__(self, spacename, column, row, value):
        self.name = spacename
        self.value = value
        self.row = str(row)
        self.column = column
        self.impossible = []
        if self.value == 0:
            self.possible = [1,2,3,4,5,6,7,8,9]
        else:
            self.possible = self.value

    def make_impossible(self, value):
        if type(self.possible) == list: #if it's not a list, it's an int, so we already know the value
            if value in self.possible:
                self.possible.remove(value)
        if value not in self.impossible:
            self.impossible.append(value)
class area:
    def __init__(self, name):
        self.name = name
        self.need = [1,2,3,4,5,6,7,8,9]
        self.impossible = []

    def make_impossible(self, value):
        if value in self.need:
            self.need.remove(value)
        if value not in self.impossible:
            self.impossible.append(value)

class square(area):
    def set_columns_and_rows(self):        
             
        left_columns = ["A", "B", "C"]
        center_columns = ["D", "E", "F"]
        right_columns = ["G", "H", "I"]
        
        top_rows = ["1","2","3"]
        middle_rows = ["4","5","6"]
        bottom_rows = ["7","8","9"]
        
        if self.name[-1] == "1":
            self.columns = left_columns
            self.rows = top_rows
            
        elif self.name[-1] == "2":
            self.columns = center_columns
            self.rows = top_rows
            
        elif self.name[-1] == "3":
            self.columns = right_columns
            self.rows = top_rows
            
        elif self.name[-1] == "4":
            self.columns = left_columns
            self.rows = middle_rows
            
        elif self.name[-1] == "5":
            self.columns = center_columns
            self.rows = middle_rows
            
        elif self.name[-1] == "6":
            self.columns = right_columns
            self.rows = middle_rows
            
        elif self.name[-1] == "7":
            self.columns = left_columns
            self.rows = bottom_rows
      
        elif self.name[-1] == "8":
            self.columns = center_columns
            self.rows = bottom_rows
     
        elif self.name[-1] == "9":
            self.columns = right_columns
            self.rows = bottom_rows
        else:
            print "how"

            
