import sys
sys.stdin = open("input.txt", "rt")

a, b, v = map(int,input().split())


if a == v:
    rst = 1
elif (v-a) // (a-b) < 1 or (v-a) % (a-b) != 0:
    rst = (v-a) // (a-b) +2
else:
    rst = (v-a) // (a-b) +1
print(rst)

    
