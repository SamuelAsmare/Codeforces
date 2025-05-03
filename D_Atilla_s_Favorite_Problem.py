t = int(input()) # test cas
for _ in range(t):
    n=int(input())
    s=input()
    s=sorted(s)
    temp=s[-1]
    print(ord(temp)-96)

