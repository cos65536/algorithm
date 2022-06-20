a = input()
b = input()

result = 0
start = 0

while a.find(b,start)!=-1:
    c = a.find(b,start)
    start = c+len(b)
    result += 1
    
print(result)
