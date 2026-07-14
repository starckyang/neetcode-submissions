class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        right_smaller = [0]*len(heights)
        right_stack = []
        for i, height in enumerate(heights):
            while right_stack and height<right_stack[-1][1]:
                index, h = right_stack.pop()
                right_smaller[index] = i-1-index
            right_stack.append((i, height))
        if right_stack:
            for i, h in right_stack:
                right_smaller[i] = len(heights)-1-i

        left_smaller = [0]*len(heights)
        left_stack = []
        for i in range(len(heights)):
            rev_i = -i-1
            rev_h = heights[rev_i]
            while left_stack and rev_h<left_stack[-1][1]:
                index, h = left_stack.pop()
                left_smaller[index] = index-rev_i-1
            left_stack.append((rev_i, rev_h))
        if left_stack:
            for i, h in left_stack:
                left_smaller[i] = i+len(heights)


        largest = 0
        for i, h in enumerate(heights):
            area = h * (left_smaller[i] + right_smaller[i] + 1)
            if area>largest:
                largest = area
        return largest