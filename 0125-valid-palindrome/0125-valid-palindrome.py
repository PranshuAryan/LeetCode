class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        left, right = 0, len(s)-1
        while(left < right):
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if (s[left] != s[right]):
                return False  
            right-=1
            left+=1
        else:
            return True
        
