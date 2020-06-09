class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        
        if not t and not s or not s:
            return True
        elif not t:
            return False
        
        for i in range(len(t)):
            if t[i] == s[j]:
                j += 1
            if j == len(s):
                return True
        return False
        