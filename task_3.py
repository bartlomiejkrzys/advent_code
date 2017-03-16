INPUT_FILENAME = 'task_3_data.txt'

## Part 1
# Answer: 1032
def valid_triangle(a, b, c):
  return a + b > c and a + c > b and b + c > a

count = 0
with open(INPUT_FILENAME, 'r') as f:
  for line in f.readlines():
    if valid_triangle(*list(map(int, line.split()))):
      count += 1
print(count)

## Part 2
# Answer: 1838
count = 0
with open(INPUT_FILENAME, 'r') as f:
  lines = list(map(str.split, f.readlines()))
  for idx in range(0, len(lines), 3):
    for triangle in zip(*lines[idx: idx + 3]):
      if valid_triangle(*map(int, triangle)):
        count += 1
print(count)
    
  
