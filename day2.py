print('> Day 2:')
with open('day2.txt') as file:
    lines = [l.strip() for l in file.readlines()]
    reports = [[int(x) for x in l.split()] for l in lines]


# Part 1
def is_safe(report):
    pairs = list(zip(report[:len(report) - 1], report[1:]))
    diffs = [x - y for x, y in pairs]
    # The levels are either all increasing or all decreasing
    check1 = all(i > 0 for i in diffs) or all(i < 0 for i in diffs)
    # Any two adjacent levels differ by at least one and at most three
    check2 = all(1 <= abs(i) <= 3 for i in diffs)
    return check1 and check2


safe_records = list(filter(is_safe, reports))
print(len(safe_records))  # 686


# Part 2
def is_safe_allowing_one_error(report):
    for index, item in enumerate(report):
        new_list = list(report)
        del new_list[index]
        if is_safe(new_list):
            return True
    return False


safe_records = list(filter(is_safe_allowing_one_error, reports))
print(len(safe_records))  # 717
