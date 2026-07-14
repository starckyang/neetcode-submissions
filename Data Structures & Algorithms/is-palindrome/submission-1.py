class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_chars = {chr(i): True for i in range(ord("a"), ord("a")+26)}
        nums = {str(i): True for i in range(10)}
        cleaned = []
        for char in s:
            if char in nums:
                cleaned.append(char)
            elif char.lower() in lower_chars:
                cleaned.append(char.lower())

        left, right = 0, len(cleaned)-1
        while left <= right:
            if cleaned[left] != cleaned[right]:
                return False
            else:
                left, right = left+1, right-1
        return True
            
