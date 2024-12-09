print('> Day 4:')
with open('day4.txt') as file:
    words = [l.strip() for l in file.readlines()]

# Part 1
counter = 0

for i in range(len(words)):
    for j in range(len(words[0])):
        current = words[i][j]
        if current == 'X':
            # forward
            if words[i][j:j + 4] == 'XMAS':
                counter += 1
            # backward
            if words[i][j - 3:j + 1] == 'SAMX':
                counter += 1
            # down
            if ''.join([el[j] for el in words[i:i + 4]]) == 'XMAS':
                counter += 1
            # up
            if ''.join([el[j] for el in words[i - 3:i + 1]]) == 'SAMX':
                counter += 1
            # diagonal down right
            if (i + 3 < len(words) and j + 3 < len(words[i]) and
                    words[i + 1][j + 1] == 'M' and words[i + 2][j + 2] == 'A' and words[i + 3][
                        j + 3] == 'S'):
                counter += 1
            # diagonal down left
            if (i + 3 < len(words) and j >= 3 and
                    words[i + 1][j - 1] == 'M' and words[i + 2][j - 2] == 'A' and words[i + 3][j - 3] == 'S'):
                counter += 1
            # diagonal up left
            if (i >= 3 and j >= 3 and
                    words[i - 1][j - 1] == 'M' and words[i - 2][j - 2] == 'A' and words[i - 3][j - 3] == 'S'):
                counter += 1
            # diagonal up right
            if (i >= 3 and j + 3 < len(words[i]) and
                    words[i - 1][j + 1] == 'M' and words[i - 2][j + 2] == 'A' and words[i - 3][j + 3] == 'S'):
                counter += 1
print('part 1:', counter)  # 2562

# Part 2
counter = 0

for i in range(len(words)):
    for j in range(len(words[0])):
        current = words[i][j]
        if current == 'A':
            # if it's the first or last col/row, skip
            if not (1 < i + 1 < len(words) and 1 < j + 1 < len(words[i])):
                continue
            sub_counter = 0
            # diagonal down right
            if words[i - 1][j - 1] == 'M' and words[i + 1][j + 1] == 'S':
                sub_counter = sub_counter + 1
            # diagonal down left
            if words[i - 1][j + 1] == 'M' and words[i + 1][j - 1] == 'S':
                sub_counter = sub_counter + 1
            # diagonal up left
            if words[i - 1][j - 1] == 'S' and words[i + 1][j + 1] == 'M':
                sub_counter = sub_counter + 1
            # diagonal up right
            if words[i - 1][j + 1] == 'S' and words[i + 1][j - 1] == 'M':
                sub_counter += 1

            if sub_counter == 2:
                counter += 1

print('part 2:', counter)  # 1902
