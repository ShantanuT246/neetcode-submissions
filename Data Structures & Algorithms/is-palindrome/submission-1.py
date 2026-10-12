class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = s.split(" ")
        s = ''.join([c for c in s if c.isalnum()]).lower()
        print(s)
        i = 0
        j = len(s) - 1
        while(i <= j):
            if s[i] == s[j]:
                i += 1
                j -= 1
                continue
            return False
        return True
