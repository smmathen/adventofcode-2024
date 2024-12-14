import re


def part1():
    with open('ainput.txt', 'r') as f:
        lines = f.readlines()

    total_sum = 0
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    for line in lines:
        matches = re.findall(pattern, line)
        for match in matches:
            nums = match[4:-1].split(",")
            num1 = int(nums[0])
            num2 = int(nums[1])
            total_sum += num1 * num2
    return total_sum


def part2():
    with open('ainput.txt', 'r') as f:
        lines = f.readlines()

    total = 0
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    enabled = True
    for line in lines:
        while len(line) > 0:
            do_index = line.find("do()")
            dont_index = line.find("don't()")
            matches = re.findall(pattern, line)
            if len(matches) == 0:
                break
            else:
                mul_index = line.find(matches[0])

            if do_index == -1:
                do_index = len(line)+1
            if dont_index == -1:
                dont_index = len(line)+1

            if mul_index < do_index and mul_index < dont_index:
                if enabled:
                    match = matches[0]
                    len_of_match = len(match)
                    nums = match[4:-1].split(",")
                    num1 = int(nums[0])
                    num2 = int(nums[1])
                    total += num1 * num2
                line = line[mul_index + len_of_match:]
            elif do_index < dont_index:
                enabled = True
                line = line[do_index + len("do()"):]

            else:
                enabled = False
                line = line[dont_index + len("don't()"):]

    return total


p1 = part1()
print("Part 1 answer:", p1)

p2 = part2()
print("Part 2 answer:", p2)
