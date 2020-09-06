def getSum():
  total_sum = 0
  prev, cur = 0, 1
  while cur < 4000000:
      prev, cur = cur, prev + cur
      if cur % 2:
          continue
      total_sum += cur
  return total_sum


if __name__ == '__main__':
  # number = eval(input('Enter number range:\n'))
  total_sum = getSum()
  print(f"Total Sum:{total_sum}")