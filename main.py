from puzzle_state import Puzzle_State
from cell import Cell
import csv


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

def main():
    cell_list = read_input()
    if cell_list == 1:
        return
    print("// imported cell list")
    ps = Puzzle_State(cell_list)
    write_output(cell_list)

main()