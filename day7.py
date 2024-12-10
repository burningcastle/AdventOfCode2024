import time

print('> Day 7:')
with (open('day7.txt') as file):
    equations = [l.strip().split(': ') for l in file.readlines()]
    equations = [[int(equation[0]), [int(x) for x in equation[1].split(' ')]] for equation in equations]


def solve(res, ops, intermediate_results=[]):
    if len(ops) == 0:
        if any(res == i for i in intermediate_results):
            return res
        else:
            return 0
    if len(intermediate_results) == 0:
        return solve(res, ops[1:], [ops[0]])
    else:
        add_next_number = [x + ops[0] for x in intermediate_results if x + ops[0] <= res]
        multiply_next_number = [x * ops[0] for x in intermediate_results if x * ops[0] <= res]
        new_intermediate_results = add_next_number + multiply_next_number
        # --- part2 --- add pipe operator
        if include_pipe_parameter:
            pipe_next_number = [int(str(x) + str(ops[0])) for x in intermediate_results if
                                int(str(x) + str(ops[0])) <= res]
            new_intermediate_results += pipe_next_number
        # --- /part2 ---
        return solve(res, ops[1:], new_intermediate_results)

# Part 1
include_pipe_parameter = False
results = [solve(equation[0], equation[1]) for equation in equations]
print('part 1:', sum(results))  # 20281182715321

# Part 2
start_time = time.time()
include_pipe_parameter = True
results = [solve(equation[0], equation[1]) for equation in equations]
print('part 2:', sum(results))  # 159490400628354 in 1.8 seconds
end_time = time.time()
print(round(end_time - start_time, 2), 'seconds')
