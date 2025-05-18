n = int(input())  
curr = 0
maxval = 0

for _ in range(n):
    a, b = map(int, input().split())  
    curr-= a 
    curr += b  
    maxval = max(maxval, curr)  

print(maxval)
