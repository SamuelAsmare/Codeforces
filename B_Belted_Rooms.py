from typing import List
from collections import defaultdict
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dic=defaultdict(int)
        counter=0
        for i,j in dominoes:   
            dic[tuple(sorted((i,j)))]+=1
        print(dic)
        for items in dic:
            counter+=(dic[items]-1)
        return counter
sol=Solution()
arr=[[2,1],[3,4],[5,6],[1,2]]
print(sol.numEquivDominoPairs(arr))

