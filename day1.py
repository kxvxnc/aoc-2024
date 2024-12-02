def part1():
    with open('day1_input') as f:
        column_left = []
        column_right = []
        rows = 0
        for line in f:
            clean_line = line.replace('\n', '').split('  ')
            column_left.append(int(clean_line[0]))
            column_right.append(int(clean_line[1]))
            rows += 1
        column_left.sort()
        column_right.sort()
        diffs = 0
        for i in range(rows):
            diff = abs(column_left[i] - column_right[i])
            diffs += diff
    return diffs


def part2():
    with open('day1_input') as f:
        counts_left = {}
        counts_right = {}
        for line in f:
            clean_line = line.replace('\n', '').split('  ')
            num_1 = int(clean_line[0])
            num_2 = int(clean_line[1])
            counts_left[num_1] = counts_left.get(num_1, 0) + 1
            counts_right[num_2] = counts_right.get(num_2, 0) + 1
        similarity_score = 0
        for id, count in counts_left.items():
            if id in counts_right:
                similarity_score += count * id * counts_right[id]
        return similarity_score


def main():
    print(f"Part 1 Solution: {part1()}")
    print(f"Part 2 Solution: {part2()}")


main()
