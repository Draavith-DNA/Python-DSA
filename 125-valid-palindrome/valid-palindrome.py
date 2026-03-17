class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalize = ""
        for i, value in enumerate(s):
            if value.isalnum():
                normalize += value.lower()

        left = 0
        right = len(normalize)-1
        while left < right:
            if normalize[left] != normalize[right]:
                return False
            left += 1
            right -= 1
            
        return True
