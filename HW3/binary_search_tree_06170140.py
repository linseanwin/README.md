class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def insert(self, root, val):
        
        NewNode = TreeNode(val)
        if root:
            if val <= root.val:
                if root.left:
                    return Solution.insert(self, root.left, val)
                else:
                    node = TreeNode(val)
                    root.left = node
                    
            else:
                if root.right:
                    return Solution.insert(self, root.right, val)
                else:
                    node = TreeNode(val)
                    root.right = node
                    return root.right
        else:
            root=TreeNode(val)
            return root
            
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
      
#參考資料:https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
        #https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%85%83%E6%90%9C%E5%B0%8B%E6%A8%B9
        #https://github.com/C-WeiYu/WeiYu/blob/master/HW3/binary_search_tree_06170201.py
        #https://github.com/samuel871211/My-python-code/blob/master/HW3/binary_search_tree_06170225.py
