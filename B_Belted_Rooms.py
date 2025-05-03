def check(s,i,j):
    if (s[i] != s[j]):
            return False
    i+=1
    j-=1
    if (i<j):
        return check(s,i,j) 
    return True      
s= "samimas"
i=0
j=len(s)-1
res=check(s,i,j)
print(res)