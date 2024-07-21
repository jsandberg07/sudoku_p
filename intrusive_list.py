class Intrusive_List:
    def __init__(self, n, region):
        self.id = (n, region)
        self.intrusive_list = []

    def add_cells_to_list(self, region, cell_1, cell_2, cell_3, cell_4, cell_5, cell_6, cell_7, cell_8, cell_9):
        self.intrusive_list = [cell_1, cell_2, cell_3, cell_4, cell_5, cell_6, cell_7, cell_8, cell_9]
        for cell in self.intrusive_list:
            cell.add_list_to_cell(self.intrusive_list, region)


