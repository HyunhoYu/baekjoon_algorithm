import sys
sys.stdin = open("input.txt", "rt")
"""" 내코드
n = int(input())
rst = n
tool = rst
void_list =[]
for _ in range(n):
    s = input()
    for i in range(len(s)-2):
        if tool != rst:
            tool -=1
            break
        void_list.append(s[i+2: len(s)])    
        print(void_list) 
        for x in void_list:
            if s[i] in x:
                rst -=1 
                
        void_list.clear()
        
                

print(rst)

""" 
n = int(input())
cnt = n

for _ in range(n):
    s = input()
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            pass
        elif s[i] in s[i+1:]:
            cnt -= 1
            break

print (cnt)




