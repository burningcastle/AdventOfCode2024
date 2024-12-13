"""
Needs refactoring :(
"""
print('> Day 9:')
with (open('day9.txt') as file):
    line = file.read()

# create disk map
disk_map_orig = list()
block_id = 0
for index, char in enumerate(line):
    # block
    if index % 2 == 0:
        for _ in range(int(char)):
            disk_map_orig.append(block_id)
        block_id += 1
    # free space
    else:
        for _ in range(int(char)):
            disk_map_orig.append('.')


def find_free_space(disk_mapp, length_block, start, end):
    start_index = start
    end_index = start
    if length_block > 1:
        while start_index <= end - length_block:
            next_free = disk_mapp.index('.', end_index + 1, end - length_block + 1)
            if next_free == end_index + 1 and next_free - start_index == length_block - 1:
                end_index = next_free
                break
            if next_free > end_index + 1:
                start_index = next_free
                end_index = start_index
                continue
            else:
                end_index += 1
    return start_index, end_index


def compact(disk_map, whole_files):
    left = 0
    right = len(disk_map) - 1
    while left < right:
        # going from right to left ignoring free space
        current_block_id = disk_map[right]
        if current_block_id == '.':
            right -= 1
            continue
        try:
            # get next free space
            left = disk_map.index('.', left, right)
        except ValueError:
            # no free space left
            break

        # get start and end of data block
        prev_block_id = disk_map[right - 1]
        length_of_block = 1
        while whole_files and prev_block_id == current_block_id and right - length_of_block >= left:
            length_of_block += 1
            prev_block_id = disk_map[right - length_of_block]
        start_index_block = right - length_of_block + 1
        end_index_block = right

        try:
            # find free space for data block
            start_index_free_space, end_index_free_space = find_free_space(disk_map, length_of_block, left, right)
            # switch blocks with free space
            for ind in range(start_index_free_space, end_index_free_space + 1): disk_map[ind] = current_block_id
            for ind in range(start_index_block, end_index_block + 1): disk_map[ind] = '.'
        except ValueError:
            # no free space found for the current block size
            right -= length_of_block
    return disk_map


check_sum = sum([i * x for i, x in enumerate(compact(disk_map_orig.copy(), False)) if x != '.'])
print('part 1:', check_sum)  # 6283404590840

check_sum = sum([i * x for i, x in enumerate(compact(disk_map_orig.copy(), True)) if x != '.'])
print('part 2:', check_sum)  # 6304576012713
