lines = open("Day 3\input.txt", "r").readlines()


def ProcessInput():
    rucksacks = []
    for line in lines:
        rucksack = ""
        for i, char in enumerate(line):
            if char == "\n" or char == " " or i == len(line):
                rucksacks.append(rucksack)
                rucksack = ""
                break
            rucksack += char
    return rucksacks


def SplitRucksacks(containers):
    splitContainers = []
    for container in containers:
        splitContainer = []
        compartment = ""
        for i, char in enumerate(container):
            if i == (len(container) / 2):
                splitContainer.append(compartment)
                compartment = ""
            if i == len(container) - 1:
                compartment += char
                splitContainer.append(compartment)
                compartment = ""
                break
            compartment += char
        splitContainers.append(splitContainer)
    return splitContainers


def FindCommonItem(splitRucksack):
    for char in splitRucksack[0]:
        if char in splitRucksack[1]:
            return char


def GetItemPriority(item):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for value, char in enumerate(alphabet):
        if item == char:
            return value + 1
    return None


def GetElfGroups(rucksacks):
    groups = []
    for i in range(0, len(rucksacks), 3):
        groups.append([rucksacks[i], rucksacks[i + 1], rucksacks[i + 2]])
    return groups


def FindMostCommonItemInThree(rucksacks):
    for char in rucksacks[0]:
        if char in rucksacks[1] and char in rucksacks[2]:
            return char


def Part1():
    commonItemPriority = []
    rucksacks = ProcessInput()
    splitRucksacks = SplitRucksacks(rucksacks)
    for compartment in splitRucksacks:
        commonItemPriority.append(GetItemPriority(FindCommonItem(compartment)))
    return sum(commonItemPriority)


def Part2():
    elfGroups = []
    commonItemPriority = []
    rucksacks = ProcessInput()
    elfGroups = GetElfGroups(rucksacks)
    for group in elfGroups:
        commonItemPriority.append(GetItemPriority(FindMostCommonItemInThree(group)))
    return sum(commonItemPriority)


print(Part1())
# 7553
print(Part2())
# 2758
