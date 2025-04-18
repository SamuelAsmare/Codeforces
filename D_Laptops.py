s = int(input())
arr = []
for i in range(s):
    l1 = list(map(int, input().split()))
    arr.append(l1)


arr.sort(key = lambda x: x[0])

flag = True
for i in range(1, len(arr)):
    if arr[i][1] < arr[i-1][1]:
        print("Happy Alex")
        flag = False
        break
if flag:
    print("Poor Alex")
