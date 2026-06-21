# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inOrderTrav(node,arr):
    if node:
        inOrderTrav(node.left,arr)
        arr.append(node.val)
        inOrderTrav(node.right,arr)
    return arr

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        tree = inOrderTrav(root,[])
        for i in range(1, len(tree)):
            if tree[i] <= tree[i - 1]:
                return False
        return True