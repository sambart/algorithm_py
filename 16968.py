import sys

str_in = sys.stdin.readline()
arr = list(str_in.strip())
nVal = 0
result = 0
prevVar = ''
for var in arr:
    nVal = 26
    if var == 'd':
        nVal = 10
    if result == 0:
        result = nVal        
    else:
        if prevVar == var:
            nVal -= 1        
        result *= nVal
 
    prevVar = var
print(result)
    