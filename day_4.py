def part1(file):
  win_num = 0
  sum_unchecked = 0
  with open(file, 'r') as f:
    lines = f.readlines()

    #forming a 3*3 array of all bingo blocks
    extracted = [line for line in lines if line.strip() != '']
    numbers = extracted[0].split(',')
    for l in range(0, len(extracted)):
      extracted[l] = extracted[l].split()
    blocks = []
    for i in range(1, len(extracted), 5):
      block = [[0 for j in range(5)] for k in range(5)]
      for j in range(5):
        for k in range(5):
          block[j][k] = extracted[i+j][k]
      blocks.append(block)
    

    #playing bingo
    break_out_flag = False
    for num in numbers:
      for i in range(len(blocks)):
        for j in range(5):
          for k in range(5):
            if blocks[i][j][k] == num:
              blocks[i][j][k] = 0
              current = blocks[i]
              row = blocks[i][j]
              column = [row[k] for row in current]

              #bingoooooooooooooo
              if all(v == 0 for v in row) or all(u == 0 for u in column):
                win_num = int(num)
                print(current, i)
                print(win_num)
                for a in range(5):
                  for b in range(5):
                    sum_unchecked += int(current[a][b])

                print(sum_unchecked)
                break_out_flag = True
                break
          if break_out_flag:
            break
        if break_out_flag:
          break
      if break_out_flag:
        break
    
  return sum_unchecked * win_num
            



    

def part2(file):
  win_num = 0
  sum_unchecked = 0
  with open(file, 'r') as f:
    lines = f.readlines()

    #forming a 3*3 array of all bingo blocks
    extracted = [line for line in lines if line.strip() != '']
    numbers = extracted[0].split(',')
    for l in range(0, len(extracted)):
      extracted[l] = extracted[l].split()
    blocks = []
    for i in range(1, len(extracted), 5):
      block = [[0 for j in range(5)] for k in range(5)]
      for j in range(5):
        for k in range(5):
          block[j][k] = extracted[i+j][k]
      blocks.append(block)
    

    #playing bingo
    break_out_flag = False
    won_blocks = [] #for finding last win
    no_of_blocks = len(blocks)
    for num in numbers:
      for i in range(no_of_blocks):
        for j in range(5):
          for k in range(5):
            if blocks[i][j][k] == num:
              blocks[i][j][k] = 0
              current = blocks[i]
              row = blocks[i][j]
              column = [row[k] for row in current]

              #bingoooooooooooooo
              if all(v == 0 for v in row) or all(u == 0 for u in column):      
                won_blocks.append(i)  
                won_blocks_Set = set(won_blocks)    #non repeating winners
                if len(won_blocks_Set) == len(blocks):  #last win
                  for a in range(5):
                    for b in range(5):
                      sum_unchecked += int(current[a][b])
                  win_num = int(num)
                  print(current, i)
                  print(sum_unchecked)
                  print(win_num)
                  break_out_flag = True
                  break
          if break_out_flag:
            break
        if break_out_flag:
          break
      if break_out_flag:
        break
    
  return sum_unchecked * win_num

#print(part1('day4_data.txt'))
print(part2('day4_data.txt'))