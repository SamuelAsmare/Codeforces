r1,c1,r2,c2 = list(map(int , input().split()))
chess = [[0 for _ in range(8)] for _ in range(8)]
chess[r1-1][c1-1] = 1
chess[r2-1][c2-1] = 2
ans = [0,0,0]
def rook(row,col):
    if (r1 == r2 and c1 == c2):
        ans[0] = 1 
        return
    row , col = r1-1 , c1 -1
    if row >= 8 or row<0 or col <0 or col>=8 or chess[col][row] == 2:
        return 0
    return 1 + 



def bishop():

def king():
