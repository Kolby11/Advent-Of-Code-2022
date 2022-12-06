data = open("Day 6\input.txt", "r").readlines()

def Part1(data):
    data=data[0]
    #process input
    for i in range(len(data)):
        marker=data[i:i+4]
        for index,m in enumerate(marker):
            if marker.count(m)>1:
                break
            if index==3:
                return i+4

def Part2(data):
    data=data[0]
    #process input
    for i in range(len(data)):
        marker=data[i:i+14]
        for index,m in enumerate(marker):
            if marker.count(m)>1:
                break
            if index==13:
                return i+14


print(Part1(data))
#1723
print(Part2(data))
#3708