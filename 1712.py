import sys
import math
sys.stdin = open("input.txt", "rt")

a, b, c = map(float,input().split())
rst = 0
if c <= b:
    rst = -1
elif int(a / (c-b)) == a / (c-b):
    rst = int(a / (c-b) +1)
else:
    rst = math.ceil(a / (c-b))
    

print(rst)
