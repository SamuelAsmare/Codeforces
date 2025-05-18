n , k = list(map(int,input().split()))
arr = list(map(int, input().split()))
if(len(set(arr))<k):
    print("NO")
    exit()
else:
    print("YES")
    ans , seen = [] , set()
    for i in range(len(arr)):
        if arr[i] not in seen:
            ans.append(i+1)
            seen.add(arr[i])
        if len(ans) >= k:
            break
    print(*ans)
        
    
