t = int(input())

for i in range(t):
    n = int(input())
    count = 0
    arr =  list(map(int, input().split()))

    arr1 = []

    minval = float("inf")
    for i in range(len(arr)-1, -1, -1):
        minval = min(minval, arr[i])

        arr1.append(minval)
    
    arr1.reverse()

    for i in range(len(arr)):
        if arr[i]> arr1[i]:
            count+=1
    print(count)





