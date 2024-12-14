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


p1 = part1()
print("Part 1 answer:", p1)
