print('> Day 1:')
with open('day1.txt') as file:
    lines = [l.strip() for l in file.readlines()]
    pairs = [l.split('   ') for l in lines]
    first, second = zip(*pairs)
    list1 = list(map(int, first))
    list2 = list(map(int, second))

# Part 1
sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)
distances = [abs(x - y) for x, y in zip(sorted_list1, sorted_list2)]
print(sum(distances))  # 2164381

# Part 2
similarities = [x * list2.count(x) for x in list1]
print(sum(similarities))
