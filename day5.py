from itertools import filterfalse
import time

print('> Day 5:')
with (open('day5.txt') as file):
    y, z = file.read().split("\n\n")
    rules = [l.split('|') for l in y.split('\n')]
    pages = [l.split(',') for l in z.split('\n')]

# Part 1
def is_correct(lst):
    for i, current in enumerate(lst):
        predecessors = lst[:i]
        # all rules with current page on the right
        relevant_rules = [r[1] for r in rules if r[0] == current]
        inters = set(predecessors).intersection(relevant_rules)
        if len(inters) != 0:
            return False
    return True

correct_lines = list(filter(is_correct, pages))
middle_pages = [int(c[len(c) // 2]) for c in correct_lines]
print('part 1:', sum(middle_pages))  # 7307

# part2
start = time.time()
incorrect_lines = list(filterfalse(is_correct, pages))

def put_in_order(lst):
    res = lst.copy()
    i = 0
    while i < len(res):
        current = res[i]
        predecessors = res[:i]
        for r in rules:
            if r[0] == current:
                if r[1] in predecessors:
                    j = res.index(r[1])
                    res[i], res[j] = res[j], res[i]
                    i = j
                    continue
        i += 1
    return res

corrected_lines = list(map(put_in_order, incorrect_lines))
middle_pages = [int(c[len(c) // 2]) for c in corrected_lines]
print('part 2:', sum(middle_pages))  # 4713 in 1 second
end = time.time()
print(round(end - start, 2), 'seconds')
