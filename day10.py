print('> Day 10:')
with (open('day10.txt') as file):
    topographic_map = [list(l.strip()) for l in file.readlines()]


def get_climbable_neighbours(pos):
    current_height = int(topographic_map[pos[0]][pos[1]])
    next_height = current_height + 1
    next = []
    if pos[0] > 0:
        # up
        if topographic_map[pos[0] - 1][pos[1]] == str(next_height):
            next.append((pos[0] - 1, pos[1]))
    if pos[0] + 1 < len(topographic_map):
        # down
        if topographic_map[pos[0] + 1][pos[1]] == str(next_height):
            next.append((pos[0] + 1, pos[1]))
    if pos[1] > 0:
        # left
        if topographic_map[pos[0]][pos[1] - 1] == str(next_height):
            next.append((pos[0], pos[1] - 1))
    if pos[1] + 1 < len(topographic_map[0]):
        # right
        if topographic_map[pos[0]][pos[1] + 1] == str(next_height):
            next.append((pos[0], pos[1] + 1))
    return next


def find_summits(start):
    current_height = int(topographic_map[start[0]][start[1]])
    if current_height == 9: return {start}
    next = get_climbable_neighbours(start)
    result = set()
    for n in next: result.update(find_summits(n))
    return result


# find all trailheads
trailheads = [(i, j) for i, line in enumerate(topographic_map) for j, p in enumerate(line) if p == '0']

# Part 1
summits = [find_summits(x) for x in trailheads]
scores = [len(x) for x in summits]
print('part 1:', sum(scores))  # 459


# Part 2
def find_all_paths(starting_pos):
    finished_paths = set()
    unfinished_paths = set()
    unfinished_paths.add(tuple([starting_pos]))
    while len(unfinished_paths) > 0:
        current_path = list(unfinished_paths.pop())
        next = get_climbable_neighbours(current_path[-1])
        for n in next:
            new_path = current_path.copy()
            new_path.append(n)
            if topographic_map[n[0]][n[1]] == '9':
                finished_paths.add(tuple(new_path))
            else:
                unfinished_paths.add(tuple(new_path))
    return finished_paths


paths = [find_all_paths(trailhead) for trailhead in trailheads]
ratings = [len(p) for p in paths]
print('part 2:', sum(ratings))  # 1034
