# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToAvg(self, root) : 
        arr, q = [], deque()
        q.append(root)

        while q :
            node = q.pop()
            arr.append(node.val)
            if node.left :
                q.append(node.left)
            if node.right : 
                q.append(node.right)
        return sum(arr)//len(arr)

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        counter, q = 0, deque()
        q.append(root)
        while q : 
            node = q.pop()
            if self.equalToAvg(node) == node.val: 
                counter += 1 

            if node.left : 
                q.append(node.left)
            if node.right : 
                q.append(node.right)

        return counter 
        