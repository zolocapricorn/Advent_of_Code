def part_1(input_file):
    house_position = [(0, 0)]
    x_axis, y_axis = 0, 0
    result = 1
    for sign in input_file:
        if sign == ">":
            x_axis += 1
        elif sign == "<":
            x_axis -= 1
        elif sign == "^":
            y_axis += 1
        elif sign == "v":
            y_axis -= 1
        if (x_axis, y_axis) not in house_position:
            result += 1
            house_position.append((x_axis, y_axis))
    return result

def part_2(input_file):
    santa_and_robo_santa = [(0, 0)]
    santa_x_axis, santa_y_axis = 0, 0
    robo_santa_x_axis, robo_santa_y_axis = 0, 0
    result = 1
    for sign_number in range(len(input_file)):
        if sign_number%2 == 0:
            if input_file[sign_number] == ">":
                santa_x_axis += 1
            elif input_file[sign_number] == "<":
                santa_x_axis -= 1
            elif input_file[sign_number] == "^":
                santa_y_axis += 1
            elif input_file[sign_number] == "v":
                santa_y_axis -= 1
            if (santa_x_axis, santa_y_axis) not in santa_and_robo_santa:
                result += 1
                santa_and_robo_santa.append((santa_x_axis, santa_y_axis))
        elif sign_number%2 != 0:
            if input_file[sign_number] == ">":
                robo_santa_x_axis += 1
            elif input_file[sign_number] == "<":
                robo_santa_x_axis -= 1
            elif input_file[sign_number] == "^":
                robo_santa_y_axis += 1
            elif input_file[sign_number] == "v":
                robo_santa_y_axis -= 1
            if (robo_santa_x_axis, robo_santa_y_axis) not in santa_and_robo_santa:
                result += 1
                santa_and_robo_santa.append((robo_santa_x_axis, robo_santa_y_axis))
    return result


def main():
    filename = "/Users/zolo_capricorn/iCloud_Drive_(Archive)/Challenge/Advent_of_Code/2015/3/input.txt"
    input_file = open(filename, "r").read()
    part1 = part_1(input_file)
    part2 = part_2(input_file)
    return print(part1, part2)
print("gg")
main()

