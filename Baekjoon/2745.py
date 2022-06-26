import sys
input = sys.stdin.readline

a,b = map(str, input().split())
b = int(b)
result = 0

for i in range(len(a)):
    if a[i].isdigit():
        result += int(a[i]) * (b ** (len(a)-i-1))
    else:
        result += (ord(a[i]) - 55) * (b ** (len(a)-i-1))

print(result)