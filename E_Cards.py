n=int(input())
arr=list(map(int,input().split()))
temp=arr.copy()
temp.sort()
summ=temp[0] + temp[-1]
pairs=[]
used=[False]*n
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if (arr[i]+arr[j]==summ   and not used[i] and not used[j]):
            pairs.append([i+1,j+1])
            used[i]=True
            used[j]=True
            break
for i in range(len(pairs)):
    # pairs[i].sort()
    print(*pairs[i])