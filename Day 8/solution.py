data = open("Day 8/input.txt", "r").readlines()


def ProcessInput():
    trees = []
    for tree in data:
        if tree[-1] == "\n":
            trees.append(tree[:-1])
            continue
        trees.append(tree)
    return trees


def Part1(trees):
    visible = 0
    for treeX in range(0, len(trees)):
        if treeX == 0 or treeX == len(trees):
            visible += 1
            continue
        for treeY in range(len(trees[treeX])):
            if treeY == 0 or treeY == len(trees[treeX]):
                visible += 1
                continue
            row=[]
            collumn=[]
            currentTree = int(trees[treeX][treeY])
            for r in range(len(trees)):
                collumn.append(int(trees[r][treeY]))
            for c in range(len(trees[treeX])):
                row.append(int(trees[treeX][c]))
            if max(row[:treeY])<currentTree or max(row[treeY:])<currentTree or max(collumn[:treeX])<currentTree or max(collumn[treeX:]<currentTree):
                visible+=1
    return visible


print(Part1(ProcessInput()))
