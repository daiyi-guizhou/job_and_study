

## solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            return _get_depth(root)
def _get_depth(_a):
    _res_l = _get_depth(_a.left) if _a.left else 0
    _res_r = _get_depth(_a.right) if _a.right else 0
    if _res_l > _res_r:
        return _res_l + 1
    else:
        return _res_r + 1

```