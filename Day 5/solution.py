lines = open("Day 5\input.txt", "r").readlines()

defaultStacks = {}
commands = []


def ProcessInput():
    for i, line in enumerate(lines):
        if line[0] == "\n" or line[0] == " ":
            continue
        elif i < 8:
            stackIndex = 1
            for index in range(1, len(line), 4):
                if i == 0:
                    defaultStacks[stackIndex] = []
                    if line[index] != " ":
                        defaultStacks[stackIndex].append(line[index])
                else:
                    if line[index] != " ":
                        defaultStacks[stackIndex].append(line[index])
                stackIndex += 1
        else:
            if i == len(lines) - 1:
                splitLine = line.split(" ")
                command = {splitLine[0]: int(splitLine[1]), splitLine[2]: int(splitLine[3]), splitLine[4]: int(splitLine[5])}
            else:
                splitLine = line.split(" ")
                lastInt = splitLine[5][:-1]
                command = {splitLine[0]: int(splitLine[1]), splitLine[2]: int(splitLine[3]), splitLine[4]: int(lastInt)}
                commands.append(command)
    commands.append(command)


def Part1(crates):
    answer = ""
    for command in commands:
        for crateIndex in range(command["move"]):
            crates[command["to"]].insert(0, crates[command["from"]][0])
            crates[command["from"]].pop(0)
    for crate in crates.values():
        if len(crate) > 0:
            answer += crate[0]
        else:
            answer += " "
    return answer


def Part2(crates):
    answer = ""
    for command in commands:
        for crateIndex in range(command["move"]):
            crates[command["to"]].insert(crateIndex, crates[command["from"]][0])
            crates[command["from"]].pop(0)
    for crate in crates.values():
        if len(crate) > 0:
            answer += crate[0]
        else:
            answer += " "
    return answer


ProcessInput()
print(Part1(defaultStacks))
# PTWLTDJV

defaultStacks = {}
commands = []
ProcessInput()
print(Part2(defaultStacks))
# WZMFVGGZP
