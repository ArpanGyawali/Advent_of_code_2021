def part1(file):
  grid = [[0 for j in range(1000)] for k in range(1000)]
  with open(file, 'r') as f:
    lines = f.readlines()
    lines = [l.replace(" -> ", ",").strip().split(',') for l in lines]
    for i in range(len(lines)):
      y1 = int(lines[i][1])
      x2 = int(lines[i][2])
      x1 = int(lines[i][0])
      y2 = int(lines[i][3])
      if x1>x2:
        x1,x2 = x2,x1
      if y1>y2:
        y1,y2 = y2,y1
      if y1 == y2:    #horizontal line
        for x in range(x1, x2+1):
          grid[x][y1] += 1
      elif x1 == x2:  #vertical line
        for y in range(y1, y2+1):
          grid[x1][y] += 1
    
    count = 0
    for i in range(1000):
      for j in range(1000):
        if grid[i][j] > 1:
          count += 1
    print(count)

  

def part2(file):
  grid = [[0 for j in range(1000)] for k in range(1000)]
  with open(file, 'r') as f:
    lines = f.readlines()
    lines = [l.replace(" -> ", ",").strip().split(',') for l in lines]
    for i in range(len(lines)):
      x1 = int(lines[i][0])
      y1 = int(lines[i][1])
      x2 = int(lines[i][2])
      y2 = int(lines[i][3])
      if x1>x2:
        x1,x2 = x2,x1
        y1,y2 = y2,y1
      diff1 = x2 - x1
      diff2 = y2 - y1
      if diff1 == diff2:
        for x,y in zip(range(x1,x2+1), range(y1, y2+1)):
          grid[x][y] += 1
      elif diff1 == -diff2:
        for x,y in zip(range(x1,x2+1), range(y1, y2-1, -1)):
          grid[x][y] += 1 
      elif y1 == y2:    #horizontal line
        for x in range(x1, x2+1):
          grid[x][y1] += 1
      elif x1 == x2:  #vertical line
        if y1 > y2:
          y1,y2 = y2,y1
        for y in range(y1, y2+1):
          grid[x1][y] += 1

    count = 0
    for i in range(1000):
      for j in range(1000):
        if grid[i][j] > 1:
          count += 1
    print(count)


#part1('day5_data.txt')
part2('day5_data.txt')