def part1():
    f = open("ainput.txt", 'r')
    rules = []
    total = 0
    for line in f.readlines():
        if line == "\n":
            continue

        if "|" in line:
            num1, num2 = line.strip().split('|')
            rules.append((num1, num2))
            continue

        nums = line.strip().split(',')
        indexes = {}
        for i, num in enumerate(nums):
            indexes[int(num)] = i

        for first, second in rules:
            first = int(first)
            second = int(second)
            broken = False
            if first in indexes and second in indexes:
                if indexes[first] > indexes[second]:
                    broken = True
                    break
        if not broken:
            middle = len(nums)//2
            mid_val = int(nums[middle])
            total += mid_val

    print("Part 1:", total)


part1()
