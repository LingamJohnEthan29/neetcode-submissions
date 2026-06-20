# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def sameTree(node1,node2):
    if not node1 and not node2:
        return True
    else:
        if node1 and not node2:
            return False
        elif not node1 and node2:
            return False
        elif node1.val != node2.val:
            return False
        else:
            return (sameTree(node1.left,node2.left) and sameTree(node1.right,node2.right))
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p and q:
            return False
        elif p and not q:
            return False
        elif p.val != q.val:
            return False
        return sameTree(p,q)

        