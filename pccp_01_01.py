#2022-08-25
#최소직사각형
#https://school.programmers.co.kr/learn/courses/30/lessons/86491?language=python3


import sys
import json
import string

rst = 0
str_in = sys.stdin.readline()
str_in = str_in.replace('\n', '')

def solution(input_string):
    answer = ''
    tempStr = ''
    strCnt = 0
    dic = {}
    for i in range(97, 123):
        dic[chr(i)] = 0

    for i in range(0, len(input_string)):
        dic[input_string[i]] += 1
        if dic[input_string[i]] >= 2:
            if input_string[i - 1] != input_string[i]:
                if(answer.count(input_string[i])) == 0:
                    answer += input_string[i]
                
    if answer == '':
        answer = 'N'
    answer = sorted(answer)
    answer = ''.join(answer)
    return answer

rst = solution(str_in)
print(rst)