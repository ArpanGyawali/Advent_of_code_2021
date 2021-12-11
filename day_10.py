import collections

def part1(file):
  with open(file, 'r') as f:
    lines = f.readlines()
    matrix = [line.strip() for line in lines]
    new_len = len(matrix) + 2
    new_matrix = [None] * new_len
    new_matrix[0] = '9' * new_len
    for i in range(len(matrix)):
      new_matrix[i+1] = '9' + matrix[i] + '9'
    new_matrix[101] = '9' * new_len
    print(new_matrix)
    count = 0
    sum_risk_level = 0
    low = []
    for i in range(1, new_len-1):
      for j in range(1, new_len-1):
        adjacent = [new_matrix[i-1][j], new_matrix[i+1][j], new_matrix[i][j-1], new_matrix[i][j+1]]
        adjacent.sort()
        #smallest num in sorted list of adjacent nums is adjacent[0]
        if new_matrix[i][j] < adjacent[0]:   
          print(new_matrix[i][j], adjacent)
          low.append((i,j))
          count += 1
          sum_risk_level += int(new_matrix[i][j]) + 1

    print(count)
    print(sum_risk_level)
    print('\n\n\n\n\n\n\n\n')
    return low, new_matrix


      

def part2(file):
  with open(file, 'r') as f:
    low, new_matrix = part1(file)

    # Do some BFS
    size_array = []
    visited = set()
    for row, col in low:
      if (row, col) not in visited:
        size = 0
        Q = collections.deque()
        Q.append((row, col))
        while Q:
          (r, c) = Q.popleft()
          if (r,c) in visited:
            continue
          visited.add((r,c))
          size += 1
          for neighbour in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            rr = r + neighbour[0]
            cc = c + neighbour[1]
            if int(new_matrix[rr][cc]) != 9:
              Q.append((rr, cc))
        size_array.append(size)
    
    size_array.sort()
    print(size_array)
    print(size_array[-1] * size_array[-2] * size_array[-3])
            

#part1('day9_data.txt')
part2('day9_data.txt')