import re

print('> Day 3:')
with open('day3.txt') as file:
    lines = [l.strip() for l in file.readlines()]
    regex_str = ''.join(lines)

# Part 2 preprocessing
regex_str = re.sub("don\\'t\\(\\).*?((do\\(\\))|$)", "", regex_str)

# Part 1
muls = re.findall("mul\\(\\d+,\\d+\\)", regex_str)
pairs = [x[4:-1].split(',') for x in muls]
print(sum([int(p[0]) * int(p[1]) for p in pairs]))  # 170807108

# Part 2
# 74838033
