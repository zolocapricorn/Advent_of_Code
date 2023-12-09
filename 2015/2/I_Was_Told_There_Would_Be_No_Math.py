import re

def part_1(input_file):
    result = 0
    for area in input_file:
        value = re.findall("\d+", area)
        length, width, height = int(value[0]), int(value[1]), int(value[2])
        calculation_list = [length*width, width*height, height*length]
        result += ((2*calculation_list[0]) + (2*calculation_list[1]) + (2*calculation_list[2])) + min(calculation_list)
    return result


def part_2(input_file):
    result = 0
    for area in input_file:
        value = re.findall("\d+", area)
        l, w, h = int(value[0]), int(value[1]), int(value[2])
        calculate_list = sorted([l, w, h])[0:2]
        result += ((calculate_list[0]*2) + (calculate_list[1]*2)) + (l*w*h)
    return result


def main():
    filename = "/Users/zolo_capricorn/iCloud_Drive_(Archive)/Challenge/Advent_of_Code/2015/2/input.txt"
    input_file = open(filename, "r").read().splitlines()
    part1 = part_1(input_file)
    part2 = part_2(input_file)
    return print(part1, part2)
main()

