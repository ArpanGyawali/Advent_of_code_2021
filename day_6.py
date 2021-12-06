def part1(file):
  with open(file, 'r') as f:
    line = f.readline()
    lanternfish = line.strip().split(',')
    lanternfish = [int(num) for num in lanternfish]
    for j in range(80):
      for i in range(len(lanternfish)):
        if lanternfish[i] > 0:
          lanternfish[i] -= 1
        elif lanternfish[i] == 0:
          lanternfish[i] = 6
          lanternfish.append(8)
    print(len(lanternfish))


from collections import defaultdict

def part2(file):
  with open(file, 'r') as f:
    line = f.readline()
    lanternfish = line.strip().split(',')
    lanternfish = [int(num) for num in lanternfish]
    by_days = defaultdict(int)
    for fish in lanternfish:  #create a dictionary with count according to no of days left
      if fish not in by_days:
        by_days[fish] = 0
      by_days[fish] += 1

    for day in range(256):
      final = defaultdict(int)
      for fish, count in by_days.items():
        if fish == 0:
          final[6] += count
          final[8] += count
        else:
          final[fish - 1] += count
        

      by_days = final
    print(sum(by_days.values()))
    

#part1('day5_data.txt')
part2('day6_data.txt')