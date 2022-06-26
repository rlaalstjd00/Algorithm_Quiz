import sys
input = sys.stdin.readline

T = int(input())

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def lcm(a,b,gcd):
    return int(gcd * (a/gcd) * (b/gcd))

for i in range(T):
    a,b = map(int, input().split())
    print(lcm(a,b,gcd(a,b)))