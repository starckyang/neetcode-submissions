class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        if len(hand)%groupSize!=0:
            return False

        hm={}
        for h in hand:
            if not h in hm:
                hm[h]=1
            else:
                hm[h]+=1

        for h in hand:
            if hm[h]!=0:
                for i in range(groupSize):
                    if h+i in hm and hm[h+i]>0:
                        hm[h+i]-=1
                    else:
                        return False
        return True
