class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # solution2: hashmap
        hm={num: i for i, num in enumerate(numbers)}
        for i, num in enumerate(numbers):
            if target-num in hm:
                return [i+1, hm[target-num]+1]