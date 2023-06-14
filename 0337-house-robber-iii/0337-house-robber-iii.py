class Solution(object):
    def rob(self, root):
        def superrob(node):
            if not node: return (0, 0)
            left, right = superrob(node.left), superrob(node.right)
            now = node.val + left[1] + right[1]
            later = max(left) + max(right)
            
            return (now, later)
            
        return max(superrob(root))