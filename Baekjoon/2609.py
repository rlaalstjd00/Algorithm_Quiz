import sys

input = sys.stdin.readline

a,b  = map(int, input().split())

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def lcm(a, b, gcd):
    return gcd * (a/gcd) * (b/gcd)

gcd = gcd(a,b)
print(gcd)
print(int(lcm(a,b,gcd)))
