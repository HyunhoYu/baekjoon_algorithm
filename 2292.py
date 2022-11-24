import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
rst = 1
i = 1 
tool = rst 
while True:
    rst += 6*i
    if n <= rst:
        if n == 1:
            print(1)
        else:
            print(i+1)
        break
    
    i += 1