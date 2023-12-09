import re

def part_1(input_file):
    result = 0
    bag_check = 0
    share_list = []
    regex_list = [r"\d+ red", r"\d+ green", r"\d+ blue"]
    for value in input_file:
        for game in value.split(":"):
            temp_list = []
            if game.find("Game") != -1:
                game_id = int(re.search(r"\d+", game).group())
            else:
                sep_id = game.split(";")
                for id in sep_id:
                    sort_list = [re.findall(pattern, id) for pattern in regex_list]
                    number_list = [int(re.search(r"\d+", *i).group()) if len(i) != 0 else 0 for i in sort_list]
                    temp_list.append(number_list)
                    if number_list[0] <= 12 and number_list[1] <=13 and number_list[2] <= 14:
                        bag_check += 1
                if len(sep_id) == bag_check:
                    result += game_id
                bag_check = 0
        share_list.append(temp_list)
    return share_list, result


def part_2(share_list):
    result = 0
    for per_list in share_list:
        red, green, blue = 0, 0, 0
        for value in per_list:
            if value[0] > red:
                red = value[0]
            if value[1] > green:
                green = value[1]
            if value[2] > blue:
                blue = value[2]
        result += red*green*blue
    return result


def main():
    filename = "/Users/zolo_capricorn/iCloud_Drive_(Archive)/Challenge/Advent_of_Code/2023/2/input.txt"
    input_file = open(filename, "r").readlines()
    share_list, part1 = part_1(input_file)
    part2 = part_2(share_list)
    return print(part1, part2)
main()

