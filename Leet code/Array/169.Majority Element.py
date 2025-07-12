class Solution(object):
    def majorityElement(self, nums):
        count=0
        final_result=None
        for i in nums:
            if count==0:
                final_result=i
            if final_result==i:
                count+=1
            else:
                count-=1
        return final_result
        
