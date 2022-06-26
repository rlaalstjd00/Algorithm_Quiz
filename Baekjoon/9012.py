import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    ps = list(input())
    cnt = 0
    for i in ps:
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1
        if cnt < 0:
            print('NO')
            break
    if cnt == 0:
        print('YES')
    elif cnt > 0:  
        print('NO')

