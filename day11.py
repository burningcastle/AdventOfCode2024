import time

print('> Day 11:')
with (open('day11.txt') as file):
    initial_stones = [int(x) for x in file.read().split()]


def blink_naive(stones, number_of_blinks, counter=0):
    if number_of_blinks > counter:
        new_stones = list()
        for stone in stones:
            # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
            if stone == 0:
                new_stones.append(1)
            # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones.
            # The left half of the digits are engraved on the new left stone, and the right half of the digits are
            # engraved on the new right stone. (The new numbers don't keep extra leading zeroes:
            # 1000 would become stones 10 and 0.)
            elif len(str(stone)) % 2 == 0:
                n = len(str(stone))
                new_stones.append(int(str(stone)[0:n // 2]))
                new_stones.append(int(str(stone)[n // 2:]))
            # If none of the other rules apply, the stone is replaced by a new stone; the old stone's number
            # multiplied by 2024 is engraved on the new stone.
            else:
                new_stones.append(stone * 2024)
        return blink_naive(new_stones, number_of_blinks, counter + 1)
    else:
        return stones


# Part 1
stones_after_blinking = blink_naive(initial_stones, 25)
print('part 1:', len(stones_after_blinking))  # 186203


# Part 2
def blink(amounts_of_stones, number_of_blinks, counter=0):
    if number_of_blinks > counter:
        new_amounts = dict()
        for current_stone, count in amounts_of_stones.items():
            new_stones = blink_naive([current_stone], 1)
            for s in new_stones:
                new_amounts[s] = new_amounts.get(s, 0) + count
        return blink(new_amounts, number_of_blinks, counter + 1)
    else:
        return amounts_of_stones


start_time = time.time()
# count number of stones
amount_of_starting_stones = dict()
for stone in initial_stones: amount_of_starting_stones[stone] = amount_of_starting_stones.get(stone, 0) + 1

stones_after_blinking = blink(amount_of_starting_stones, 75)
print('part 2:', sum(stones_after_blinking.values()))  # 221291560078593 in 0.06 seconds
end_time = time.time()
print(round(end_time - start_time, 2), 'seconds')
