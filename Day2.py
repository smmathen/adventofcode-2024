def part1():
    unsafe_count = 0
    with open("ainput.txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            reports = line.split()
            inc = int(reports[1]) > int(reports[0])
            for i in range(len(reports)-1):
                diff = int(reports[i+1]) - int(reports[i])
                abs_diff = abs(diff)
                if abs_diff == 0 or abs_diff > 3:
                    unsafe_count += 1
                    break
                elif diff > 0 and not inc:
                    unsafe_count += 1
                    break
                elif diff < 0 and inc:
                    unsafe_count += 1
                    break

    return len(lines)-unsafe_count


def part2():
    def is_safe(levels):
        increasing = True
        for i in range(len(levels)-1):
            if levels[i+1] <= levels[i]:
                increasing = False
                break

        decreasing = True
        for i in range(len(levels)-1):
            if levels[i+1] >= levels[i]:
                decreasing = False
                break

        differences_good = True
        for i in range(len(levels)-1):
            if not (1 <= abs(levels[i+1]-levels[i]) <= 3):
                differences_good = False
                break

        return (increasing or decreasing) and differences_good

    with open('ainput.txt', 'r') as f:
        lines = f.readlines()

    safe = 0

    for line in lines:
        levels = line.split()
        for i in range(len(levels)):
            levels[i] = int(levels[i])

        if is_safe(levels):
            safe += 1
            continue

        dampened_safe = False
        for i in range(len(levels)):
            dampened = levels[:i] + levels[i + 1:]
            if is_safe(dampened):
                dampened_safe = True
                break

        if dampened_safe:
            safe += 1

    return safe


p1 = part1()
print("Part 1 answer:", p1)
p2 = part2()
print("Part 2 answer:", p2)
