import sys
rst = 0
numLIst = [1, 5, 10, 50]
rstList = [0 for i in range(2000)]
str_in = int(sys.stdin.readline())


def solve(value, nVal, deepCnt):
    global rst
    if str_in == deepCnt:
        # print(value)
        if rstList[value] == 0:
            rstList[value] = 1
            rst = rst + 1
            #rstList += 1
        return
    for i in range(nVal, 4):
        # print(i)
        solve(value + numLIst[i], i, deepCnt + 1)
    #return


solve(0, 0, 0)

print(rst)
