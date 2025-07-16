class Solution(object):
    def isAnagram(self, s, t):
        d={}
        for char in s:
            if char not in d:
                d[char]=1
            else:
                d[char]+=1
        for char in t:
            if char not in d:
                return False
            else:
                if d[char]==1:
                    del d[char]
                elif d[char] > 1:
                    d[char]-=1
        return True if d=={} else False
