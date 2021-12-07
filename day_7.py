import math

def part1(file):
  with open(file, 'r') as f:
    line = f.readline()
    crabs = line.strip().split(',')
    crabs = [int(num) for num in crabs]
    min_dist = math.inf
    for j in range(min(crabs), max(crabs) + 1):
      dist = 0
      for i in crabs:
        dist += abs(i-j)
      if dist < min_dist:
        min_dist = dist
    print(min_dist)

def arithematic_sum(n):
  return n * ( n + 1 ) / 2;

def part2(file):
  with open(file, 'r') as f:
    line = f.readline()
    crabs = line.strip().split(',')
    crabs = [int(num) for num in crabs]
    min_dist = math.inf
    for j in range(min(crabs), max(crabs) + 1):
      dist = 0
      for i in crabs:
        dist += arithematic_sum(abs(i-j))
      if dist < min_dist:
        min_dist = dist
    print(min_dist)
    

#part1('day7_data.txt')
part2('day7_data.txt')