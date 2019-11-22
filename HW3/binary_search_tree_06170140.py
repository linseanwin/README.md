class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def insert(self, root, val):
        if val <= root.val and root.left is None:
            root.left = TreeNode(val)
            return root.left
        if val > root.val and root.right is None:
            root.right = TreeNode(val)
            return root.right
        if val <= root.val and root.left:
            root = root.left
        if val> root.val and root.right:
            root = root.right
            
    def search(self, root, val):
        if root is None:
            return root
        if root.val == val:
            return root
        if root.val < val:
            return self.search(root.right,val)
        if root.val > val:
            return self.search(root.left,val)
    def delete(self, root, target):
        pass
    def modify(self, root, target, new_val):
        pass
      
參考資料:https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
        https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%85%83%E6%90%9C%E5%B0%8B%E6%A8%B9
        
        AB班許多王牌高手
