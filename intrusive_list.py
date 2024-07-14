class Intrusive_List:
    def __init__(self, n, region):
        self.id = (n, region)
        self.intrusive_list = []

    def add_cells_to_list(self, region, cell_1, cell_2, cell_3, cell_4, cell_5, cell_6, cell_7, cell_8, cell_9):
        self.intrusive_list = [cell_1, cell_2, cell_3, cell_4, cell_5, cell_6, cell_7, cell_8, cell_9]
        for cell in self.intrusive_list:
            cell.add_list_to_cell(self.intrusive_list, region)


def assign_cells_to_lists(cell_list):
    # row
    region = 'row'
    for n in range(0, 9):
        intrusive_list = Intrusive_List(n, region)
        intrusive_list.add_cells_to_list(region, cell_list[n][0], cell_list[n][1], cell_list[n][2], 
                                          cell_list[n][3], cell_list[n][4], cell_list[n][5], 
                                          cell_list[n][6], cell_list[n][7], cell_list[n][8])
    # column
    region = 'column'
    for n in range(0, 9):
        intrusive_list = Intrusive_List(n, region)
        intrusive_list.add_cells_to_list(region, cell_list[0][n], cell_list[1][n], cell_list[2][n], 
                                          cell_list[3][n], cell_list[4][n], cell_list[5][n], 
                                          cell_list[6][n], cell_list[7][n], cell_list[8][n])

    # blocks
    region = 'block'
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            intrusive_list = Intrusive_List(i, region)
            intrusive_list.add_cells_to_list(region, cell_list[i][j], cell_list[i][j+1], cell_list[i][j+2], 
                                              cell_list[i+1][j], cell_list[i+1][j+1], cell_list[i+1][j+2], 
                                              cell_list[i+2][j], cell_list[i+2][j+1], cell_list[i+2][j+2])