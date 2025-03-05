class Solution(object):
    def applyOperations(self, nums):
        for i in range(0,len(nums)-1):
            if(nums[i]==nums[i+1]):
                nums[i]*=2
                nums[i+1]=0
        for i in nums:
            if(i==0):
                nums.remove(i)
                nums.append(0)      
        return nums
