from collections import Counter
t = int(input()) # test cas
count=0
for _ in range(t):
    li= list (map(int,input().split()))
    fre=Counter(li)
    if fre[1]>=2:
        count+=1
print(count)