class Solution(object):
    
    def merge(self,left,right):
        ans = []
        while len(left) > 0 or len(right) > 0:        
            if len(left) > 0 and len(right) > 0:     
                if left[0] <= right[0]:              
                    ans.append(left.pop(0))       
                else:
                    ans.append(right.pop(0))      
            elif len(left) > 0:                     
                ans.append(left.pop(0))
            elif len(right) > 0:
                ans.append(right.pop(0))
        return ans

def merge_sort(self,nums):
        if len(nums) <= 1:
            return nums
        else:
            number = len(nums)//2               
            left = Solution().merge_sort(list[:number])     
            right = Solution().merge_sort(list[number:])
            
            return Solution().merge(left, right)
