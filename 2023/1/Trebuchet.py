import re

def part_1(input_file):
    result = []
    for text in input_file:
        number = re.findall(r"\d", text)
        if len(number) == 1:
            result.append(int(number[0] + number[0]))
        else:
            result.append(int(number[0] + number[-1]))
    return sum(tuple(result))


def part_2(input_file):
    number_dict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", 
                   "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    regex_list = [r"\d", r"one", r"two", r"three", r"four", r"five", r"six", r"seven", r"eight", r"nine"]
    result = 0
    for text in input_file[0:5]:
        extract = sorted([(m.start(), m.end(), m.group()) for pattern in regex_list for m in re.finditer(pattern, text)])
        choosing = [c[2] for c in extract]
        transfer = [number_dict.get(word) if word.isalpha() else word for word in choosing]
        if len(transfer) == 1:
            result += int(transfer[0] + transfer[0])
        elif len(transfer) > 1:
            result += int(transfer[0] + transfer[-1])
    return result


def main():
    filename = "/Users/zolo_capricorn/iCloud_Drive_(Archive)/Challenge/Advent_of_Code/2023/1/input.txt"
    input_file = open(filename, "r").readlines()
    part1 = part_1(input_file)
    part2 = part_2(input_file)
    return print(part1, part2)
main()

