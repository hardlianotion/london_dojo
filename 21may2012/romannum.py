def print_digit(num, symbols):
  if num == 9:
    return symbols[0] + symbols[2]
  if num == 4:
    return symbols[0] + symbols[1]
  if num >= 5:
    return symbols[1] + symbols[0] * (num - 5)
  return symbols[0] * num


def convert(num):
  symbols = map(lambda x: x.split(), "C D M__X L C__I V X".split("__"))

  retval = "M" * (num // 1000)
  num = num % 1000
  strnum = '%03d' % (num)
  return retval + ''.join([print_digit(int(strnum[i]), symbols[i]) for i in range(3)])

