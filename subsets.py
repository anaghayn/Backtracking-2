# Time Complexity: O(2^n)
# Space Complexity: O(n)

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]

        def helper(nums, index, path):
            #base case
            if index == len(nums): #when we run out of index (leaf exhaustion)
                result.append(copy.deepcopy(path))
                return

            #action
            #do not choose
            helper(nums, index+1, path)

            #choose
            path.append(nums[index])
            helper(nums, index+1, path)
            path.pop()

        helper(nums, 0, [])
        return result
