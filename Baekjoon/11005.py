import sys
input = sys.stdin.readline

n,b = map(int, input().split())
result = []

while n >= b :
    result.append(n%b)
    n = n//b
result.append(n)

result = result[::-1]

for i in range(len(result)):
    if result[i] >= 10:
        result[i] = chr(result[i]+55)
    else:
        result[i] = str(result[i])

print("".join(result))


