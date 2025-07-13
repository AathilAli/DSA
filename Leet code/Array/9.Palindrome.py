class Solution(object):
    def isPalindrome(self, x):
        reversed=0
        orginal=x
        while(x > 0):
            a=x % 10
            reversed=reversed * 10 + a
            x=x//10
        return True if reversed==orginal else False
