class Solution(object):
    def missingNumber(self, nums):
        sum=0
        total=0
        n=len(nums)+1
        sum=(n*(n-1)) // 2
        for i in nums:
            total+=i
        print(total ,sum)
        return sum - total
