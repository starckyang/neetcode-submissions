import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if not (nums1 and nums2):
            r_num = nums1 if nums1 else nums2
            return r_num[len(r_num)//2] if len(r_num)%2==1 else \
                   (r_num[len(r_num)//2]+r_num[len(r_num)//2-1])/2
        
        (l_num, s_num) = (nums1, nums2) if len(nums1) >= len(nums2) else (nums2, nums1)
        len_diff = len(l_num) - len(s_num)

        odd = len_diff%2 != 0
        if len_diff%2 == 0:
            ns_num = [-math.inf] * (len_diff//2) + s_num + [math.inf] * (len_diff//2)
        else:
            ns_num = [-math.inf] * (len_diff//2+1) + s_num + [math.inf] * (len_diff//2)
        if len(l_num) == 1:
            return (l_num[0] + ns_num[0])/2
        l, r = 0, len(l_num)-1
        while l<=r:
            m = (l+r)//2
            if m == len(l_num)-1:
                if l_num[m] > ns_num[0]:
                    if odd == False:
                        return (min(l_num[m], ns_num[1])+ns_num[0])/2
                    return min(l_num[m], ns_num[1])
                else:
                    if odd == False:
                        return (l_num[m]+ns_num[0])/2
                    return ns_num[0]
            elif m == 0:
                if l==r:
                    if l_num[m] < ns_num[-1]:
                        if odd == False:
                            return (min(l_num[m+1], ns_num[-1])+l_num[m])/2
                        return min(l_num[m+1], ns_num[-1])
                    else:
                        if odd == False:
                            return (l_num[m]+ns_num[-1])/2
                        return l_num[m]
                else:
                    final = sorted(l_num[0:2] + ns_num[-2:])
                    if odd:
                        return final[2]
                    return (final[1] + final[2])/2
            elif (l_num[m-1] <= ns_num[len(ns_num)-m]) and (l_num[m] >= ns_num[len(ns_num)-m-1]):
                if odd == False:
                    return (max(l_num[m-1], ns_num[len(ns_num)-m-1]) + min(l_num[m], ns_num[len(ns_num)-m]))/2
                return min(l_num[m], ns_num[len(ns_num)-m])
            elif l_num[m-1] > ns_num[len(ns_num)-m]:
                r = m-1
            else:
                l = m+1