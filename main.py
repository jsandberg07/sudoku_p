import csv
from cell import Cell
from intrusive_list import assign_cells_to_lists
from debug import print_possibilities

def create_template():
    blank_template = []
    blank_row = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    # TODO: sudoku puzzles have a fixed size. Don't bother with loops, just type it out.
    # TODO: is it easier to just have the commas? like fr overwriting zeros sucks
    for row in range(0, 9):
        blank_template.append(blank_row)

    file_path = 'sudoku.csv'
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(blank_template)

def read_input():
    try:
        node_list = []
        with open('sudoku.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                row_list = []
                for num in row:
                    if num != '':
                        #TODO: handle numbers outside of range, handle characters
                        row_list.append(Cell(int(num)))
                node_list.append(row_list)
        return node_list
    except:
        print("No input found. Creating template.")
        create_template()
        return 1
    
def write_output(cell_list):
    file_path = 'output.csv'
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(cell_list)

def print_cell_list(cell_list):
    for n in cell_list:
        print(n)

def solve(cell_list):
    passes = 0
    max_passes = 20
    while passes < max_passes:
        for i in range(0, 9):
            for j in range(0, 9):
                if cell_list[i][j].is_solved():
                    cell_list[i][j].remove_possibilities()

        passes += 1
        if check_if_solved(cell_list):
            break

    if passes == max_passes:
        print(f"Stopping after {passes} passes. Check the result.")
    else:
        print(f"Took {passes} passes to solve linearly")


def check_if_solved(cell_list):
    for i in range(0, 9):
        for j in range(0, 9):
            if cell_list[i][j].is_solved() == False:
                return False
    return True    
    


def main():
    cell_list = read_input()
    assign_cells_to_lists(cell_list)

    
    print_cell_list(cell_list)
    solve(cell_list)
    print("//")
    print_cell_list(cell_list)
    
    # print_cell_list(cell_list)
    write_output(cell_list)

main()