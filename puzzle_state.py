from intrusive_list import Intrusive_List

class Puzzle_State:
    def __init__(self, cell_list):
        print("// creating puzzle state")
        self.cell_list = cell_list
        self.rows = []
        self.columns = []
        self.blocks = []
        self.assign_cells_to_lists()
        self.print_cell_list()
        self.solve()
        self.print_cell_list()

    def check_if_solved(self):
        for i in range(0, 9):
            for j in range(0, 9):
                if self.cell_list[i][j].is_solved() == False:
                    return False
        return True       
    
    # the most basic form of solving
    # remove possibilities from related cells and check for solution
    def linear_pass(self):
        for i in range(0, 9):
                for j in range(0, 9):
                    if self.cell_list[i][j].is_solved():
                        self.cell_list[i][j].remove_possibilities()

    def remove_possibilities(self):
        for i in range(0, 9):
                for j in range(0, 9):
                    if self.cell_list[i][j].is_solved():
                        self.cell_list[i][j].remove_possibilities()

    def check_for_solutions(self):
        for i in range(0, 9):
                for j in range(0, 9):
                    if self.cell_list[i][j].is_solved() == False:
                        self.cell_list[i][j].check_for_solution()

    # checks all of a group to see if only 1 cell can have a certain number
    # then sets those cells
    def last_in_list_pass(self):
        # blocks
        print("// blocks")
        if self.last_in_list_pass_h(self.blocks) == True:
            return
        # rows
        print("// rows")
        if self.last_in_list_pass_h(self.rows) == True:
            return
        # columns
        print("// columns")
        if self.last_in_list_pass_h(self.columns) == True:
            return

    def last_in_list_pass_h(self, list_of_intrusive_lists):
        # for each number, count the number of cells that may have that result
        change_made = False
        for intrusive_list in list_of_intrusive_lists:
            list_of_possibilites = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for cell in intrusive_list.intrusive_list:
                for possibility in range(1, 9):
                    if cell.possible[possibility]:
                        list_of_possibilites[possibility] += 1

            # iterate through the list and for each 1, find the cell that has that same possibility and solve it
            for possibility in range(1, 9):
                if list_of_possibilites[possibility] == 1:
                    change_made = True
                    print("// last in list found!")
                    print(f"// {list_of_possibilites}")
                    for cell in intrusive_list.intrusive_list:
                        if cell.possible[possibility] == True:
                            print(f"// marking a cell as {possibility}")
                            cell.num = possibility
                            print(f"// here are the cells possibilities: ")
                            print(f"// {cell.possible}")
                            cell.possible = [True, False, False, False, False, False, False, False, False, False]
                            cell.remove_possibilities()
                            return change_made
        return change_made

    def solve(self):
        passes = 0
        max_passes = 100
        while passes < max_passes:
            self.remove_possibilities()
            self.check_for_solutions()
            self.print_cell_list()
            print("/// linear pass complete")
            self.remove_possibilities()
            self.last_in_list_pass()
            print("/// last in list pass complete")
            self.print_cell_list()
            print("// passes complete")
            print("// ")

            passes += 1
            if self.check_if_solved():
                break

        if passes == max_passes:
            print(f"Stopping after {passes} passes. Check the result.")
        else:
            print(f"Took {passes} passes to solve linearly")

         
    def assign_cells_to_lists(self):
    # row
        region = 'row'
        for n in range(0, 9):
            intrusive_list = Intrusive_List(n, region)
            self.rows.append(intrusive_list)
            intrusive_list.add_cells_to_list(region, self.cell_list[n][0], self.cell_list[n][1], self.cell_list[n][2], 
                                            self.cell_list[n][3], self.cell_list[n][4], self.cell_list[n][5], 
                                            self.cell_list[n][6], self.cell_list[n][7], self.cell_list[n][8])


        # column
        region = 'column'
        for n in range(0, 9):
            intrusive_list = Intrusive_List(n, region)
            self.columns.append(intrusive_list)
            intrusive_list.add_cells_to_list(region, self.cell_list[0][n], self.cell_list[1][n], self.cell_list[2][n], 
                                            self.cell_list[3][n], self.cell_list[4][n], self.cell_list[5][n], 
                                            self.cell_list[6][n], self.cell_list[7][n], self.cell_list[8][n])
  

        # blocks
        region = 'block'
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                intrusive_list = Intrusive_List(i, region)
                self.blocks.append(intrusive_list)
                intrusive_list.add_cells_to_list(region, self.cell_list[i][j], self.cell_list[i][j+1], self.cell_list[i][j+2], 
                                                self.cell_list[i+1][j], self.cell_list[i+1][j+1], self.cell_list[i+1][j+2], 
                                                self.cell_list[i+2][j], self.cell_list[i+2][j+1], self.cell_list[i+2][j+2])


    def print_cell_list(self):
        for n in self.cell_list:
            print(n)

    