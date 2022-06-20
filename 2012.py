import sys

n = int(input())
a = [int(sys.stdin.readline()) for i in range(n)]

a.sort()

result = 0

for i in range(n):
    result += abs(a[i]-(i+1))

print(result)