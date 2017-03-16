# Answer: umcvzsmw
from collections import Counter
INPUT_FILENAME = 'task_6_data.txt'

with open(INPUT_FILENAME, 'r') as f:
  data = f.readlines()
  data = list(zip(*data))
  for col in data:
    print(Counter(col).most_common(1)[0][0])
