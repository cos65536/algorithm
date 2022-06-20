a = int(input())
b = 1000-a

result = 0

en = [500, 100, 50, 10, 5, 1]

for i in en:
    if b//i>=1:
        result += b//i
        b %= i

print(result)