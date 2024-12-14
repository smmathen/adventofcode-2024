def part1():
    f = open("ainput.txt", 'r')
    lines = f.readlines()
    graph = []
    for line in lines:
        chars = list(line)[:-1]
        graph.append(chars)

    count = 0
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] != "X":
                continue
            # check up
            if i >= 3:
                # directly up
                if graph[i-1][j] == 'M' and graph[i-2][j] == 'A' and graph[i-3][j] == 'S':
                    count += 1

                # left up
                if j >= 3:
                    if graph[i-1][j-1] == 'M' and graph[i-2][j-2] == 'A' and graph[i-3][j-3] == 'S':
                        count += 1
                # right up
                if j < len(graph[i])-3:
                    if graph[i-1][j+1] == 'M' and graph[i-2][j+2] == 'A' and graph[i-3][j+3] == 'S':
                        count += 1

            # check down
            if i < len(graph)-3:
                # directly down
                if graph[i+1][j] == 'M' and graph[i+2][j] == 'A' and graph[i+3][j] == 'S':
                    count += 1
                # down left
                if j >= 3:
                    print(i, j)
                    if graph[i+1][j-1] == 'M' and graph[i+2][j-2] == 'A' and graph[i+3][j-3] == 'S':
                        count += 1
                # down right
                if j < len(graph[i])-3:
                    if graph[i+1][j+1] == 'M' and graph[i+2][j+2] == 'A' and graph[i+3][j+3] == 'S':
                        count += 1
            # check right
            if j < len(graph)-3:
                if graph[i][j+1] == 'M' and graph[i][j+2] == 'A' and graph[i][j+3] == 'S':
                    count += 1
            # check left
            if j >= 3:
                if graph[i][j-1] == 'M' and graph[i][j-2] == 'A' and graph[i][j-3] == 'S':
                    count += 1

    print("Count:", count)


part1()
