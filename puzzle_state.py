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

    # get cell list from main
    # create lists
    # assign cells to lists
    # solve
    # new method

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

    # checks all of a group to see if only 1 cell can have a certain number
    # then sets those cells
    def last_in_list_pass(self):
        # rows
        self.last_in_list_pass_h(self.rows)
        # columns
        self.last_in_list_pass_h(self.columns)
        # blocks
        self.last_in_list_pass_h(self.blocks)

    def last_in_list_pass_h(self, intrusive_list):
        # the first index does nothing :^3 i just like cuter indexes
        # it is also causing a lot of headaches kek
        for sub_list in intrusive_list:
            possibility_sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            current_list = sub_list.intrusive_list
            for cell in current_list:
                for i in range(0, 10):
                    if cell.possible[i] == True:
                        possibility_sum[i] += 1
            # if only 1 cell has the possibility to be a certain number
            print(f"// possibility sum: {possibility_sum}")
            if 1 in possibility_sum[1:9]:
                # have to search the cells for whichever one has that particular possibility
                # and set it to being solved
                # then loop again
                print(f"// a 1 was found in the PS")
                solution = possibility_sum[1:9].index(1)
                print(f"// setting a cell in the list to {solution}")
                for cell in current_list:
                    if cell.possible[solution] == True:
                        print(f"// here's the possible list for the cell")
                        print(f"// {cell.possible}")
                        cell.num = solution
                        cell.possible = [True, False, False, False, False, False, False, False, False, False]
                        break
            

    def solve(self):
        passes = 0
        max_passes = 20
        while passes < max_passes:
            self.linear_pass()
            # self.last_in_list_pass()
            

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

    