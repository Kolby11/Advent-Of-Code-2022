lines = open("Day 5\input.txt", "r").readlines()

stacks = {}
commands = []


def ProcessInput():
    for i, line in enumerate(lines):
        value = ""
        stackIndex = 1
        if i == 0:
            for index in range(1, len(line), 4):
                stacks[stackIndex] = []
                if line[index] != " ":
                    stacks[stackIndex].append(line[index])
                stackIndex += 1
        elif i < 8:
            for index in range(1, len(line), 4):
                if line[index] != " ":
                    stacks[stackIndex].append(line[index])
                stackIndex += 1
        elif line[0] == "\n" or line[0] == " ":
            continue
        else:
            splitLine = line.split(" ")
            command = {splitLine[0]: splitLine[1], splitLine[2]: splitLine[3], splitLine[4]: splitLine[5][:-1]}
            commands.append(command)


def Part1():
    for command in commands:
        for crateIndex in range(command["move"]):
            stacks[command["to"]].insert(0, stacks[command["from"]][0])
            stacks[command["from"]].pop(0)


ProcessInput()
print(commands)
# print(Part1())
# 538
# print(Part2())
# 792
