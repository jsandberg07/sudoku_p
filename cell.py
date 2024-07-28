# represents a cell in the puzzle, and possible numbers it could be
# first boolian represents if it's solved. not necessary but makes indexing look cuter :^3
import debug

class Cell:
    def __init__(self, num):
        self.num = num
        self.possible = []
        self.row = None
        self.column = None
        self.block = None
        if num == 0:
            self.possible = [False, True, True, True, True, True, True, True, True, True]
        else:
            self.possible = [True, False, False, False, False, False, False, False, False, False]

    def add_list_to_cell(self, intrusive_list, region):
        if region == 'row':
            self.row = intrusive_list
        elif region == 'column':
            self.column = intrusive_list
        elif region == 'block':
            self.block = intrusive_list
        else:
            raise Exception("Invalid region passed to cell in add_list_to_cell")
        
    def solve_cell(self, num):
        self.num = num
        self.possible = [True, False, False, False, False, False, False, False, False, False]
        
    def is_solved(self):
        return self.possible[0]
    
    def check_if_impossible(self):
        if True not in self.possible[1:]:
            raise Exception("A cell was found to have 0 possibilies and be unsolved.")
        
    def check_for_solution(self):
        if self.possible[1:].count(True) == 1:
            self.num = self.possible.index(True)
            self.possible = [True, False, False, False, False, False, False, False, False, False]
            

    def remove_possibilities(self):
        self.remove_possibilities_h(self.row)
        self.remove_possibilities_h(self.column)
        self.remove_possibilities_h(self.block)

    def remove_possibilities_h(self, region):
        for cell in region:
            if not cell.is_solved():
                cell.possible[self.num] = False
    
    def __repr__(self):
        return f"{self.num}"
    
    


