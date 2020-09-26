import sys
numLIst = [1, 5, 10, 20]

str_in = sys.stdin.readline()
solve(0, 0)
print(numLIst)


def solve(value, deepCnt):
    if int(str_in) == deepCnt - 1:
        print(value)
        return
    for var in numLIst:
        solve(value + var, deepCnt + 1)
    return