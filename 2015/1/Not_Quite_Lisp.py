def part_1(input_file):
    opening = input_file.count("(")
    closing = input_file.count(")")
    return opening-closing


def part_2(input_file):
    count = 0
    for i in range(len(input_file)):
        if count == -1:
            return i
        if input_file[i] == "(":
            count += 1
        else:
            count -=1


def main():
    filename = "/Users/zolo_capricorn/iCloud_Drive_(Archive)/Challenge/Advent_of_Code/2015/1/input.txt"
    input_file = open(filename, "r").read()
    part1 = part_1(input_file)
    part2 = part_2(input_file)
    return print(part1, part2)
main()

