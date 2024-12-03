def part1():
    distance = 0
    left = []
    right = []
    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            nums = line.split()
            left.append(nums[0])
            right.append(nums[1])

    left.sort()
    right.sort()
    for l, r in zip(left, right):
        distance += abs(int(l)-int(r))

    return distance


def part2():
    left = []
    right = []
    sim_score = 0
    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            nums = line.split()
            left.append(nums[0])
            right.append(nums[1])
    right_counts = {}
    for r in right:
        if r in right_counts:
            right_counts[r] += 1
        else:
            right_counts[r] = 1
    for l in left:
        if l in right_counts:
            sim_score += int(l) * right_counts[l]

    return sim_score


p1 = part1()
print("Part 1 answer:", p1)

p2 = part2()
print("Part 2 answer:", p2)
