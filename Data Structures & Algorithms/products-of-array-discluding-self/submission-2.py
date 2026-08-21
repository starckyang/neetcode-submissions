class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # division

        n_zeros=0
        all_product=1
        non_zero_product=1

        for num in nums:
            if num==0:
                n_zeros+=1
            else:
                non_zero_product*=num
            all_product*=num

        res=[]
        for num in nums:
            if num==0:
                if n_zeros==1:
                    res.append(int(non_zero_product))
                else:
                    res.append(0)
            else:
                res.append(int(all_product/num))

        return res