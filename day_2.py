def part1(file):
  horizontal = 0
  depth = 0
  with open(file, 'r') as f:
    lines = f.readlines()
    for line in lines:
      temp = line.strip().split()
      value = int(temp[1])
      if temp[0] == 'forward':
        horizontal += value
      elif temp[0] == 'down':
        depth += value
      elif temp[0] == 'up':
        depth -= value

  return (depth * horizontal)

def part2(file):
  horizontal = 0
  depth = 0
  aim = 0
  with open(file, 'r') as f:
    lines = f.readlines()
    for line in lines:
      temp = line.strip().split()
      value = int(temp[1])
      if temp[0] == 'down':
        aim += value
      elif temp[0] == 'up':
        aim -= value
      elif temp[0] == 'forward':
        horizontal += value
        depth += (value * aim)

  return (depth * horizontal)  

#print(part1('day2_directions.txt'))
print(part2('day2_directions.txt'))