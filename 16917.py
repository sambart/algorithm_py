import sys

aChickenValue, bChickenValue, cChickenValue, aChickenCnt, bChickenCnt = input().split()
result = 0
aChickenValue = int(aChickenValue)
bChickenValue = int(bChickenValue)
cChickenValue = int(cChickenValue)
aChickenCnt = int(aChickenCnt)
bChickenCnt = int(bChickenCnt)


aRst = (aChickenValue * aChickenCnt) + (bChickenValue * bChickenCnt)
bRst = cChickenValue * (min(aChickenCnt, bChickenCnt) * 2)
if aChickenCnt > bChickenCnt:
    bRst += (aChickenCnt - bChickenCnt) * aChickenValue
else:
    bRst += (bChickenCnt - aChickenCnt) * bChickenValue
cRst = max(aChickenCnt, bChickenCnt) * 2 * cChickenValue

print(min(aRst, bRst, cRst))
