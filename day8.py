import itertools

print('> Day 8:')
with (open('day8.txt') as file):
    lines = [l.strip() for l in file.readlines()]
    frequencies = [f for f in set(''.join(lines)) if f not in ['#', '.']]


def is_on_map(pos): return pos[0] in range(len(lines)) and pos[1] in range(len(lines[0]))


def find_antinodes_part1(combinations):
    for combination in combinations:
        x, y = combination[0][0] - combination[1][0], combination[0][1] - combination[1][1]
        antinode_1 = combination[0][0] + x, combination[0][1] + y
        antinode_2 = combination[1][0] - x, combination[1][1] - y
        if is_on_map(antinode_1): antinodes_part1.add(antinode_1)
        if is_on_map(antinode_2): antinodes_part1.add(antinode_2)


def find_antinodes_part2(combinations):
    for combination in combinations:
        x, y = combination[0][0] - combination[1][0], combination[0][1] - combination[1][1]
        next_antinode = combination[0]
        factor = 1
        # go in one direction...
        while is_on_map(next_antinode):
            antinodes_part2.add(next_antinode)
            next_antinode = combination[0][0] + x * factor, combination[0][1] + y * factor
            factor += 1
        next_antinode = combination[1]
        factor = 1
        # ... other direction
        while is_on_map(next_antinode):
            antinodes_part2.add(next_antinode)
            next_antinode = combination[1][0] - x * factor, combination[1][1] - y * factor
            factor += 1


antinodes_part1 = set()
antinodes_part2 = set()
for frequency in frequencies:
    antennas = [(i, j) for i, line in enumerate(lines) for j, p in enumerate(line) if p == frequency]
    # using itertools for the permutations... sorry I'm lazy ^.^
    antenna_combinations = list(itertools.combinations(antennas, 2))
    find_antinodes_part1(antenna_combinations)
    find_antinodes_part2(antenna_combinations)

# Part 1
print('part 1:', len(antinodes_part1))  # 381

# Part 2
print('part 2:', len(antinodes_part2))  # 1184
