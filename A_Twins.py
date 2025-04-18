t=int(input())
coins=list(map(int,input().split(" ")))
if(len(coins) != t):
    print("error")
else:
    count=0
    coins.sort(reverse=True)
    right=sum(coins)
    left=0
    for i in range(len(coins)):
        right-=coins[i]
        left+=coins[i]
        count+=1
        if(left>right):
            break
    print(count)
