from collections import deque

class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def level_order_grouped(root):
   result=[]
   que=deque([root])
   count=0
   while(que):
      level=[]
      for _ in range(len(que)):
         node = que.popleft()
         level.append(node.val)
         if node.left:
            que.append(node.left)
         if (node.right):
            que.append(node.right)
      count+=1
      result.append(level)
   print(count)
   return result 

# Example Usage:
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(level_order_grouped(root))  # Output: [[1], [2, 3], [4, 5]]


sam=deque([])
print(len(sam))