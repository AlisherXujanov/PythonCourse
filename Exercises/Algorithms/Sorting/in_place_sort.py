
# IN PLACE ALGORITHM
# This algorithm does not create a new list, it modifies the original list
# It is best when it comes to memory usage
# It is not the best when it comes to time complexity because it has to shift the elements

# Time complexity means how long it takes to run the algorithm
# Space complexity means how much memory it uses

# FORMULA
# i <= j
# i is the left pointer
# j is the right pointer

nums = [3, 2, 2, 3, 1, 5]  # in-place algorithm
target = 3

# nums = [3, 2, 2, 3, 1, 5]  =>  3, 5   =?  i==3 yes  switch
# nums = [5, 2, 2, 3, 1, 3]  =>  5, 1   =?  i==5 no   Do nothing
# nums = [5, 2, 2, 3, 1, 3]  =>  2, 1   =?  i==2 no   Do nothing
# nums = [5, 2, 2, 3, 1, 3]  =>  2, 1   =?  i==2 no   Do nothing
# nums = [5, 2, 2, 3, 1, 3]  =>  3, 1   =?  i==3 yes  switch
# nums = [5, 2, 2, 1, 3, 3]  =>  i <= j  finish


# Example: Remove all the 3s from the list
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0  # left pointer
        j = len(nums) - 1  # right pointer
        while i <= j:  # when left is less than or equal to right
            if nums[i] == val:  # if left pointer is equal to val
                nums[i], nums[j] = nums[j], nums[i]  # switch left and right
                j -= 1  # move right pointer to the left
            else:
                i += 1  # move left pointer to the right
        return i  # return the length of the list

s = Solution()
k = s.removeElement(nums, target)
print(k)
