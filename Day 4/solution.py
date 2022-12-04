lines = open("Day 4\input.txt", "r").readlines()


def ProcessInput():
    pairs = []
    for line in lines:
        pair = []
        elf = []
        number = ""
        for i, char in enumerate(line):
            if char == "-":
                elf.append(int(number))
                number = ""
                continue
            if char == ",":
                elf.append(int(number))
                pair.append(elf)
                elf = []
                number = ""
                continue
            if i == (len(line) - 1) and char == "\n":
                elf.append(int(number))
                pair.append(elf)
                pairs.append(pair)
                break
            elif i == (len(line) - 1):
                number += char
                elf.append(int(number))
                pair.append(elf)
                pairs.append(pair)
                break
            number += char
    return pairs


def Part1():
    fullyContains = 0
    for pair in ProcessInput():
        if (pair[0][0] <= pair[1][0]) and (pair[0][1] >= pair[1][1]):
            fullyContains += 1
        elif (pair[1][0] <= pair[0][0]) and (pair[1][1] >= pair[0][1]):
            fullyContains += 1
    return fullyContains


def Part2():
    overlaps = 0
    for pair in ProcessInput():
        if pair[0][0] >= pair[1][0] and pair[0][0] <= pair[1][1]:
            overlaps += 1
        elif pair[0][1] >= pair[1][0] and pair[0][1] <= pair[1][1]:
            overlaps += 1
        elif pair[1][0] >= pair[0][0] and pair[1][0] <= pair[0][1]:
            overlaps += 1
        elif pair[1][1] >= pair[0][0] and pair[1][1] <= pair[0][1]:
            overlaps += 1
    return overlaps


print(Part1())
# 538
print(Part2())
# 792
