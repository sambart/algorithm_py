#2022-08-25
#최소직사각형
#https://school.programmers.co.kr/learn/courses/30/lessons/86491?language=python3


import sys
import json

rst = 0
str_in = sys.stdin.readline()
size_in = json.loads(str_in)

def solution(sizes):
    answer = 0
    maxSize = 0
    maxPair = 0

    for sizeMap in sizes:
        if sizeMap[0] > sizeMap[1]:
            highV = sizeMap[0]
            lowV = sizeMap[1]
        else:
            highV = sizeMap[1]
            lowV = sizeMap[0]

        if maxSize < highV:
            maxSize = highV            
        if lowV > maxPair:
            maxPair = lowV
    answer = maxSize * maxPair
    return answer

rst = solution(size_in)
print(rst)