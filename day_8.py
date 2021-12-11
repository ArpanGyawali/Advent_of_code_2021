import math

def part1(file):
  with open(file, 'r') as f:
    lines = f.readlines()
    outputs = [line.split(' | ')[1].strip() for line in lines]
    outputs = [output.split() for output in outputs]
    unique_no = [2,3,4,7]
    count = 0
    for output in outputs:
      for digit in output:
        if len(digit) in unique_no:
          print(digit)
          count += 1;
    print(count)
    
import itertools

def part2(file):
  

  with open(file) as f:
      raw_data = f.read().strip().split("\n")
      data = [
          [
              sorted(line[:line.index("|") - 1].split(" ")),
              line[line.index("|") + 2:].split(" ")
          ] for line in raw_data
      ]

  digits_key = [
      "abcefg",
      "cf",
      "acdeg",
      "acdfg",
      "bcdf",
      "abdfg",
      "abdefg",
      "acf",
      "abcdefg",
      "abcdfg"
  ]
  digits = sorted(digits_key)
  digits = tuple(digits)

  ans = 0

  for line in data:
      clues = line[0]
      assert len(clues) == 10

      num = line[1]

      # Try all possible substitutions
      for sigma in itertools.permutations("abcdefg"):
          # Reencode digits
          key = {}
          for c in "abcdefg":
              key[c] = sigma["abcdefg".index(c)]

          new_clues = [] * 10
          for clue in clues:
              x = ""
              for char in clue:
                  x += key[char]
              x = "".join(sorted(x))
              new_clues.append(x)

          new_clues.sort()

          if tuple(new_clues) == digits:
              # Get the number it's supposed to be
              n = []
              for d in num:
                  x = ""
                  for char in d:
                      x += key[char]
                  x = "".join(sorted(x))
                  n.append(digits_key.index(x))

              ans += int("".join([str(i) for i in n]))

              break

  print(ans)
    
    

#part1('day8_data.txt')
part2('day8_data.txt')