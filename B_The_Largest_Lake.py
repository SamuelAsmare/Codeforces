# import sys
# sys.setrecursionlimit(10**6)

# t = int(input())
# for _ in range(t):
#     n, m = map(int, input().split())
#     grid = [list(map(int, input().split())) for _ in range(n)]
#     ans = 0

#     def dfs(i, j):
#         if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0:
#             return 0
#         temp = grid[i][j]
#         grid[i][j] = 0  # Mark as visited
#         return (temp +
#                 dfs(i + 1, j) +
#                 dfs(i - 1, j) +
#                 dfs(i, j + 1) +
#                 dfs(i, j - 1))

#     for i in range(n):
#         for j in range(m):
#             if grid[i][j] != 0:
#                 ans = max(ans, dfs(i, j))

#     print(ans)
import sys

input = sys.stdin.read

def main():
    
    inputdata = input().split()
    t = int(inputdata[0])  
    index = 1  
    results = []  
    for _ in range(t):
        
        n, m = int(inputdata[index]), int(inputdata[index + 1])
        index += 2 

      
        grid = []
        for _ in range(n):
            
            row = list(map(int, inputdata[index:index + m]))
            grid.append(row)
            index += m  

       
        ans = 0

        
        def iterative_dfs(i, j):
            
            stack = [(i, j)]
            total = 0
 
            while stack:
                
                x, y = stack.pop()

               
                if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 0:
                    continue  
               
                total += grid[x][y]

               
                grid[x][y] = 0

              
                stack.extend([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])

            return total

        
        for i in range(n):
            for j in range(m):
             
                if grid[i][j] != 0:
                 
                    component_sum = iterative_dfs(i, j)
                  
                    ans = max(ans, component_sum)

       
        results.append(str(ans))

    
    sys.stdout.write("\n".join(results) + "\n")


if __name__ == '__main__':
    main()
