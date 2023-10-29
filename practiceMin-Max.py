import math


def minmax(current, nodeIndex, maxTurn, scoress, treeDepth):
    if current == treeDepth:
        return scoress[nodeIndex]

    if maxTurn:
        return max(
            minmax(current + 1, nodeIndex * 2, False, scoress, treeDepth),
            minmax(current + 1, nodeIndex * 2 + 1, False, scoress, treeDepth),
        )
    else:
        return min(
            minmax(current + 1, nodeIndex * 2, True, scoress, treeDepth),
            minmax(current + 1, nodeIndex * 2 + 1, True, scoress, treeDepth),
        )


def main():
    scores = []

    n = int(input("Enter number of nodes (must be power of 2) : "))

    print("Enter scores : ")
    for i in range(n):
        scores.append(int(input()))

    treeDepth = math.log(len(scores), 2)
    print("The optimal value is :", minmax(0, 0, True, scores, treeDepth))


if __name__ == "__main__":
    main()
