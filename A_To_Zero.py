import math
t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))

    count =0
  
    if not n & 1:
        count = math.ceil(n/(k-1))
    else:
        n = n-k
        
        count=math.ceil(n/(k-1))
        count+=1
    print(count)