lines = open("Day 2\input.txt", "r").readlines()
plays = []


def readInput():
    round = []
    for line in lines:
        for char in line:
            if char == "\n" or char == " ":
                continue
            round.append(char)
        plays.append(round)
        round = []


def play():
    points = 0
    for round in plays:
        match round[0]:
            case "A":
                match round[1]:
                    case "X":
                        points += 1 + 3
                    case "Y":
                        points += 2 + 6
                    case "Z":
                        points += 3
            case "B":
                match round[1]:
                    case "X":
                        points += 1
                    case "Y":
                        points += 2 + 3
                    case "Z":
                        points += 3 + 6
            case "C":
                match round[1]:
                    case "X":
                        points += 1 + 6
                    case "Y":
                        points += 2
                    case "Z":
                        points += 3 + 3
    return points


def play2():
    points = 0
    for round in plays:
        match round[0]:
            case "A":
                match round[1]:
                    case "X":
                        points += 3 + 0
                    case "Y":
                        points += 1 + 3
                    case "Z":
                        points += 2 + 6
            case "B":
                match round[1]:
                    case "X":
                        points += 1 + 0
                    case "Y":
                        points += 2 + 3
                    case "Z":
                        points += 3 + 6
            case "C":
                match round[1]:
                    case "X":
                        points += 2 + 0
                    case "Y":
                        points += 3 + 3
                    case "Z":
                        points += 1 + 6
    return points


readInput()
print(play())
# 11906
print(play2())
# 11186
