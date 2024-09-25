from sudoku import Sudoku

puzzle_board = [[3,0,0,0,5,0,6,0,8],
                [0,2,8,3,0,0,0,0,0],
                [1,0,0,0,0,0,0,5,0],
                [0,0,2,9,0,0,4,6,0],
                [0,0,1,0,0,0,0,0,0],
                [0,0,3,0,6,4,0,0,1],
                [0,0,0,6,0,0,5,0,0],
                [0,0,0,0,1,0,3,0,0],
                [9,0,0,7,4,0,0,0,0]]

puzzle = Sudoku(3,3,board=puzzle_board)
solution = puzzle.solve(raising=True)
print(solution)

