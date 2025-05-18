t = int(input())
ans  = 0
for _ in  range(t):
    arr = list(map(int , input().split()))
    if (arr.count(1)>=2):
        ans += 1
print(ans)

