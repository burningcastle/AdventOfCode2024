import time

print('> Day 6:')
with (open('day6.txt') as file):
    mapp = [list(l.strip()) for l in file.readlines()]


def turn_right(direction):
    if direction == (-1, 0): return 0, 1  # right
    if direction == (0, 1): return 1, 0  # down
    if direction == (1, 0): return 0, -1  # left
    if direction == (0, -1): return -1, 0  # up


def is_on_map(pos):
    return pos[0] in range(len(mapp)) and pos[1] in range(len(mapp[0]))


# perform patrol and return True if it is a loop
def perform_patrol(route):
    direction = -1, 0  # up
    next = start
    stepcount = 0
    while is_on_map(next):
        nextVal = route[next[0]][next[1]]
        if stepcount == 6000:  # loop detection magic number :D
            return True
        elif nextVal != '#':
            stepcount += 1
            route[next[0]][next[1]] = 'X'
        else:
            # next is obstruction
            next = next[0] - direction[0], next[1] - direction[1]
            direction = turn_right(direction)
        next = next[0] + direction[0], next[1] + direction[1]
    return False


# get start position
for i, current in enumerate(mapp):
    if '^' in current:
        start = i, current.index('^')

# Part 1
# copy the map
patrol_route = [line.copy() for line in mapp]

perform_patrol(patrol_route)
print('part 1:', sum([line.count('X') for line in patrol_route]))  # 5145

# Part 2
start_time = time.time()
x_positions = [(i, j) for i, line in enumerate(patrol_route) for j, p in enumerate(line) if p == 'X']
loop_counter = 0
for candidate in x_positions:
    # ignore start position
    if candidate[0] == start[0] and candidate[1] == start[1]: continue
    # deep copy the map
    alternate_route = [line.copy() for line in mapp]
    # place obstruction candidate
    alternate_route[candidate[0]][candidate[1]] = '#'
    if perform_patrol(alternate_route): loop_counter += 1
    # if loop_counter % 100 == 0: print('loops detected:', loop_counter)

print('part 2:', loop_counter)  # 1523 in 5 seconds
end_time = time.time()
print(round(end_time - start_time, 2), 'seconds')
