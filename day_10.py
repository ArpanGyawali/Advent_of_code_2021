import collections

def part1(file):
  with open(file, 'r') as f:
    lines = f.readlines()
    navigation = [line.strip() for line in lines]
    opening = ['(', '[', '{', '<']
    closing = [')', ']', '}', '>']
    points = {
      ')': 3,
      ']': 57,
      '}': 1197,
      '>': 25137
    }
    score = 0
    for syntax in navigation:
      if syntax[0] in opening:
        stack = [syntax[0]]
      i = 1
      while stack and i < len(syntax):
        if syntax[i] in opening:
          stack.append(syntax[i])
          i += 1
        elif syntax[i] in closing:
          last = stack.pop()
          print(last, syntax[i])
          if opening.index(last) != closing.index(syntax[i]):   #non matching parenthesis
            score += points[syntax[i]]
            break
          else:
            i += 1
            continue
    print(score)

def part2(file):
  with open(file, 'r') as f:
    lines = f.readlines()
    navigation = [line.strip() for line in lines]
    opening = ['(', '[', '{', '<']
    closing = [')', ']', '}', '>']
    points = {
      ')': 1,
      ']': 2,
      '}': 3,
      '>': 4
    }
    score_array = []
    for syntax in navigation:
      if syntax[0] in opening:
        stack = [syntax[0]]
      i = 1
      while stack:
        if i == len(syntax):
          remaining = [closing[index] for index in [i for i in [opening.index(stack[j]) for j in range(len(stack)-1, -1, -1)]]]
          print(remaining, syntax)
          score = 0
          for symbol in remaining:
            score = score * 5 + points[symbol]
          score_array.append(score)
          break
        elif syntax[i] in opening:
          stack.append(syntax[i])
          i += 1
        elif syntax[i] in closing: 
          last = stack.pop()
          if opening.index(last) != closing.index(syntax[i]):   #non matching parenthesis
            break
          else:
            i += 1
            continue
    score_array.sort()
    print(len(score_array))
    middle = int((len(score_array) + 1)/2)
    print(score_array, middle)
    print(score_array[middle - 1])
            

#part1('day10_data.txt')
part2('day10_data.txt')