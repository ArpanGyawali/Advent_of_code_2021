def part1(file):
  gamma = ''
  epsilon = ''
  with open(file, 'r') as f:
    lines = f.readlines()
    total = len(lines)
    count_arr = [0] * 12
    for i in range(0, total):
      for j in range(0, 12):
        if lines[i][j] == '1':
          count_arr[j] += 1
    
    for i in range(0, 12):
      if count_arr[i] > total/2:
        gamma = gamma + '1'
      else:
        gamma = gamma + '0'

    for digit in gamma:
      epsilon = (epsilon + '1') if digit == '0' else (epsilon + '0')

  return int(gamma,2) * int(epsilon, 2)

def calculate_oxygen(list, k=0):
  new_list = []
  total = len(list)
  print(str(total) + ' oxy')
  if total == 1:
    return list[0].strip()

  count_arr = [0] * 12

  for i in range(0, total):
    for j in range(0, 12):
      if list[i][j] == '1':
        count_arr[j] += 1
  
  for l in list:
    if count_arr[k] >= total/2:
      if l[k] == '1': new_list.append(l) 
    else:
      if l[k] == '0': new_list.append(l) 


  return calculate_oxygen(new_list, k = k+1)

def calculate_co2(list, k=0):
  new_list = []
  total = len(list)
  print(str(total) + ' co2')
  if total == 1:
    return list[0].strip()

  count_arr = [0] * 12

  for i in range(0, total):
    for j in range(0, 12):
      if list[i][j] == '1':
        count_arr[j] += 1
  

  for l in list:
    if count_arr[k] < total/2:
      if l[k] == '1': new_list.append(l) 
    else:
      if l[k] == '0': new_list.append(l) 

  return calculate_co2(new_list, k=k+1)


def part2(file):
  with open(file, 'r') as f:
    lines = f.readlines()
    oxygen = calculate_oxygen(lines)
    print(oxygen)
    co2 = calculate_co2(lines)
    print(co2)
    return int(oxygen,2) * int(co2, 2)


    

  

#print(part1('day3_data.txt'))
print(part2('day3_data.txt'))