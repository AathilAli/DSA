class Solution(object):
    def singleNumber(self, nums):
        xor=0
        for x in nums:
            xor ^= x
        return xor
