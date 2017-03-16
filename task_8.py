# Answer: 106
import numpy as np
import re
rotate_pat = r"rotate (row|column) [xy]=(\d+) by (\d+)"
rect_pat = r"rect (\d*)x(\d*)"
INPUT_FILENAME = 'task_8_data.txt'

width, height = 50, 6
screen = np.array([['.'] * width for _ in range(height)])

def rectangle(array, r, c, mark = "X"):
  array[:c, :r] = mark

def rotate_col(array, col_idx, by):
    array[:, col_idx] = np.roll(array[:, col_idx], by)
    
def rotate_row(array, row_idx, by):
    array[row_idx] = np.roll(array[row_idx], by)

with open(INPUT_FILENAME, 'r') as f:
  for i, inst in enumerate(f.readlines()):
    if inst.startswith('rect'):
      x, y = re.search(rect_pat, inst).groups()
      rectangle(screen, int(x), int(y))
    else:
      what, idx, by = re.search(rotate_pat, inst).groups()
      idx, by = int(idx), int(by)
      if what == 'column':
        rotate_col(screen, idx, by)
      elif what == 'row':
        rotate_row(screen, idx, by)

for r in screen:
  print(''.join(r))

# Number of occurences
print(np.sum(screen == 'X'))
