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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        tree = inOrderTrav(root,[])
        return tree[k-1]
        