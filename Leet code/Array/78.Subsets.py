class Solution(object):
    def subsets(self, nums):
        result=[[]]
        for num in nums:
            temp_result=[]
            for subset in result:
                new_subset=subset+[num]
                temp_result.append(new_subset)
            result+=temp_result
        return result
