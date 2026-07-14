class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        existing_char = {}
        for i, char in enumerate(s):
            while (char in existing_char) and (existing_char[char]):
                cur_char = s[left]
                existing_char[cur_char] = False
                left += 1
            existing_char[char] = True
            longest = max(longest, i - left + 1)
        return longest