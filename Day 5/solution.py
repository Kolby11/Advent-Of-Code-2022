lines = open("Day 5\input.txt", "r").readlines()

stacks = {}
commands = []


def ProcessInput():
    for i, line in enumerate(lines):
        if line[0] == "\n" or line[0] == " ":
            continue
        elif i < 8:
            stackIndex = 1
            for index in range(1, len(line), 4):
                if i == 0:
                    stacks[stackIndex] = []
                    if line[index] != " ":
                        stacks[stackIndex].append(line[index])
                else:
                    if line[index] != " ":
                        stacks[stackIndex].append(line[index])
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


def Part1():
    answer = ""
    for command in commands:
        for crateIndex in range(command["move"]):
            stacks[command["to"]].insert(0, stacks[command["from"]][0])
            stacks[command["from"]].pop(0)
    for stack in stacks.values():
        if len(stack) > 0:
            answer += stack[0]
        else:
            answer += " "
    return answer


ProcessInput()
print(Part1())
# PTWLTDJ V
