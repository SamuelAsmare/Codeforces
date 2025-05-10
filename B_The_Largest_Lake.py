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


import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        grid = [list(map(int, input().split())) for _ in range(n)]
        ans = 0

        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0:
                return 0
            temp = grid[i][j]
            grid[i][j] = 0  # Mark as visited
            return (temp +
                    dfs(i + 1, j) +
                    dfs(i - 1, j) +
                    dfs(i, j + 1) +
                    dfs(i, j - 1))

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    ans = max(ans, dfs(i, j))

        print(ans)

if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
