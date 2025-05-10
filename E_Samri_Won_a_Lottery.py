t = int(input())
for _ in range(t):
   
    s = list(map(int, input()))
    if (sum(s[:3]) == sum(s[3:])):
        print("YES")
    else:
        print("NO")
