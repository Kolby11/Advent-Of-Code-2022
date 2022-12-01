lines = open("Day 1\input.txt", "r").readlines()
elfes = []


def readInput():
    calorieAmount = 0
    for line in lines:
        if line == "\n":
            elfes.append(calorieAmount)
            calorieAmount = 0
        else:
            calorieAmount += int(line)


def GetMostAmountOfCalories():
    return max(elfes)


def GetTopThreeAmountOfCalories():
    amount = 0
    for i in range(3):
        amount += GetMostAmountOfCalories()
        print(elfes)
        elfes.remove(GetMostAmountOfCalories())
    return amount


readInput()
print(GetMostAmountOfCalories())
# 68923
print(GetTopThreeAmountOfCalories())
# 200044
