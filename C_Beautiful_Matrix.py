mymat=[]  # zero indexed mat
for _ in range(5):
    row = list(map(int,input().split())) # each row
    mymat.append(row)
for i in range(5):
    for j in range(5):
        if mymat[i][j]==1:
            print(abs(i-2) + abs(j-2))
            exit()