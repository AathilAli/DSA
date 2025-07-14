class Solution(object):
    def reverse(self, x):
        y = abs(x)
        rev = 0
        while y > 0:
            id = y % 10
            rev=rev * 10 + id
            y = y // 10
            if rev > (2**31)-1:
                return 0
        if (x < 0):
            return -rev
        else:
            return rev
