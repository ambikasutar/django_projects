def getSum(number):
  final_list = []
  total_sum = 0
  for i in range((number)):
    if i%3==0 or i%5==0:
      final_list.append(i)
      total_sum += i
  return total_sum


if __name__ == '__main__':
  number = eval(input('Enter number range:\n'))
  total_sum = getSum(number)
  #print(f"Final List:{final_list}")
  print(f"Total Sum:{total_sum}")
