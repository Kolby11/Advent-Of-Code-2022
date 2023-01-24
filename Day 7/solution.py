lines = open("Day 7\input.txt", "r").readlines()


def ProcessInput():
    data = []
    for line in lines:
        if line != lines[-1]:
            line = line.split(" ")
            line[-1] = line[-1][:-1]
        else:
            line = line.split(" ")
        data.append(line)
    return data


class File:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = int(size)
        self.parent = parent


class Directory:
    def __init__(self, name, parent=None, children=None):
        self.name = name
        self.parent = parent
        self.children = children or []

    def size(self):
        return sum(c.size for c in self.children)


def buildFileTree(data):
    root = Directory("root")
    currentDc = root
    for line in data:
        if line[0] == "$":
            if line[1] == "ls":
                continue
            command, target = line[1], line[2]
            if command == "cd":
                if target == "..":
                    currentDc = currentDc.parent
                else:
                    for child in currentDc.children:
                        if child.name == target:
                            currentDc = child
        else:
            v1, name = line[0], line[1]
            if v1 == "dir":
                currentDc.children.append(Directory(name, currentDc))
            else:
                currentDc.children.append(File(name, v1, currentDc))
    return root


part1 = 0


def Part1(root, limit):
    count = 0
    for dc in root.children:
        if isinstance(dc, File):
            if dc.size < limit:
                count += 1
        else:
            if dc.size() < limit:
                count += 1
            count += Part1(dc, limit)
    return count


print(Part1(buildFileTree(ProcessInput()), 100000))
