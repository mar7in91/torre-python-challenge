import numpy as np

## This method is is used to get quadrant number. row and col are digits in a 'base-3' convertion
def GetQuadrantNumber(quad_row, quad_col):
  return str(quad_row * 3 + quad_col + 1)

def GetSubGrid(sudoku, r, c):
  return sudoku[(r // 3 * 3):(r // 3 * 3 + 3), (c // 3 * 3):(c // 3 * 3 + 3)]

def MatrixChallenge(sudoku):
  ## Extract each value from string array and the convert to a matrix
  ## to use numpy methods in order to read columns and rows easily.
  parsed_sudoku = [x.replace("(", "").replace(")", "").split(",") for x in sudoku]
  quadrants_with_errors = []
  matrix = np.array(parsed_sudoku) # Parse to numpy array

  ## Run over the matrix elements
  for r in range(9):
    for c in range(9):
      if matrix[r][c] == "x": # Ignore 'x' values
        continue
      if (np.count_nonzero(matrix[r, :] == matrix[r][c]) > 1 or ## Evaluate over row r
        np.count_nonzero(matrix[:, c] == matrix[r][c]) > 1 or ## Evaluate over column c
        np.count_nonzero(GetSubGrid == matrix[r][c]) > 1): ## Evaluate over sub-grid
        quadrants_with_errors.append(GetQuadrantNumber(r // 3, c // 3))
  
  return ",".join(quadrants_with_errors)

# keep this function call here 
print MatrixChallenge(raw_input())