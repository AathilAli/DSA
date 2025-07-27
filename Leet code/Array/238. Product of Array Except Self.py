class Solution(object):
    def productExceptSelf(self, nums):
        final=[1]*len(nums)
        preffix=1
        for i in range(len(nums)):
            final[i]=preffix
            preffix=preffix*nums[i]
        suffix=1
        for i in range(len(nums)-1,-1,-1):
            final[i]=final[i]*suffix
            suffix=suffix*nums[i]
        return final
        
