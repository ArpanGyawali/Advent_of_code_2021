def part1(file):
  with open(file, 'r') as f:
    measurements = f.readlines()
    print(len(measurements))
    no_of_increaments = 0
    old = measurements[0]
    for measurement in measurements:
      if int(measurement) > int(old):
        no_of_increaments += 1
      old = measurement

  print(no_of_increaments)

def part2(file):
  with open(file, 'r') as f:
    measurements = f.readlines()
    print(len(measurements))
    no_of_increaments = 0
    old_sum = int(measurements[0]) + int(measurements[1]) + int(measurements[2])
    for i in range(1, len(measurements) - 2):
      new_sum = int(measurements[i]) + int(measurements[i+1]) + int(measurements[i+2])
      if new_sum > old_sum:
        no_of_increaments += 1
      old_sum = new_sum
      
  print(no_of_increaments)


#result = part1('task1_measurements.txt')
result = part2('task1_measurements.txt')

